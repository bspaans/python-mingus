from unittest import TestCase


def get_note_length(note_type, beat_length, bpm) -> int:
    """
    Since we are working in milliseconds as integers, we want to unify how we calculate
    note lengths so that tracks do not get out of sync

    :param note_type: 1=whole note, 4 = quarter note, etc...
    :param beat_length: 4 - quarter note, 8 - eighth note
    :param bpm: beats per minute
    :return: note length in milliseconds
    """
    beat_ms = ((1.0 / bpm) * 60.0) * 1000.0  # milliseconds
    length = (beat_length / note_type) * beat_ms
    return round(length)


def get_beat_start(beat_number, bpm):
    """

    :param beat_number: 1, 2, 3, 4 for 4/4, etc..
    :param bpm: beats per minute
    :return: note length in milliseconds
    """
    beat_ms = ((1.0 / bpm) * 60.0) * 1000.0  # milliseconds
    start = (beat_number - 1.0) * beat_ms
    return round(start)


def get_bar_length(meter, bpm):
    return get_beat_start(meter[0] + 1, bpm)


class TestLengthCalculations(TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.whole = 1.0
        self.quarter = 4.0
        self.eighth = 8.0

    def test_get_note_length(self):
        # A quarter note, in 4/4 with 1/2 second per beat
        length = get_note_length(self.quarter, 4.0, 120.0)
        self.assertEqual(500, length)

        # A whole note, in 4/4 with 1/2 second per beat
        length = get_note_length(self.whole, 4.0, 120.0)
        self.assertEqual(2000, length)

        # An eighth note, in 4/4 with 1/2 second per beat
        length = get_note_length(self.eighth, 4.0, 120.0)
        self.assertEqual(250, length)

        # An eighth note, in 6/8 with 1/2 second per beat
        length = get_note_length(self.eighth, 8.0, 120.0)
        self.assertEqual(500, length)

        # An quarter note, in 6/8 with 1/2 second per beat
        length = get_note_length(self.quarter, 8.0, 120.0)
        self.assertEqual(1000, length)

    def test_get_beat_start(self):
        start = get_beat_start(2.0, 120.0)
        self.assertEqual(500, start)

    def test_get_bar_length(self):
        length = get_bar_length((4.0, 4.0), 120.0)
        self.assertEqual(2000, length)

        length = get_bar_length((6.0, 8.0), 120.0)
        self.assertEqual(3000, length)
