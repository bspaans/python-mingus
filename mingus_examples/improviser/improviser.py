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

# If True every second iteration will be played 
# in double time, starting on the first
double_time = False


# Orchestrates every second iteration with an additional instrument
# If False, orchestrates every iteration
orchestrate_second = True

swing = True
bar_length = 1.5

chord_channel = 1
chord_channel2 = 7
chord_channel3 = 3
bass_channel = 3
solo_channel = 11

random_solo_channel = True

if not fluidsynth.init_fluidsynth():
	print "Couldn't connect to FluidSynth server at port 9800."
	sys.exit(1)

chords = progressions.to_chords(progression, key)
loop = 1
while 1:
	i = 0 

	if random_solo_channel:
		solo_channel = choice(range(1,8) + [11])

	for chord in chords:
		c = NoteContainer(chords[i])
		l = Note(c[0].name)
		n = Note('C')
		l.octave_down()

		print ch.determine(chords[i])[0]


		# Play chord and lowered first note
		fluidsynth.play_NoteContainer(c, randrange(50,75), chord_channel)
		if orchestrate_second:
			if loop % 2 == 0:
				fluidsynth.play_NoteContainer(c, randrange(50,75), chord_channel2)
		else:
			fluidsynth.play_NoteContainer(c, randrange(50,75), chord_channel2)

		fluidsynth.play_Note(l, randrange(50,75), bass_channel)

		# Create random solo over chord
		if double_time:
			beats = [ random() > 0.5 for x in range((loop % 2 + 1) * 8)]
		else:
			beats = [ random() > 0.5 for x in range(8)]
		t = 0
		for beat in beats:
			# Play random note
			if beat:
				fluidsynth.stop_Note(n)
				if t % 2 == 0:
					n = Note(choice(c).name)
				else:
					if random() > 0.5:
						n = Note(intervals.second(choice(c).name, key))
					else:
						n = Note(intervals.seventh(choice(c).name, key))
				fluidsynth.play_Note(n, randrange(80, 110), solo_channel)
				print n

			# Repeat chord on half of the bar
			if swing and random() > 0.86:
				fluidsynth.play_NoteContainer(c, randrange(50, 75), chord_channel3)
			elif t % (len(beats) / 2) == 0 and t != 0:
				fluidsynth.play_NoteContainer(c, randrange(50, 75), chord_channel3)


			# Drums
			if loop > 0:
				if t % (len(beats) / 2) == 0 and t != 0:
					fluidsynth.play_Note(Note("E", 2), 100, 9)
				else:
					if random() > 0.8 or t == 0:
						fluidsynth.play_Note(Note("C", 2), 100, 9)

				if swing:
					if random() > 0.85:
						fluidsynth.play_Note(Note("A#", 2), 100, 9)
					elif random() > 0.5:
						fluidsynth.play_Note(Note("G#", 2), 100, 9)
					if random() > 0.95:
						fluidsynth.play_Note(Note("E", 2), 100, 9)
				elif t % 2 == 0: 
					fluidsynth.play_Note(Note("A#", 2), 100, 9)
				else:
					if random() > 0.9:
						fluidsynth.play_Note(Note("E", 2), 100, 9)
	
			if swing:
				if t % 2 == 0:
					time.sleep( (bar_length / (len(beats) * 3)) * 4)
				else:
					time.sleep( (bar_length / (len(beats) * 3)) * 2)
			else:
				time.sleep( bar_length / len(beats))
			t += 1

		fluidsynth.stop_NoteContainer(c, chord_channel)
		fluidsynth.stop_NoteContainer(c, chord_channel2)
		fluidsynth.stop_NoteContainer(c, chord_channel3)
		fluidsynth.stop_Note(l, bass_channel)
		fluidsynth.stop_Note(n, solo_channel)
		i += 1
	print "-" * 20
	loop += 1
