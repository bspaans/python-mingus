#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

*** Description ***

    Converts a progression to chords, orchestrates them and plays
    them using fluidsynth.

    Make sure to set SF2 to a valid soundfont file.

    Based on play_progression.py
"""

from mingus.core import progressions, intervals
from mingus.core import chords as ch
from mingus.containers import NoteContainer, Note
from mingus.midi import fluidsynth
import time
import sys
from random import random, choice, randrange
SF2 = 'soundfont.sf2'
progression = ['I', 'bVdim7']

# progression = ["I", "vi", "ii", "iii7",               "I7", "viidom7", "iii7",
# "V7"]

key = 'C'

# If True every second iteration will be played in double time, starting on the
# first

double_time = True

orchestrate_second = True
swing = True
play_solo = True
play_drums = True
play_bass = True
play_chords = True
bar_length = 1.75
song_end = 28

# Control beginning of solos and chords

solo_start = 8
solo_end = 20
chord_start = 16
chord_end = 24

# Channels

chord_channel = 1
chord_channel2 = 7
chord_channel3 = 3
bass_channel = 4
solo_channel = 13
random_solo_channel = False
if not fluidsynth.init(SF2):
    print("Couldn't load soundfont", SF2)
    sys.exit(1)
chords = progressions.to_chords(progression, key)
loop = 1
while loop < song_end:
    i = 0
    if random_solo_channel:
        solo_channel = choice(list(range(5, 8)) + [11])
    for chord in chords:
        c = NoteContainer(chords[i])
        l = Note(c[0].name)
        n = Note('C')
        l.octave_down()
        l.octave_down()
        print(ch.determine(chords[i])[0])

        if not swing and play_chords and loop > chord_start and loop\
             < chord_end:
            fluidsynth.play_NoteContainer(c, chord_channel, randrange(50, 75))
        if play_chords and loop > chord_start and loop < chord_end:
            if orchestrate_second:
                if loop % 2 == 0:
                    fluidsynth.play_NoteContainer(c, chord_channel2,
                            randrange(50, 75))
            else:
                fluidsynth.play_NoteContainer(c, chord_channel2, randrange(50,
                        75))

        if double_time:
            beats = [random() > 0.5 for x in range((loop % 2 + 1) * 8)]
        else:
            beats = [random() > 0.5 for x in range(8)]
        t = 0
        for beat in beats:

            # Play random note

            if beat and play_solo and loop > solo_start and loop < solo_end:
                fluidsynth.stop_Note(n)
                if t % 2 == 0:
                    n = Note(choice(c).name)
                elif random() > 0.5:
                    if random() < 0.46:
                        n = Note(intervals.second(choice(c).name, key))
                    elif random() < 0.46:
                        n = Note(intervals.seventh(choice(c).name, key))
                    else:
                        n = Note(choice(c).name)
                    if t > 0 and t < len(beats) - 1:
                        if beats[t - 1] and not beats[t + 1]:
                            n = Note(choice(c).name)
                fluidsynth.play_Note(n, solo_channel, randrange(80, 110))
                print(n)

            # Repeat chord on half of the bar

            if play_chords and t != 0 and loop > chord_start and loop\
                 < chord_end:
                if swing and random() > 0.95:
                    fluidsynth.play_NoteContainer(c, chord_channel3,
                            randrange(20, 75))
                elif t % (len(beats) / 2) == 0 and t != 0:
                    fluidsynth.play_NoteContainer(c, chord_channel3,
                            randrange(20, 75))

            # Play bass note

            if play_bass and t % 4 == 0 and t != 0:
                l = Note(choice(c).name)
                l.octave_down()
                l.octave_down()
                fluidsynth.play_Note(l, bass_channel, randrange(50, 75))
            elif play_bass and t == 0:
                fluidsynth.play_Note(l, bass_channel, randrange(50, 75))

            # Drums

            if play_drums and loop > 0:
                if t % (len(beats) / 2) == 0 and t != 0:
                    fluidsynth.play_Note(Note('E', 2), 9, randrange(50, 100))  # snare
                else:
                    if random() > 0.8 or t == 0:
                        fluidsynth.play_Note(Note('C', 2), 9, randrange(20,
                                100))  # bass
                if t == 0 and random() > 0.75:
                    fluidsynth.play_Note(Note('C#', 3), 9, randrange(60, 100))  # crash
                if swing:
                    if random() > 0.9:
                        fluidsynth.play_Note(Note('A#', 2), 9, randrange(50,
                                100))  # hihat open
                    elif random() > 0.6:
                        fluidsynth.play_Note(Note('G#', 2), 9, randrange(100,
                                120))  # hihat closed
                    if random() > 0.95:
                        fluidsynth.play_Note(Note('E', 2), 9, 100)  # snare
                elif t % 2 == 0:
                    fluidsynth.play_Note(Note('A#', 2), 9, 100)  # hihat open
                else:
                    if random() > 0.9:
                        fluidsynth.play_Note(Note('E', 2), 9, 100)  # snare
            if swing:
                if t % 2 == 0:
                    time.sleep((bar_length / (len(beats) * 3)) * 4)
                else:
                    time.sleep((bar_length / (len(beats) * 3)) * 2)
            else:
                time.sleep(bar_length / len(beats))
            t += 1
        fluidsynth.stop_NoteContainer(c, chord_channel)
        fluidsynth.stop_NoteContainer(c, chord_channel2)
        fluidsynth.stop_NoteContainer(c, chord_channel3)
        fluidsynth.stop_Note(l, bass_channel)
        fluidsynth.stop_Note(n, solo_channel)
        i += 1
    print('-' * 20)
    loop += 1
