=====================
mingus.midi.sequencer
=====================

A general purpose sequencer for the objects in mingus.containers.

You can use the Sequencer object either by creating a subclass and
implementing some of the events (init, play_event, stop_event, cc_event,
instr_event) or by attaching observer objects via 'attach' and catching the
messages in the notify(msg_type, param_dict) function of your object.

See SequencerObserver for a pre made, easy to extend base class that can be
attached to the Sequencer.


----



:doc:`Back to Index</index>`
