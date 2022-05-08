import json
import time
import tkinter as tk
from functools import partial
from pathlib import Path
from threading import Thread
from tkinter import ttk
from tkinter.filedialog import askopenfile, asksaveasfile
from typing import Optional

import midi_percussion as mp

import mingus.tools.mingus_json as mingus_json
from mingus.containers import PercussionNote, Track
from mingus.containers.raw_snippet import RawSnippet
from mingus.midi.fluid_synth2 import FluidSynthPlayer
from mingus.midi.get_soundfont_path import get_soundfont_path
from mingus.midi.sequencer2 import Sequencer

# A global variable for communicating with the click track thread
click_track_done = False
player_track_done = False

# noinspection SpellCheckingInspection
KEYS = ' zxcvbnm,./'


class TrackGUI:
    def __init__(self, widget=None, track=None, path: Optional[str] = None):
        self.widget = widget
        self.track = track
        self.path = path

        if path:
            full_path = Path(path).expanduser()
            with open(full_path, 'r') as fp:
                self.track = mingus_json.load(fp)

    def destroy_widget(self):
        if self.widget:
            self.destroy_widget()
        self.widget = None

    def load(self):
        fp = askopenfile()
        if fp:
            try:
                self.path = fp.name
                self.track = mingus_json.load(fp)
            except Exception as e:
                print(f"An error occurred while writing to the file: {e}")
            finally:
                # Make sure to close the file after using it
                fp.close()


class ClickTrack(Thread):
    instrument = 85

    def __init__(self, synth, percussion_channel, bpm, beats_per_bar):
        super().__init__()
        self.synth = synth
        self.percussion_channel = percussion_channel
        self.sleep_seconds = (1.0 / bpm) * 60.0
        self.beats_per_bar = beats_per_bar

    def run(self):
        global click_track_done
        count = 0
        while not click_track_done:
            if count == 0:
                velocity = 127
            else:
                velocity = 50
            self.synth.noteon(self.percussion_channel, self.instrument, velocity)
            time.sleep(self.sleep_seconds)

            count += 1

            if count == self.beats_per_bar:
                count = 0


class PlayOld(Thread):
    def __init__(self, synth, score):
        super().__init__()
        self.synth = synth
        self.sequencer = Sequencer(score=score)

    def run(self):
        global player_track_done

        self.sequencer.play_score(self.synth)

        # while not player_track_done:
        #     print('beat')
        #     time.sleep(3)

        print('player_done')


class Play(Thread):
    def __init__(self, synth, sequencer):
        super().__init__()
        self.synth = synth
        self.sequencer = sequencer

    def run(self):
        global player_track_done

        def stop_func():
            global player_track_done
            return player_track_done

        self.sequencer.play_score(self.synth, stop_func=stop_func)

        print('player_done')


