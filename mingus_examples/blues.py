import copy
from pathlib import Path

from mingus.containers import Bar, Track, PercussionNote, Note
from mingus.containers import MidiInstrument
from mingus.containers.midi_snippet import MidiPercussionSnippet
from mingus.midi.fluid_synth2 import FluidSynthPlayer
from mingus.containers.midi_percussion import MidiPercussion
from mingus.midi.get_soundfont_path import get_soundfont_path
from mingus.midi.sequencer2 import Sequencer
import mingus.tools.mingus_json as  mingus_json


soundfont_path = get_soundfont_path()


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

    for _ in range(12):
        track.add_bar(drum_bar)

    # path = Path.home() / 'drum 1.mid'
    # snippet = MidiPercussionSnippet(path, start=0.0, length_in_seconds=4.0, n_replications=6)
    # track.add_midi_snippet(snippet)

    track.repeat(n_times - 1)

    return track


def play(voices, n_times):
    fluidsynth = FluidSynthPlayer(soundfont_path, gain=1.0)
    fluidsynth.play_tracks([voice(n_times) for voice in voices], range(1, len(voices) + 1))


def save(path, voices, bpm=120):
    n_times = 1
    channels = range(1, len(voices) + 1)
    sequencer = Sequencer()
    sequencer.save_tracks('saved_blues.json', [voice(n_times) for voice in voices], channels, bpm=bpm)


def load(path):
    sequencer = Sequencer()
    sequencer.load_tracks(path)

    fluidsynth = FluidSynthPlayer(soundfont_path, gain=1.0)
    sequencer.play_score(fluidsynth)
    print('x')


if __name__ == '__main__':
    # noinspection PyListCreation
    # voices = []
    # voices.append(percussion)  # percusion is a track
    # voices.append(bass)        # a track
    # play(voices, n_times=1)
    # path = 'saved_blues.json'
    # save(path, voices)
    # load(path)

    # Track manipulations
    # track = percussion(1)
    track = bass(1)
    track_path = Path.home() / 'python_mingus' / 'tracks' / 'test_bass.json'
    with open(track_path, 'w') as fp:
        mingus_json.dump(track, fp)

    # with open(track_path, 'r') as fp:
    #     new_track = mingus_json.load(fp)
    #
    # fluidsynth = FluidSynthPlayer(soundfont_path, gain=1.0)
    # fluidsynth.play_tracks([track], [2])
    print('x')
