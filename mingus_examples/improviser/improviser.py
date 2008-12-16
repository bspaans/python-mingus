#!/usr/bin/env python
"""

*** Description ***

	Converts a progression to chords, orchestrates them and plays 
	them using fluidsynth.

	Make sure you have a fluidsynth server listening at port 9800
	for this example to work.
	
	Based on play_progression.py

"""

from mingus.core import progressions, intervals
from mingus.core import chords as ch
from mingus.containers import NoteContainer, Note
from mingus.extra import fluidsynth
import time, sys
from random import random, choice, randrange


progression = ["I", "vi", "ii", "iii7",
	       "I7", "viidom7", "iii7", "V7"]
key = 'C'

chords = progressions.to_chords(progression, key)

if not fluidsynth.init_fluidsynth():
	print "Couldn't connect to FluidSynth server at port 9800."
	sys.exit(1)

while 1:
	i = 0 
	for chord in chords:
		c = NoteContainer(chords[i])
		l = Note(c[0].name)
		n = Note('C')
		l.octave_down()

		print ch.determine(chords[i])[0]


		# Play chord and lowered first note
		fluidsynth.play_NoteContainer(c, randrange(50,75), 1)
		fluidsynth.play_Note(l, randrange(50,75), 2)

		# Create random solo over chord
		beats = [ random() > 0.5 for x in range(8)]
		t = 0
		for beat in beats:
			if beat:
				fluidsynth.stop_Note(n)
				if t % 2 == 0:
					n = Note(choice(c).name)
				else:
					if random() > 0.5:
						n = Note(intervals.second(choice(c).name, key))
					else:
						n = Note(intervals.seventh(choice(c).name, key))
				fluidsynth.play_Note(n, randrange(80, 110), 11)
				print n
			if t == 5:
				fluidsynth.play_NoteContainer(c, randrange(50, 75), 7)

			time.sleep( 2.0 / len(beats))
			t += 1

		fluidsynth.stop_NoteContainer(c, 1)
		fluidsynth.stop_Note(l, 2)
		fluidsynth.stop_Note(n, 11)
		i += 1
	print "-" * 20
