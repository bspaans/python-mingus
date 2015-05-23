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


----



:doc:`Back to Index</index>`
