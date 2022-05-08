from functools import partial
import os
import json
from pathlib import Path

import tkinter as tk
from tkinter import ttk

from mingus.containers import Bar, Track, PercussionNote
from mingus.midi.fluid_synth2 import FluidSynthPlayer
from mingus.containers.midi_percussion import MidiPercussion, percussion_instruments


class PercussionComposer:
    def __init__(self, setup_synth=True, instruments_path='percussion_composer.pkl'):
        """

        :param setup_synth: synth setup can take several seconds. Set this to False to delay setup until it is needed
        :type setup_synth: bool
        """
        self.instruments_path = Path(instruments_path)
        if setup_synth:
            self.setup_synth()
        else:
            self.synth = None
            self.sound_font = 'not loaded'

        padding = {
            'padx': 10,
            'pady': 10
        }

        self.root = tk.Tk()
        self.root.title("Percussion Composer")
        
        self.composer_frame = tk.Frame(self.root)
        self.composer_frame.grid(row=0, column=0)

        control_frame = tk.Frame(self.root, **padding)
        control_frame.grid(row=1, column=0)

        # Composer frame
        self.note_duration = 32

        if os.path.exists(self.instruments_path):
            self.instruments = self.from_json(path=instruments_path)
        else:
            self.instruments = [self.make_instrument()]

        self.composer_row = 0
        for instrument in self.instruments:
            self.add_instrument(row=self.composer_row, instrument=instrument)
            self.composer_row += 1

        # Controls
        tk.Button(control_frame, text="Add Instrument", command=self.add_instrument).pack(side='left')
        tk.Button(control_frame, text="Play", command=self.play).pack(side='left')
        tk.Button(control_frame, text="Save", command=self.to_json).pack(side='left')
        tk.Button(control_frame, text="Quit", command=self.quit).pack(side='left')

        self.root.mainloop()

    def setup_synth(self):
        self.soundfont_path = os.getenv('MINGUS_SOUNDFONT')
        assert self.soundfont_path, \
            'Please put the path to a soundfont file in the environment variable: MINGUS_SOUNDFONT'

        self.synth = FluidSynthPlayer(self.soundfont_path, gain=1.0)

    def do_something(self, row, col):
        pass

    def make_instrument(self, name=''):
        instrument = {
            'name': tk.StringVar(value=name),
            'beats': [tk.IntVar(0) for _ in range(self.note_duration)]
        }
        return instrument

    def add_instrument(self, row=None, instrument=None):
        row = row or self.composer_row

        if instrument is None:
            instrument = self.make_instrument()
            self.instruments.append(instrument)

        column = 0
        ttk.Combobox(
            self.composer_frame,
            textvariable=instrument['name'],
            values=list(percussion_instruments.keys()),
            state="READONLY"
        ).grid(row=row, column=column, sticky=tk.W)
        column += 1

        for beat in instrument['beats']:
            ttk.Checkbutton(
                self.composer_frame,
                variable=beat,
                onvalue=1,
                offvalue=0,
                command=partial(self.do_something, row, column - 1)
            ).grid(row=row, column=column, sticky=tk.W)
            column += 1
        self.composer_row = row

    def play(self):
        tracks = []
        for instrument in self.instruments:
            track = Track(MidiPercussion())
            bar = Bar()
            note = PercussionNote(instrument['name'].get(), velocity=62)
            for beat in instrument['beats']:
                if beat.get():
                    bar.place_notes([note], self.note_duration)
                else:
                    bar.place_rest(self.note_duration)
            track.add_bar(bar)
            tracks.append(track)

        self.synth.play_tracks(tracks, range(1, len(tracks) + 1))

    def to_json(self, path=None):
        path = path or self.instruments_path
        d = []
        for instrument in self.instruments:
            d.append(
                {
                    'name': instrument['name'].get(),
                    'beats': [beat.get() for beat in instrument['beats']]
                }
            )
        with open(path, 'w') as fp:
            json.dump(d, fp)

    @staticmethod
    def from_json(path):
        with open(path, 'r') as fp:
            data = json.load(fp)

        instruments = []
        for instrument_data in data:
            instrument = {
                'name': tk.StringVar(value=instrument_data['name']),
                'beats': [tk.IntVar(value=note) for note in instrument_data['beats']]
            }
            instruments.append(instrument)
        return instruments

    def quit(self):
        self.root.withdraw()
        self.root.destroy()


if __name__ == '__main__':
    PercussionComposer()
