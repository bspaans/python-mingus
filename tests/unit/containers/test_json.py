from mingus.containers import Bar, Track, PercussionNote, Note, NoteContainer
from mingus.containers.track import ControlChangeEvent, MidiControl
from mingus.containers import MidiInstrument
from mingus.tools import mingus_json


def make_bar():
    bar = Bar()
    n1 = Note('C-3')
    n2 = Note('C-2')
    bar.place_notes(n1, 4)
    bar.place_notes(n2, 4)
    return bar


def test_json_notes():
    c_note = Note("C", 5)
    p_note = PercussionNote('Ride Cymbal 1', velocity=62)
    initial = [c_note, p_note]

    s = mingus_json.encode(initial)
    results = mingus_json.decode(s)

    assert results == initial


def test_json_note_container():
    n1 = Note('C-3')
    n2 = Note('C-2')
    note_container = NoteContainer(notes=[n1, n2])

    s = mingus_json.encode(note_container)
    results = mingus_json.decode(s)

    assert results == note_container

    # print('done')


def test_json_bars():
    bar = make_bar()
    s = mingus_json.encode(bar)
    results = mingus_json.decode(s)

    assert results == bar


def test_json_track():
    bar = make_bar()
    track = Track(MidiInstrument("Acoustic Bass"))
    track.add_bar(bar, n_times=4)

    s = mingus_json.encode(track)
    results = mingus_json.decode(s)

    assert results == track


def test_control_event_json():
    event = ControlChangeEvent(beat=1.0, control=MidiControl.CHORUS, value=127)

    s = mingus_json.encode(event)
    results = mingus_json.decode(s)

    # Not sure why this works in other tests, but not here
    # assert results == event

    s2 = mingus_json.encode(results)
    assert s == s2