class KeyboardDrumSet:
    """
    For creating percussion tracks from the keyboard. This is useful for working out rhythms. It is lacking in
    velocity control.

    SECTIONS

    Assign keys to instruments:

        Key: spinner?  | Instrument: drop-down  | Delete
        "Add" Button

    Define Tracks

    DRUM SET FORMAT
    Dict saved to a Json file in the format:

        drum_set = {
            'instruments': {
                'z': 'Acoustic Bass Drum',
                'm': 'Acoustic Snare'
            },
            'click_track': {
                'bpm': 120,
                'beats_per_bar': 4,
                'enabled': True
            }
        }
    """
    def __init__(self, setup_synth=True, drum_set=None):
        self.recording = {}  # keys are times in milliseconds, values are lists of events
        self.is_recording = False
        self.start_recording_time = None
        self.play_click_track = False

        if drum_set is None:
            self.drum_set = {
                'instruments': {
                    'z': 'Acoustic Bass Drum',
                    'm': 'Acoustic Snare'
                },
                'click_track': {
                    'bpm': 120,
                    'beats_per_bar': 4,
                    'enabled': True
                },
                'tracks': [
                    '~/python_mingus/tracks/test_percussion.json',
                    '~/python_mingus/tracks/test_bass.json'
                ]
            }
        else:
            self.drum_set = drum_set

        self.instruments = self.drum_set['instruments']

        if setup_synth:
            soundfont_path = get_soundfont_path()
            self.synth = FluidSynthPlayer(soundfont_path, gain=1)
            self.synth.load_sound_font()

            self.percussion_channel = 1  # can be any channel between 1-128
            bank = 128  # Must be 128 (at least for the Musescore default sound font)
            preset = 1
            self.synth.fs.program_select(self.percussion_channel, self.synth.sfid, bank, preset)
        else:
            self.synth = None
            self.sound_font = 'not loaded'
            self.percussion_channel = None

        self.velocity = 80
        self.padding = {
            'padx': 2,
            'pady': 2
        }

        self.window = tk.Tk()
        self.window.title("Keyboard Drum Set")

        # Instruments ---------------------------------------------------------------------------------------------
        self.instrument_frame = ttk.LabelFrame(self.window, text='Instruments', borderwidth=5, relief=tk.GROOVE)
        self.instrument_frame.pack(fill=tk.BOTH, expand=tk.YES)
        self.instrument_widgets = []
        self.bound_keys = set()
        self.render_instrument_section()

        # Click track ---------------------------------------------------------------------------------------------
        click_track_frame = ttk.LabelFrame(self.window, text='Click Track', padding=10)
        click_track_frame.pack(fill=tk.BOTH, expand=tk.YES)
        row = 0
        ttk.Label(click_track_frame, text='BPM').grid(row=row, column=0, sticky=tk.W, **self.padding)
        self.bpm = tk.IntVar(value=self.drum_set['click_track']['bpm'])
        spin_box = tk.Spinbox(click_track_frame, from_=50, to=200, increment=1, textvariable=self.bpm)
        spin_box.grid(row=row, column=1, sticky=tk.W, **self.padding)

        row += 1
        ttk.Label(click_track_frame, text='Beats/Bar').grid(row=row, column=0, sticky=tk.W, **self.padding)
        self.beats_per_bar = tk.IntVar(value=self.drum_set['click_track']['beats_per_bar'])
        spin_box = tk.Spinbox(click_track_frame, from_=2, to=16, increment=1, textvariable=self.beats_per_bar)
        spin_box.grid(row=row, column=1, sticky=tk.W, **self.padding)

        row += 1
        ttk.Label(click_track_frame, text='Enable Clicks').grid(row=row, column=0, sticky=tk.W, **self.padding)
        self.play_click_track = tk.BooleanVar(value=self.drum_set['click_track']['enabled'])
        tk.Checkbutton(click_track_frame, variable=self.play_click_track).\
            grid(row=row, column=1, sticky=tk.W, **self.padding)
        
        # Background tracks --------------------------------------------------------------------------------------
        self.tracks_frame = ttk.LabelFrame(self.window, text='Tracks', padding=5)
        self.tracks_frame.pack(fill=tk.BOTH, expand=tk.YES)
        self.tracks = [TrackGUI(path=path) for path in self.drum_set.get('tracks', [])]
        self.render_tracks_section()
        
        # Recorded Controls --------------------------------------------------------------------------------------
        recorder_frame = ttk.LabelFrame(self.window, text='Recorder', padding=5)
        recorder_frame.pack(fill=tk.BOTH, expand=tk.YES)
        tk.Button(recorder_frame, text="|<", command=self.rewind).pack(side=tk.LEFT)
        tk.Button(recorder_frame, text=">", command=self.play).pack(side=tk.LEFT)
        self.start_stop_recording_button = tk.Button(recorder_frame, text="Start", command=self.start_stop_recording)
        self.start_stop_recording_button.pack(side=tk.LEFT)

        # Controls ------------------------------------------------------------------------------------------------
        control_button_frame = ttk.LabelFrame(self.window, text='Controls', padding=5)
        control_button_frame.pack(fill=tk.BOTH, expand=tk.YES)
        tk.Button(control_button_frame, text="Clear", command=self.clear).pack(side=tk.LEFT)
        tk.Button(control_button_frame, text="Save", command=self.save).pack(side=tk.LEFT)
        tk.Button(control_button_frame, text="Quit", command=self.quit).pack(side=tk.LEFT)

        self.window.mainloop()

    # Instruments -------------------------------------------------------------------------------------------------
    def delete_instrument(self, char):
        del self.instruments[char]
        self.render_instrument_section()

    def render_instrument_section(self):
        # Delete all
        for widget in reversed(self.instrument_widgets):
            widget.destroy()
        self.instrument_widgets = []

        for key in self.bound_keys:
            self.window.bind(key, self.do_nothing)

        self.window.update()

        # Draw all
        self.instruments = self.drum_set['instruments']
        row = 0
        for row, (char, instrument) in enumerate(self.instruments.items()):
            instrument_label = ttk.Label(self.instrument_frame, text=f'{char} -> {instrument}')
            instrument_label.grid(row=row, column=0, sticky=tk.W, **self.padding)
            self.instrument_widgets.append(instrument_label)
            delete_instrument_button = tk.Button(
                self.instrument_frame,
                text='Delete',
                command=partial(self.delete_instrument, char)
            )
            delete_instrument_button.grid(row=row, column=1, sticky=tk.E, **self.padding)
            self.instrument_widgets.append(delete_instrument_button)

            self.window.bind(char, self.play_note)
            self.bound_keys.add(char)

        row += 1
        buttons = [
            ('Add Instrument', self.make_instrument_popup),
            ('Load Drum Set', self.load_drum_set),
            ('Save Drum Set', self.save_drum_set),
        ]
        for column, (button_text, command) in enumerate(buttons):
            button = tk.Button(self.instrument_frame, text=button_text, command=command)
            button.grid(row=row, column=column, sticky=tk.W, **self.padding)
            self.instrument_widgets.append(button)
        self.window.update()

    # noinspection PyUnusedLocal
    def add_key_and_instrument(self, ev):
        if self.new_key.get() and self.new_instrument.get():
            self.save_new_instrument_button['state'] = tk.NORMAL

    def save_instrument(self):
        self.top.destroy()
        char = self.new_key.get()
        self.instruments[char] = self.new_instrument.get()
        self.render_instrument_section()

    def make_instrument_popup(self):
        padding = {'padx': 2, 'pady': 2}
        self.top = tk.Toplevel(self.window)

        row = 0
        ttk.Label(self.top, text='Key:').grid(row=row, column=0, sticky=tk.W, **padding)
        self.new_key = tk.StringVar()
        ttk.OptionMenu(self.top, self.new_key, *KEYS, command=self.add_key_and_instrument).\
            grid(row=row, column=1, sticky=tk.W, **padding)

        row += 1
        ttk.Label(self.top, text='Instrument:').grid(row=row, column=0, sticky=tk.W, **padding)
        self.new_instrument = tk.StringVar()
        ttk.OptionMenu(self.top, self.new_instrument, '', *mp.percussion_instruments.keys(),
                       command=self.add_key_and_instrument).\
            grid(row=row, column=1, sticky=tk.W, **padding)

        row += 1
        self.save_new_instrument_button = tk.Button(self.top, text="Save", command=self.save_instrument,
                                                    state=tk.DISABLED)
        self.save_new_instrument_button.grid(row=row, column=0, sticky=tk.W, **padding)
        tk.Button(self.top, text="Cancel", command=lambda: self.top.destroy()).grid(row=row, column=1,
                                                                                    sticky=tk.W, **padding)

    def load_drum_set(self):
        file = askopenfile()
        if file:
            self.drum_set = json.load(file)
            self.render_instrument_section()

    def save_drum_set(self):
        files = [
            ('All Files', '*.*'),
            ('Drum Sets', '*.json')
        ]
        file = asksaveasfile(filetypes=files, defaultextension=".json")
        if file:
            json.dump(self.drum_set, file)
            
    # Tracks -------------------------------------------------------------------------------------------------------
    def render_tracks_section(self):
        # Delete all
        for track in reversed(self.tracks):
            track.destroy_widget()
        self.window.update()

        # Draw all
        row = 0
        for_sequencer = {'tracks': [], 'channels': [], 'bpm': self.bpm.get()}
        for i, track in enumerate(self.tracks, start=10):
            messages = tk.Text(self.tracks_frame, height=1)
            messages.grid(row=row, column=0, sticky=tk.W, **self.padding)
            messages.insert(tk.END, getattr(track.track, 'name', 'Unknown'))
            for_sequencer['tracks'].append(track.track)
            for_sequencer['channels'].append(i)
            row += 1

        self.sequencer = Sequencer()
        self.sequencer.play_Tracks(**for_sequencer)

        row += 1
        column = 0
        button = tk.Button(self.tracks_frame, text='Add Track', command=self.add_track_popup)
        button.grid(row=row, column=column, sticky=tk.W, **self.padding)
        self.window.update()

    def add_track_popup(self):
        padding = {'padx': 2, 'pady': 2}
        self.top = tk.Toplevel(self.window)

        row = 0
        ttk.Label(self.top, text='File:').grid(row=row, column=0, sticky=tk.W, **padding)
        tk.Button(self.top, text="Load", command=self.load_track).\
            grid(row=row, column=1, sticky=tk.W, **padding)

        row += 1
        self.add_track_button = tk.Button(self.top, text="Add", command=self.add_track, state=tk.DISABLED)
        self.add_track_button.grid(row=row, column=0, sticky=tk.W, **padding)

        tk.Button(self.top, text="Cancel", command=lambda: self.top.destroy()).grid(row=row, column=1,
                                                                                    sticky=tk.W, **padding)

    def load_track(self):
        self.new_track = TrackGUI()
        self.new_track.load()
        self.add_track_button['state'] = tk.NORMAL

    def add_track(self):
        self.tracks.append(self.new_track)
        self.top.destroy()
        self.render_tracks_section()

    # Play ---------------------------------------------------------------------------------------------------------
    def play_note(self, event):
        instrument_name = self.instruments[event.char]
        instrument_number = mp.percussion_instruments[instrument_name]

        if self.synth is not None:
            self.synth.fs.noteon(self.percussion_channel, instrument_number, self.velocity)

            if self.is_recording and self.start_recording_time is not None:
                start_key = int((time.time() - self.start_recording_time) * 1000.0)  # in milliseconds
                note = PercussionNote(name=None, number=instrument_number, velocity=64, channel=self.percussion_channel)
                self.recording.setdefault(start_key, []).append(
                    {
                        'func': 'start_note',
                        'note': note,
                        'channel': self.percussion_channel,
                        'velocity': note.velocity
                    }
                )
        else:
            print('Note did not play because synth is not setup.')

    def do_nothing(self, event):
        pass

    def start_click_track(self):
        global click_track_done
        click_track_done = False

        if self.percussion_channel:
            self.click_thread = \
                ClickTrack(self.synth.fs, self.percussion_channel, self.bpm.get(), self.beats_per_bar.get())
            self.click_thread.start()
        else:
            print('Click track does not work because synth is not setup.')

    def stop_click_track(self):
        global click_track_done
        click_track_done = True

        try:
            del self.click_thread
        except:
            pass

    def start_stop_recording(self):
        global player_track_done

        if self.is_recording:
            self.is_recording = False
            self.start_stop_recording_button['text'] = 'Start'

            if self.play_click_track.get():
                self.stop_click_track()
            self.start_recording_time = None
            player_track_done = True
        else:
            self.is_recording = True
            self.start_stop_recording_button['text'] = 'Stop'

            # if self.play_click_track.get():
            #     self.start_click_track()

            # self.sequencer.play_score(self.synth)
            player = Play(self.synth, self.sequencer)
            player_track_done = False
            player.start()

            self.start_recording_time = time.time()
            print('recording started')

    def rewind(self):
        pass

    def play(self):
        from mingus.containers.midi_percussion import MidiPercussion
        global player_track_done

        snippet = RawSnippet(self.recording)
        track = Track(instrument=MidiPercussion(), snippets=[snippet])
        sequencer = Sequencer()  # TODO: prob want to add to existing sequencer
        sequencer.play_Track(track, channel=self.percussion_channel)
        player_track_done = False
        player = Play(self.synth, sequencer)
        player.start()

    def clear(self):
        self.recording = {}

    def quit(self):
        global click_track_done
        global player_track_done

        click_track_done = True
        player_track_done = True

        self.window.withdraw()
        self.window.destroy()

    def save(self):
        files = [
            ('All Files', '*.*'),
            ('Drum Tracks', '*.json')
        ]
        file = asksaveasfile(filetypes=files, defaultextension=files)
        if file:
            output = {
                'version': '1',
                'bpm': self.bpm.get(),
                'beats_per_bar': self.beats_per_bar.get(),
                'events': self.recording
            }
            mingus_json.dump(output, file)


if __name__ == '__main__':
    KeyboardDrumSet(setup_synth=True)
