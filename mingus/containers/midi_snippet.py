from typing import Optional

import mido

from mingus.containers import PercussionNote


class MidiPercussionSnippet:
    def __init__(self, midi_file_path, start: float = 0.0, length_in_seconds: Optional[float] = None,
                 n_replications: int = 1):
        """

        :param midi_file_path:
        :param start: in seconds
        :param length_in_seconds: Original length. Needed for repeats.
        :param n_replications: 
        """
        self.midi_file_path = midi_file_path
        self.start = start  # in seconds
        self.length_in_seconds = length_in_seconds
        self.n_replications = n_replications
        assert not (n_replications > 1 and length_in_seconds is None), \
            f'If there are replications, then length_in_seconds cannot be None'

    def put_into_score(self, channel: int, score: dict, bpm: Optional[float] = None):
        """
        See: https://majicdesigns.github.io/MD_MIDIFile/page_timing.html
        https://mido.readthedocs.io/en/latest/midi_files.html?highlight=tempo#about-the-time-attribute

        :param channel:
        :param score: the score dict
        :param bpm: the target bpm of the first tempo in the snippet.


        :return:
        """
        midi_data = mido.MidiFile(self.midi_file_path)

        length_in_sec = 0.0
        elapsed_time = self.start
        tempo = None
        speed = None
        for i, track in enumerate(midi_data.tracks):
            # print('Track {}: {}'.format(i, track.name))
            for msg in track:
                if msg.type == 'note_on':
                    elapsed_time += mido.tick2second(msg.time, ticks_per_beat=midi_data.ticks_per_beat, tempo=tempo)

                    for j in range(self.n_replications):
                        # The score dict key in milliseconds
                        key = round((elapsed_time + j * length_in_sec) * 1000.0)
                        score.setdefault(key, []).append(
                            {
                                'func': 'start_note',
                                'note': PercussionNote(None, number=msg.note, velocity=msg.velocity, channel=channel),
                                'channel': channel,
                                'velocity': msg.velocity
                            }
                    )
                elif msg.type == 'set_tempo':
                    if tempo is None:
                        speed = bpm / mido.tempo2bpm(msg.tempo)
                        if self.length_in_seconds:
                            length_in_sec = self.length_in_seconds / speed

                    assert speed is not None, f'Could not set speed for midi snippet: {self.midi_file_path}'
                    tempo = msg.tempo / speed  # microseconds per beat
