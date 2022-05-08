from mingus.containers import Bar, Track
from mingus.containers import MidiInstrument
from mingus.midi.fluid_synth2 import FluidSynthPlayer
from mingus.midi.get_soundfont_path import get_soundfont_path


soundfont_path = get_soundfont_path()

fluidsynth = FluidSynthPlayer(soundfont_path, gain=1.0)

# Some whole notes
c_bar = Bar()
c_bar.place_notes('C-4', 1)


t1 = Track(MidiInstrument("Acoustic Grand Piano",))
t1.add_bar(c_bar)


fluidsynth.play_tracks([t1], [1])
