#!/usr/bin/env python
"""

*** Description ***

	Converts a progression to chords and plays them using fluidsynth.

	Make sure you have a fluidsynth server listening at port 9800
	for this example to work.


"""

from mingus.core import progressions
from mingus.core import chords as ch
from mingus.containers import NoteContainer
from mingus.extra import fluidsynth
import time, sys


progression = ["I", "vi", "ii", "iii7",
	       "I7", "viidom7", "iii7", "V7"]

chords = progressions.to_chords(progression)

if not fluidsynth.init_fluidsynth():
	print "Couldn't connect to FluidSynth server at port 9800."
	sys.exit(1)

while 1:
	i = 0 
	for chord in chords:
		c = NoteContainer(chords[i])
		print ch.determine(chords[i])[0]
		fluidsynth.play_NoteContainer(c)
		time.sleep(1.0)
		fluidsynth.play_Note(c[-1])
		time.sleep(1.0)
		fluidsynth.stop_NoteContainer(c)
		i += 1
	print "-" * 20
