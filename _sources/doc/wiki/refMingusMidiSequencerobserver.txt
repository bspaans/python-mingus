.. module:: mingus.midi.SequencerObserver

=============================
mingus.midi.SequencerObserver
=============================

An easy to extend base class that can be used to observe a Sequencer.

    Each time a Sequencer starts playing a new Note, Bar, w/e, an event is
    fired; this SequencerObserver intercepts the event messages and calls
    the proper function so you only have to implement the functions for the
    events you need to see.
    


----

.. function:: cc_event(self, channel, control, value)


----

.. function:: instr_event(self, channel, instr, bank)


----

.. function:: notify(self, msg_type, params)


----

.. function:: play_Bar(self, bar, channel, bpm)


----

.. function:: play_Bars(self, bars, channels, bpm)


----

.. function:: play_Composition(self, composition, channels, bpm)


----

.. function:: play_Note(self, note, channel, velocity)


----

.. function:: play_NoteContainer(self, notes, channel)


----

.. function:: play_Track(self, track, channel, bpm)


----

.. function:: play_Tracks(self, tracks, channels, bpm)


----

.. function:: play_int_note_event(self, int_note, channel, velocity)


----

.. function:: sleep(self, seconds)


----

.. function:: stop_Note(self, note, channel)


----

.. function:: stop_NoteContainer(self, notes, channel)


----

.. function:: stop_int_note_event(self, int_note, channel)

----



:doc:`Back to Index</index>`
