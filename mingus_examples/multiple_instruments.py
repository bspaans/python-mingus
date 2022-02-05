"""
This module demonstrates two tracks, each playing a different instrument.
"""

import os

from mingus.containers import Bar, Track
from mingus.containers import MidiInstrument
from mingus.midi import fluidsynth

sound_font = os.getenv('MINGUS_SOUNDFONT')
assert sound_font, 'Please put the path to a soundfont file in the environment variable: MINGUS_SOUNDFONT'

fluidsynth.init(sound_font)

# Some whole notes
a_bar = Bar()
a_bar.place_notes('A-4', 1)

c_bar = Bar()
c_bar.place_notes('C-5', 1)

f_bar = Bar()
f_bar.place_notes('G-5', 1)

rest_bar = Bar()
rest_bar.place_rest(1)

t1 = Track(MidiInstrument("Rock Organ"))
t1.add_bar(a_bar)   # by itself
t1.add_bar(rest_bar)
t1.add_bar(a_bar)    # with track 2
t1.add_bar(rest_bar)
t1.add_bar(rest_bar)

t2 = Track(MidiInstrument("Choir Aahs"))
t2.add_bar(rest_bar)
t2.add_bar(rest_bar)
t2.add_bar(c_bar)  # with track 1
t2.add_bar(rest_bar)
t2.add_bar(f_bar)  # by itself

fluidsynth.play_Tracks([t1, t2], [1, 2])
