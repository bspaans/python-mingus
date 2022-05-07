from time import sleep

from mingus.midi.fluid_synth2 import FluidSynthPlayer
from mingus.midi.get_soundfont_path import get_soundfont_path
from mingus.containers.instrument import get_instrument_number
from mingus.containers import Bar, Track
from mingus.containers import MidiInstrument


def play_w_chorus():
    """Get single notes working"""
    soundfont_path = get_soundfont_path()

    synth = FluidSynthPlayer(soundfont_path, gain=1.0)

    bank = 0  # not percussion
    instrument = get_instrument_number("Trumpet")
    channel = 1
    synth.set_instrument(channel=channel, instr=instrument, bank=bank)

    velocity = 100
    note_dur = 2.0
    print('Starting')

    def play_note(chorus_level):
        if chorus_level:
            chorus = 93
            synth.control_change(channel=channel, control=chorus, value=chorus_level)

        synth.play_note(note=60, channel=channel, velocity=velocity)
        sleep(note_dur)
        synth.stop_note(note=60, channel=channel)
        sleep(0.1)

    play_note(0)
    play_note(64)
    play_note(127)


def play_with_chorus_2():
    soundfont_path = get_soundfont_path()

    fluidsynth = FluidSynthPlayer(soundfont_path, gain=1.0)

    # Some whole notes
    c_bar = Bar()
    c_bar.place_notes('C-4', 1)

    t1 = Track(MidiInstrument("Acoustic Grand Piano", ))
    t1.add_bar(c_bar)

    fluidsynth.play_tracks([t1], [1])


play_with_chorus_2()

print('done')
