import copy

from mingus.containers import Bar, Track, PercussionNote, Note
from mingus.containers import MidiInstrument
from mingus.midi.fluid_synth2 import FluidSynthPlayer
from mingus.containers.midi_percussion import MidiPercussion
from mingus.midi.get_soundfont_path import get_soundfont_path

soundfont_path = get_soundfont_path()

fluidsynth = FluidSynthPlayer(soundfont_path, gain=1.0)


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
    bass_track = Track(MidiInstrument("Acoustic Bass"))

    # Make section
    bass_track.add_bar(i_bar, n_times=4)

    bass_track.add_bar(iv_bar, n_times=2)
    bass_track.add_bar(i_bar, n_times=2)

    bass_track.add_bar(v_bar)
    bass_track.add_bar(iv_bar)
    bass_track.add_bar(i_bar)
    bass_track.add_bar(turn_around)

    if n_times > 1:
        bass_track.repeat(n_times - 1)

    return bass_track


def percussion(n_times):
    track = Track(MidiPercussion())
    drum_bar = Bar()
    note = PercussionNote('Ride Cymbal 1', velocity=127)
    note2 = PercussionNote('Ride Cymbal 1', velocity=62)
    drum_bar.place_notes([note2], 4)
    drum_bar.place_notes([note], 4)
    drum_bar.place_notes([note2], 4)
    drum_bar.place_notes([note], 4)

    for _ in range(12):
        track.add_bar(drum_bar)

    if n_times > 1:
        track.repeat(n_times - 1)

    return track


fluidsynth.play_tracks([bass(1), percussion(1)], [1, 2])
