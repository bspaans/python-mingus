"""
This module demonstrates two tracks, each playing a different instrument along with a percussion track.
"""

import os

from mingus.containers import Bar, Track, Note, PercussionNote
from mingus.containers import MidiInstrument
from mingus.midi.fluid_synth2 import FluidSynthPlayer
from mingus.containers.midi_percussion import MidiPercussion

sound_font = os.getenv('MINGUS_SOUNDFONT')
assert sound_font, 'Please put the path to a soundfont file in the environment variable: MINGUS_SOUNDFONT'

fluidsynth = FluidSynthPlayer(sound_font, driver='coreaudio', gain=1.0)

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

t3 = Track(MidiPercussion())
drum_bar = Bar()
note = PercussionNote('High Tom', velocity=127)
note2 = PercussionNote('High Tom', velocity=62)
drum_bar.place_notes([note], 4)
drum_bar.place_notes([note2], 4)
drum_bar.place_notes([note2], 4)
drum_bar.place_notes([note2], 4)

t3.add_bar(drum_bar)
t3.add_bar(drum_bar)
t3.add_bar(drum_bar)
t3.add_bar(drum_bar)
t3.add_bar(drum_bar)

fluidsynth.play_tracks([t1, t2, t3], [1, 2, 3])
