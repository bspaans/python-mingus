"""
MIDI percussion is treated as one instrument, with each type of percussion instrument being a "key"
(i.e. like a key on a piano.
"""

midi_percussion = {
    'Acoustic Bass Drum': 35,
    'Bass Drum 1': 36,
    'Side Stick': 37,
    'Acoustic Snare': 38,
    'Hand Clap': 39,
    'Electric Snare': 40,
    'Low Floor Tom': 41,
    'Closed Hi Hat': 42,
    'High Floor Tom': 43,
    'Pedal Hi-Hat': 44,
    'Low Tom': 45,
    'Open Hi-Hat': 46,
    'Low-Mid Tom': 47,
    'Hi Mid Tom': 48,
    'Crash Cymbal 1': 49,
    'High Tom': 50,
    'Ride Cymbal 1': 51,
    'Chinese Cymbal': 52,
    'Ride Bell': 53,
    'Tambourine': 54,
    'Splash Cymbal': 55,
    'Cowbell': 56,
    'Crash Cymbal 2': 57,
    'Vibraslap': 58,
    'Ride Cymbal 2': 59,
    'Hi Bongo': 60,
    'Low Bongo': 61,
    'Mute Hi Conga': 62,
    'Open Hi Conga': 63,
    'Low Conga': 64,
    'High Timbale': 65,
    'Low Timbale': 66,
    'High Agogo': 67,
    'Low Agogo': 68,
    'Cabasa': 69,
    'Maracas': 70,
    'Short Whistle': 71,
    'Long Whistle': 72,
    'Short Guiro': 73,
    'Long Guiro': 74,
    'Claves': 75,
    'Hi Wood Block': 76,
    'Low Wood Block': 77,
    'Mute Cuica': 78,
    'Open Cuica': 79,
    'Mute Triangle': 80,
    'Open Triangle': 81
}


class MidiPercussion:
    def __init__(self, bank=128):
        self.bank = bank
        self.number = 1
        self.name = 'Percussion'
