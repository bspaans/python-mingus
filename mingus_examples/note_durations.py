"""
This module demonstrates note durations and rests
"""
from mingus.containers import Bar, Track, PercussionNote
from mingus.containers import MidiInstrument
from mingus.midi.fluid_synth2 import FluidSynthPlayer
from mingus.containers.midi_percussion import MidiPercussion
from mingus.midi.get_soundfont_path import get_soundfont_path


soundfont_path = get_soundfont_path()

fluidsynth = FluidSynthPlayer(soundfont_path, driver='coreaudio', gain=1.0)

# Some half notes
a_bar = Bar()
a_bar.place_notes('A-4', 2)
a_bar + 'A-4'

# Eight 8th notes
b_bar = Bar()
for _ in range(8):
    r = b_bar.place_notes('A-4', 8)

# 3 eighth notes tied together, quarter note rest, then 3 eighth notes tied together (off the beat)
c_bar = Bar()
c_bar.place_notes('B-4', 8.0 / 3.0)
c_bar.place_rest(4)
c_bar.place_notes('B-4', 8.0 / 3.0)

# Two whole notes tied together
d_bar = Bar()
d_bar.place_notes('A-4', 1.0 / 2.0)

rest_bar = Bar()
rest_bar.place_rest(1)

t1 = Track(MidiInstrument("Acoustic Grand Piano"))
t1.add_bar(a_bar)
t1.add_bar(b_bar)
t1.add_bar(c_bar)
t1.add_bar(d_bar)


# Add beat
t3 = Track(MidiPercussion())
drum_bar = Bar()
note = PercussionNote('High Tom', velocity=127)
note2 = PercussionNote('High Tom', velocity=62)
drum_bar.place_notes([note], 4)
drum_bar.place_notes([note2], 4)
drum_bar.place_notes([note2], 4)
drum_bar.place_notes([note2], 4)

for _ in range(5):
    t3.add_bar(drum_bar)

fluidsynth.play_tracks([t1, t3], [1, 3])
