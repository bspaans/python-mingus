"""
This module demonstrates two tracks, each playing a different instrument along with a percussion track.
"""
from mingus.containers import Bar, Track, PercussionNote
from mingus.containers import MidiInstrument
from mingus.midi.fluid_synth2 import FluidSynthPlayer
from mingus.containers.midi_percussion import MidiPercussion
from mingus.midi.get_soundfont_path import get_soundfont_path


soundfont_path = get_soundfont_path()

fluidsynth = FluidSynthPlayer(soundfont_path, gain=1.0)

# Some half notes
a_bar = Bar()
a_bar.place_notes('A-4', 2)  # play two successive notes and an instrument without decay to see if we hear 2 notes
a_bar + 'A-4'

# Some whole notes
c_bar = Bar()
c_bar.place_notes('C-5', 1)

f_bar = Bar()
f_bar.place_notes('G-5', 1)

rest_bar = Bar()
rest_bar.place_rest(1)

t1 = Track(MidiInstrument("Rock Organ"))  # an instrument without decay
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
# fluidsynth.play_tracks([t1], [1])
