from mingus.midi.sequencer2 import Sequencer
from mingus.containers import PercussionNote, Track
from mingus.containers.raw_snippet import RawSnippet

import midi_percussion as mp


def test_snippets():
    recording = {}
    channel = 1
    instrument_number = mp.percussion_instruments['Acoustic Snare']
    note = PercussionNote(name=None, number=instrument_number, velocity=64, channel=channel)
    for i in range(4):
        recording[i * 1000] = [
            {
                'func': 'start_note',
                'note': note,
                'channel': note.channel,
                'velocity': note.velocity
            }
        ]

    snippet = RawSnippet(recording)
    track = Track(instrument=mp.MidiPercussion(), snippets=[snippet])
    sequencer = Sequencer()
    sequencer.play_Track(track, channel=channel)

    assert len(sequencer.score) == 4
    assert sequencer.score[0][0]['func'] == 'start_note'
    assert sequencer.score[0][0]['channel'] == channel
    assert sequencer.score[0][0]['velocity'] == 64
    assert isinstance(sequencer.score[0][0]['note'], PercussionNote)
