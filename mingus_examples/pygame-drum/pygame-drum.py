#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

*** Description ***

    A pygame drum computer with recording and playback functionality.

    The drum computer is completely controlled by the keyboard, no MIDI
    hardware is required. You only have to specify an sf2 file.


*** Keys ***

    r    Enter record mode
    p    Exit record mode and play
    Escape    Quit


    On the keypad:
    0    Snare
    1    Base
    2    Low tom
    3    Middle tom
    4    Crash
    5    Hihat closed
    6    Hihat opened
    9    Ride
    Enter    High tom


"""

import pygame
from pygame.locals import *
from mingus.containers import *
from mingus.midi import fluidsynth
from os import sys
SF2 = 'soundfont.sf2'

PAD_PLACEMENT = [  # high, mid, low, snare bass, crash, ride, open, close
    (190, 20),
    (330, 20),
    (470, 20),
    (330, 160),
    (190, 300),
    (20, 20),
    (470, 160),
    (20, 160),
    (20, 300),
    ]
FADEOUT = 0.125  # coloration fadout time (1 tick = 0.001)


def load_img(name):
    """Load image and return an image object"""

    fullname = name
    try:
        image = pygame.image.load(fullname)
        if image.get_alpha() is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except pygame.error, message:
        print "Error: couldn't load image: ", fullname
        raise SystemExit, message
    return (image, image.get_rect())


if not fluidsynth.init(SF2):
    print "Couldn't load soundfont", SF2
    sys.exit(1)

pygame.init()
screen = pygame.display.set_mode((610, 500))
(pad, pad_rect) = load_img('pad.png')
hit = pygame.Surface(pad_rect.size)  # Used to display which pad was hit

track = pygame.Surface((610, 45))
track.fill((0, 0, 0))
pygame.draw.rect(track, (255, 0, 0), track.get_rect(), 1)
for y in range(1, 9):
    pygame.draw.line(track, (255, 0, 0), (0, y * 5), (610, y * 5), 1)
pygame.display.set_caption('mingus drum')


def play_note(note):
    """play_note determines which pad was 'hit' and send the
    play request to fluidsynth"""

    index = None
    if note == Note('B', 2):
        index = 0
    elif note == Note('A', 2):
        index = 1
    elif note == Note('G', 2):
        index = 2
    elif note == Note('E', 2):
        index = 3
    elif note == Note('C', 2):
        index = 4
    elif note == Note('A', 3):
        index = 5
    elif note == Note('B', 3):
        index = 6
    elif note == Note('A#', 2):
        index = 7
    elif note == Note('G#', 2):
        index = 8
    if index != None and status == 'record':
        playing.append([index, tick])
        recorded.append([index, tick, note])
        recorded_buffer.append([index, tick])
    fluidsynth.play_Note(note, 9, 100)


tick = 0.0
quit = False

# The left and right sides of the track representation. Used as a window onto
# the recording

low_barrier = 0.0
high_barrier = 0.50
playing = []  # Notes playing right now
recorded = []  # Recorded notes. A list of all the notes entered.
recorded_buffer = []  # Recorded notes that are in the display window (ie. their
                      # tick is between low and high barrier)
played = 0  # Used to keep track of the place in the recording, when status is
            # 'play'
buffered = 0  # Used to keep track of the buffer, when status is 'play'
need_buffer = True  # This is only False when status is 'play' and there are no
                    # more notes to buffer

status = 'stopped'
while not quit:
    screen.fill((0, 0, 0))

    # Blit drum pads

    for (x, y) in PAD_PLACEMENT:
        screen.blit(pad, (x, y))

    # Check each playing note

    for note in playing:
        diff = max(0, tick - note[1])

        # If the note should be removed, remove it. Otherwise blit a fading
        # 'hit' surface.

        if diff > FADEOUT:
            playing.remove(note)
        else:
            hit.fill((0, ((FADEOUT - diff) / FADEOUT) * 155, 0))
            screen.blit(hit, PAD_PLACEMENT[note[0]], None, BLEND_SUB)

    # Check if the view window onto the track has to be changed

    if tick > high_barrier:
        high_barrier += high_barrier - low_barrier
        low_barrier = tick
    track_c = track.copy()

    # Draw a line representing the current place on the track surface

    current = tick - low_barrier
    x = (current / (high_barrier - low_barrier)) * 610
    pygame.draw.line(track_c, (0, 255, 0), (x, 0), (x, 50), 2)

    # Blit all the notes in recorded_buffer onto the track surface as little
    # squeares or remove the note if it's outside the viewing window

    for r in recorded_buffer:
        if r[1] < low_barrier:
            recorded_buffer.remove(r)
        else:
            y = r[0] * 5
            x = ((r[1] - low_barrier) / (high_barrier - low_barrier)) * 610
            pygame.draw.rect(track_c, (255, 0, 0), (x, y, 5, 5))

    # Blit the track

    screen.blit(track_c, (0, 440))

    for event in pygame.event.get():
        if event.type == QUIT:
            quit = True
        if event.type == KEYDOWN:
            if event.key == K_KP0:
                play_note(Note('E', 2))  # snare
            elif event.key == K_KP1 or event.key == K_SPACE:
                play_note(Note('C', 2))  # bass
            elif event.key == K_KP_ENTER:
                play_note(Note('B', 2))  # high tom
            elif event.key == K_KP2:
                play_note(Note('A', 2))  # middle tom
            elif event.key == K_KP3:
                play_note(Note('G', 2))  # low tom
            elif event.key == K_KP4:
                play_note(Note('A', 3))  # crash
            elif event.key == K_KP5:
                play_note(Note('G#', 2))  # hihat closed
            elif event.key == K_KP6:
                play_note(Note('A#', 2))  # hihat opened
            elif event.key == K_KP9:
                play_note(Note('B', 3))  # ride
            if status == 'record':
                if event.key == K_p:

                    # Starts playing mode, which a lot of variables have to be
                    # adjusted for

                    status = 'play'
                    tick = 0.0
                    low_barrier = 0.0
                    high_barrier = 0.50
                    played = 0

                    # A new recorded buffer has to be loaded

                    recorded_buffer = []
                    buffered = 0
                    need_buffer = True
                    for r in recorded:
                        if r[1] <= 0.50:
                            recorded_buffer.append([r[0], r[1]])
                            buffered += 1
                        else:
                            break
            elif status == 'stopped':
                if event.key == K_r:
                    status = 'record'
            if event.key == K_ESCAPE:
                quit = True

    if status == 'play':
        try:
            while recorded[played][1] <= tick:
                playing.append([recorded[played][0], recorded[played][1]])
                fluidsynth.play_Note(recorded[played][2], 9, 100)
                played += 1
                if played == len(recorded) - 1:
                    status = 'stopped'
        except:
            pass

        # Update the recorded_buffer

        try:
            while need_buffer and recorded[buffered][1] <= high_barrier:
                recorded_buffer.append([recorded[buffered][0],
                                       recorded[buffered][1]])
                buffered += 1
                if buffered >= len(recorded) - 1:
                    buffered = len(recorded) - 1
                    need_buffer = False
        except:
            pass
    pygame.display.update()
    if status != 'stopped':
        tick += 0.001
pygame.quit()
