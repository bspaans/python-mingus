"""
A simple demonstration of using percussion with fluidsynth.

This code was developed using the Musescore default sound font. We are not sure how it will work for other
sound-fonts.
"""
from time import sleep

import midi_percussion as mp
import pyfluidsynth
from mingus.midi.get_soundfont_path import get_soundfont_path

soundfont_path = get_soundfont_path()

synth = pyfluidsynth.Synth()
sfid = synth.sfload(soundfont_path)
synth.start()

# Percussion --------------------------------------------
percussion_channel = 1    # can be any channel between 1-128
bank = 128  # Must be 128 (at least for the Musescore default sound font)
preset = 1  # seem like it can be any integer
synth.program_select(percussion_channel, sfid, bank, preset)  # percussion

# Default non-percussion (i.e. piano)
bank = 0  # not percussion
instrument = 1
synth.program_select(percussion_channel + 1, sfid, bank, instrument)

velocity = 100
# Percussion does not use a noteoff
print('Starting')
for _ in range(3):
    synth.noteon(percussion_channel, 81, velocity)
    sleep(0.5)
    synth.noteon(percussion_channel + 1, 45, velocity)
    sleep(0.25)

# Do a hand clap using the midi percussion dict to make it more readable.
synth.noteon(percussion_channel, mp.percussion_instruments['Hand Clap'], velocity)
sleep(0.5)
print('done')
