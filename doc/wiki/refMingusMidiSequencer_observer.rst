.. module:: mingus.midi.sequencer_observer

==============================
mingus.midi.sequencer_observer
==============================

Provides an easy to extend base class that can be used to observe a
Sequencer.

Each time a Sequencer starts playing a new Note, Bar, w/e, an event is
fired; this SequencerObserver intercepts the event messages and calls the
proper function so you only have to implement the functions for the events
you need to see.



.. class:: SequencerObserver


   .. method:: cc_event(self, channel, control, value)


   .. method:: instr_event(self, channel, instr, bank)


   .. method:: notify(self, msg_type, params)


   .. method:: play_Bar(self, bar, channel, bpm)


   .. method:: play_Bars(self, bars, channels, bpm)


   .. method:: play_Composition(self, composition, channels, bpm)


   .. method:: play_Note(self, note, channel, velocity)


   .. method:: play_NoteContainer(self, notes, channel)


   .. method:: play_Track(self, track, channel, bpm)


   .. method:: play_Tracks(self, tracks, channels, bpm)


   .. method:: play_int_note_event(self, int_note, channel, velocity)


   .. method:: sleep(self, seconds)


   .. method:: stop_Note(self, note, channel)


   .. method:: stop_NoteContainer(self, notes, channel)


   .. method:: stop_int_note_event(self, int_note, channel)

----



:doc:`Back to Index</index>`
