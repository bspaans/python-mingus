#!/usr/bin/env python

import pygame
from pygame.locals import *
from mingus.core import notes, chords
from mingus.containers import *
from mingus.extra import fluidsynth
from os import sys

PAD_PLACEMENT = [(190, 20), (330, 20), (470, 20), (330, 160), # high, mid, low, snare
		 (190, 300), (20, 20), (470, 160), (20, 160), (20, 300)] # bass, crash, ride, open, close
FADEOUT = 0.125

def load_img(name):
	"""Load image and return an image object"""

	fullname = name
	try:
		image = pygame.image.load(fullname)
		if image.get_alpha() is None:
			image= image.convert()
		else:
			image = image.convert_alpha()
	except pygame.error, message:
		print "Error: couldn't load image: ", fullname
		raise SystemExit, message
	return image, image.get_rect()

if not fluidsynth.init_fluidsynth():
	print "Couldn't connect to the fluidsynth server. Are you sure it is running?"
	sys.exit(1)


pygame.init()
screen = pygame.display.set_mode((610,500))
pad, pad_rect = load_img("pad.png")
hit = pygame.Surface(pad_rect.size)


# Draw track
track=pygame.Surface((610, 45))
track.fill((0,0,0))
pygame.draw.rect(track, (255,0,0), track.get_rect(), 1)
for y in range(1, 9):
	pygame.draw.line(track, (255,0,0), (0, y * 5), (610, y * 5), 1)


pygame.display.set_caption("mingus drum")


def play_note(note):

	index = None
	if note == Note("B", 2):
		index = 0
	elif note == Note("A", 2):
		index = 1
	elif note == Note("G", 2):
		index = 2
	elif note == Note("E", 2):
		index = 3
	elif note == Note("C",2):
		index = 4
	elif note == Note("A", 3):
		index = 5
	elif note == Note("B", 3):
		index = 6
	elif note == Note("A#", 2):
		index = 7
	elif note == Note("G#", 2):
		index = 8

	if index != None:
		playing.append([index, tick])
		recorded.append([index, tick, note])
		recorded_buffer.append([index, tick])
	fluidsynth.play_Note(note, 100, 9)


tick = 0.0
quit = False
playing = []
recorded = []
recorded_buffer=[]
played=0
buffered= 0
need_buffer= True
low_barrier= 0.0
high_barrier= 0.50

status = "stopped"

while not quit:

	screen.fill((0,0,0))

	# Blit drum pads
	for x, y in PAD_PLACEMENT:
		screen.blit(pad, (x, y))

	for note in playing:
		diff = max(0, tick - note[1])
		if diff > FADEOUT:
			playing.remove(note)
		else:
			hit.fill((0, (FADEOUT - diff) / FADEOUT * 155, 0 ))
			screen.blit(hit, PAD_PLACEMENT[note[0]], None,BLEND_SUB)

	# Blit track info
	track_c = track.copy()
	if tick > high_barrier:
		high_barrier += (high_barrier - low_barrier) 
		low_barrier = tick

	current = tick - low_barrier
	x = (current / (high_barrier - low_barrier)) * 610
	pygame.draw.line(track_c, (0, 255,0), (x, 0), (x, 50), 2)

	# Recorded bits
	for r in recorded_buffer:
		if r[1] < low_barrier:
			recorded_buffer.remove(r)
		else:
			y = r[0] * 5
			x = ((r[1] - low_barrier) / (high_barrier - low_barrier)) * 610
			pygame.draw.rect(track_c, (255, 0, 0), (x, y, 5, 5))
		

	screen.blit(track_c, (0, 440))
	

	for event in pygame.event.get():
		if event.type == QUIT:
			quit = True
		if event.type == KEYDOWN:
			if status == "record":
				if event.key == K_KP0:
					play_note(Note("E", 2)) # snare
				elif event.key == K_KP1:		
					play_note(Note("C", 2))	# bass
				elif event.key == K_KP_ENTER:
					play_note(Note("B", 2)) # high tom
				elif event.key == K_KP2:		
					play_note(Note("A", 2))	# middle tom
				elif event.key == K_KP3:		
					play_note(Note("G", 2))	# low tom
				elif event.key == K_KP4:
					play_note(Note("A", 3)) # crash
				elif event.key == K_KP5:
					play_note(Note("G#", 2)) # hihat closed
				elif event.key == K_KP6:
					play_note(Note("A#", 2)) # hihat opened
				elif event.key == K_KP9:
					play_note(Note("B", 3)) # ride
				elif event.key == K_p:
					status= "play"
					tick = 0.0
					low_barrier= 0.0
					high_barrier = 0.5
					played = 0
					recorded_buffer = []
					buffered = 0
					need_buffer = True
					for r in recorded:
						if r[1] <= 0.5:
							recorded_buffer.append([r[0], r[1]])
							buffered += 1
						else:
							break
			elif status == "play" or status == "stopped":
				if event.key == K_r:
					status = "record"

			if event.key == K_ESCAPE:
				quit = True


	# move pads around
	i = 0
	for x,y in PAD_PLACEMENT:
		PAD_PLACEMENT[i] = (x, y)
		i += 1

	# play recorded notes
	if status == "play":
		try: 
			while recorded[played][1] <= tick:
				playing.append([recorded[played][0],recorded[played][1]])
				fluidsynth.play_Note(recorded[played][2], 100, 9)
				played += 1
				if played == len(recorded) - 1:
					status = "stopped"
		except:
			pass
		try:
			while need_buffer and recorded[buffered][1] <= high_barrier:
				recorded_buffer.append([recorded[buffered][0], recorded[buffered][1]])
				buffered += 1
				if buffered >= len(recorded) - 1:
					buffered = len(recorded) - 1
					need_buffer= False
		except:
			pass


	pygame.display.update()

	if status != "stopped":
		tick += 0.001


pygame.quit()
