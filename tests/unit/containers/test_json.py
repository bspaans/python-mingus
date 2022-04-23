from mingus.containers.note import Note, PercussionNote
from mingus.tools import mingus_json


def test_json():
    c_note = Note("C", 5)
    p_note = PercussionNote('Ride Cymbal 1', velocity=62)
    initial = [c_note, p_note]

    s = mingus_json.encode(initial)
    results = mingus_json.decode(s)

    assert results == initial
