from binascii import a2b_hex

class MidiFileOut:

	tracks = []
	time_division = "\x00\x48"

	def __init__(self):
		pass

	def get_midi_data(self):
		tracks = [ t.get_midi_data() for t in self.tracks ]
		return self.header() + "".join(tracks)

	def header(self):
		"""Returns a header for type 1 midi file"""
		tracks = a2b_hex("%04x" % len(self.tracks))
		return "MThd\x00\x00\x00\x06\x00\x01" + tracks + self.time_division

class MidiTrack:

	track_data = ''
	delta_time = '\x00'
	bpm = 120

	def __init__(self, start_bpm = 120):
		self.bpm = start_bpm
		self.track_data = self.set_tempo_event(120)


	def end_of_track(self):
		"""End of track meta event."""
		return "\x00\xff\x2f\x00"

	def play_Note(self, channel, note, velocity = 64):
		self.track_data += self.note_on(channel, int(note), velocity)
		print len(self.track_data)

	def play_NoteContainer(self, channel, notecontainer, velocity = 64):
		[self.play_Note(channel, x, velocity) for x in notecontainer]


	def stop_Note(self, channel, note, velocity = 64):
		self.track_data += self.note_off(channel, int(note), velocity)

	def header(self):
		print len(self.track_data), "%08x" % (len(self.track_data))
		chunk_size = a2b_hex("%08x" % (len(self.track_data) +\
				len(self.end_of_track())))
		return "MTrk" + chunk_size

	def get_midi_data(self):
		return self.header() + self.track_data + self.end_of_track()

	def midi_event(self, event_type, channel, param1, param2):
		"""Parameters should be given as integers."""
		"""event_type and channel: 4 bits."""
		"""param1 and param2: 1 byte."""
		assert event_type < 128 and event_type >= 0
		assert channel < 16 and channel >= 0
		tc = a2b_hex("%x%x" % (event_type, channel))
		params = a2b_hex("%02x%02x" % (param1, param2))

		return self.delta_time + tc + params

	def note_off(self, channel, note, velocity):
		return self.midi_event(8, channel, note, velocity)

	def note_on(self, channel, note, velocity):
		return self.midi_event(9, channel, note, velocity)

	def reset(self):
		self.track_data = ''
		self.delta_time = '\x00'

	def set_deltatime(self, delta_time):
		self.delta_time = delta_time

	def set_tempo_event(self, bpm):
		"""Calculates the microseconds per quarter note """
		"""and returns tempo event."""
		ms_per_min = 60000000
		mpqn = a2b_hex("%06x" % (ms_per_min / bpm))
		return self.delta_time + "\xff\x51\x03" + mpqn
		

def _write_file(file, data):
	try:
		f = open(file, "wb")
	except:
		print "Couldn't open '%s' for writing." % file
		return False
	try:
		f.write(data)
	except:
		print "An error occured while writing data to %s." % file
		return False
	f.close()
	return True


def write_Note(file, channel, note, velocity, repeat = 0):
	m = MidiFileOut()
	t = MidiTrack(120)
	m.tracks = [t]
	while repeat >= 0:
		t.play_Note(channel, note, velocity)
		t.set_deltatime("\x48")
		t.stop_Note(channel, note, velocity)
		repeat -= 1
	return _write_file(file, m.get_midi_data())



if __name__ == '__main__':
	write_Note("testmingus.mid", 9, 50, 100, 10)
