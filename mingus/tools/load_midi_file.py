from collections import defaultdict

from pathlib import Path

import mido


path = Path.home() / 'drum 2.mid'

mid = mido.MidiFile(path)

inst = defaultdict(list)
events = defaultdict(list)

elapsed_time = 0
tempo = 500_000
for i, track in enumerate(mid.tracks):
    print('Track {}: {}'.format(i, track.name))
    for msg in track:
        if msg.type == 'note_on':
            elapsed_time += mido.tick2second(msg.time, ticks_per_beat=mid.ticks_per_beat, tempo=tempo)
            print(f'Elapsed: {elapsed_time}  instrument: {msg.note}  velocity: {msg.velocity}')
        elif msg.type == 'set_tempo':
            tempo = msg.tempo
        print(msg)


print('x')
