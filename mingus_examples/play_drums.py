"""
A simple demonstration of using percussion with fluidsynth.

This code was developed using the Musescore default sound font. We are not sure how it will work for other
sound-fonts.
"""

import os
from time import sleep

from midi_percussion import midi_percussion as mp
import pyfluidsynth

sound_font = os.getenv('MINGUS_SOUNDFONT')
assert sound_font, 'Please put the path to a soundfont file in the environment variable: MINGUS_SOUNDFONT'

synth = pyfluidsynth.Synth()
sfid = synth.sfload(sound_font)
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
synth.noteon(percussion_channel, mp['Hand Clap'], velocity)
sleep(0.5)
print('done')
