import copy
from pathlib import Path

from mingus.containers import Bar, Track, PercussionNote, Note
from mingus.containers.track import ControlChangeEvent, MidiControl
from mingus.containers import MidiInstrument
from mingus.containers.midi_snippet import MidiPercussionSnippet
from mingus.midi.fluid_synth2 import FluidSynthPlayer
from mingus.containers.midi_percussion import MidiPercussion
from mingus.midi.get_soundfont_path import get_soundfont_path
from mingus.midi.sequencer2 import Sequencer, calculate_bar_start_time, calculate_bar_end_time
import mingus.tools.mingus_json as  mingus_json


soundfont_path = get_soundfont_path()


def melody(n_times):
    rest_bar = Bar()
    rest_bar.place_rest(1)

    i_bar = Bar()
    i_bar.place_notes(Note('C-5', velocity=60), 16.0 / 2.5)
    i_bar.place_notes(Note('C-5', velocity=50), 16.0 / 1.5)
    i_bar.place_rest(8.0 / 5.0)

    i_bar_2 = Bar()
    i_bar_2.place_rest(8.0 / 5.0)
    i_bar_2.place_notes(Note('C-5'), 8.0 / 3.0)

    turn_around = Bar()
    turn_around.place_notes(Note('C-5', velocity=60), 4)
    turn_around.place_notes(Note('C-5', velocity=80), 4)
    turn_around.place_rest(4.0 / 2.0)

    iv_bar = copy.deepcopy(i_bar)
    iv_bar.transpose("4")

    v_bar = copy.deepcopy(i_bar)
    v_bar.transpose("5")
    
    track = Track(MidiInstrument("Trumpet"), name="Trumpet")
    track.add_bar(i_bar, n_times=1)
    track.add_bar(rest_bar, 2)
    track.add_bar(i_bar_2)

    track.add_bar(iv_bar, n_times=1)
    track.add_bar(rest_bar)
    track.add_bar(i_bar, n_times=1)
    track.add_bar(rest_bar)

    track.add_bar(v_bar)
    track.add_bar(iv_bar)
    track.add_bar(rest_bar)
    track.add_bar(turn_around)

    event = ControlChangeEvent(beat=0, control=MidiControl.CHORUS, value=80)
    track.add_event(event)

    return track
    

def bass(n_times):
    # Make the bars
    i_bar = Bar()
    i_bar.place_notes(Note('C-3'), 4)
    i_bar.place_notes(Note('C-2'), 4)
    i_bar.place_notes(Note('Eb-2'), 4)
    i_bar.place_notes(Note('E-2'), 4)

    turn_around = Bar()
    turn_around.place_notes(Note('Eb-2'), 4)
    turn_around.place_notes(Note('E-2'), 4)
    turn_around.place_notes(Note('G-3'), 2)

    iv_bar = copy.deepcopy(i_bar)
    iv_bar.transpose("4")

    v_bar = copy.deepcopy(i_bar)
    v_bar.transpose("5")

    # Make the track
    bass_track = Track(MidiInstrument("Acoustic Bass"), name='Bass')

    # Make section
    bass_track.add_bar(i_bar, n_times=4)

    bass_track.add_bar(iv_bar, n_times=2)
    bass_track.add_bar(i_bar, n_times=2)

    bass_track.add_bar(v_bar)
    bass_track.add_bar(iv_bar)
    bass_track.add_bar(i_bar)
    bass_track.add_bar(turn_around)

    bass_track.repeat(n_times - 1)

    return bass_track


def percussion(n_times):
    track = Track(MidiPercussion(), name='Percussion')
    drum_bar = Bar()
    note = PercussionNote('Ride Cymbal 1', velocity=62)
    note2 = PercussionNote('Ride Cymbal 1', velocity=32)
    drum_bar.place_notes([note2], 4)
    drum_bar.place_notes([note], 4)
    drum_bar.place_notes([note2], 4)
    drum_bar.place_notes([note], 4)

    for i in range(3):
        for j in range(4):
            track.add_bar(drum_bar)

    track.repeat(n_times - 1)
    return track


def snare(n_times):
    snare_track = Track(MidiPercussion(), name='Snare')
    snare = PercussionNote('Acoustic Snare', velocity=62)
    snare2 = PercussionNote('Acoustic Snare', velocity=32)
    rest_bar = Bar()
    rest_bar.place_rest(1)

    drum_turn_around_bar = Bar()
    drum_turn_around_bar.place_rest(16.0 / 11.0)
    drum_turn_around_bar.place_notes([snare2], 16)
    drum_turn_around_bar.place_notes([snare], 16.0 / 3.0)
    drum_turn_around_bar.place_notes([snare2], 16)

    for i in range(3):
        for j in range(3):
            snare_track.add_bar(rest_bar)
        snare_track.add_bar(drum_turn_around_bar)

    snare_track.repeat(n_times - 1)

    return snare_track


def play(voices, n_times, **kwargs):
    fluidsynth = FluidSynthPlayer(soundfont_path, gain=1.0)
    fluidsynth.play_tracks([voice(n_times) for voice in voices], range(1, len(voices) + 1), **kwargs)


def save(path, voices, bpm=120):
    n_times = 1
    channels = range(1, len(voices) + 1)
    sequencer = Sequencer()
    sequencer.save_tracks(path, [voice(n_times) for voice in voices], channels, bpm=bpm)


def load(path):
    sequencer = Sequencer()
    sequencer.load_tracks(path)

    fluidsynth = FluidSynthPlayer(soundfont_path, gain=1.0)
    sequencer.play_score(fluidsynth)
    print('x')


def play_in_player(n_times):
    # noinspection PyListCreation
    voices = []
    voices.append(percussion)  # percusion is a track
    # voices.append(snare)
    voices.append(bass)  # a track
    voices.append(melody)
    tracks = [voice(n_times) for voice in voices]
    channels = list(range(1, len(voices) + 1))
    return tracks, channels


if __name__ == '__main__':
    # noinspection PyListCreation
    voices = []
    voices.append(percussion)  # percusion is a track
    # voices.append(snare)
    voices.append(bass)        # a track
    voices.append(melody)
    start_time = calculate_bar_start_time(120.0, 4, 9)
    end_time = calculate_bar_start_time(120.0, 4, 13)

    play(voices, n_times=1, start_time=start_time, end_time=end_time)
    # score_path = Path.home() / 'python_mingus' / 'scores' / 'blues.json'
    # save(score_path, voices)

    # Track manipulations
    # track = percussion(1)
    # track = bass(1)
    # track_path = Path.home() / 'python_mingus' / 'tracks' / 'test_bass.json'
    # with open(track_path, 'w') as fp:
    #     mingus_json.dump(track, fp)

    # with open(track_path, 'r') as fp:
    #     new_track = mingus_json.load(fp)
    #
    # fluidsynth = FluidSynthPlayer(soundfont_path, gain=1.0)
    # fluidsynth.play_tracks([track], [2])
    print('done')
