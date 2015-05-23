.. module:: mingus.midi.sequencer

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



.. class:: Sequencer


   .. attribute:: MSG_CC

      Attribute of type: int
      ``2``

   .. attribute:: MSG_INSTR

      Attribute of type: int
      ``3``

   .. attribute:: MSG_PLAY_BAR

      Attribute of type: int
      ``9``

   .. attribute:: MSG_PLAY_BARS

      Attribute of type: int
      ``10``

   .. attribute:: MSG_PLAY_COMPOSITION

      Attribute of type: int
      ``13``

   .. attribute:: MSG_PLAY_INT

      Attribute of type: int
      ``0``

   .. attribute:: MSG_PLAY_NC

      Attribute of type: int
      ``7``

   .. attribute:: MSG_PLAY_NOTE

      Attribute of type: int
      ``5``

   .. attribute:: MSG_PLAY_TRACK

      Attribute of type: int
      ``11``

   .. attribute:: MSG_PLAY_TRACKS

      Attribute of type: int
      ``12``

   .. attribute:: MSG_SLEEP

      Attribute of type: int
      ``4``

   .. attribute:: MSG_STOP_INT

      Attribute of type: int
      ``1``

   .. attribute:: MSG_STOP_NC

      Attribute of type: int
      ``8``

   .. attribute:: MSG_STOP_NOTE

      Attribute of type: int
      ``6``

   .. method:: __init__(self)


   .. method:: attach(self, listener)

      Attach an object that should be notified of events.
      
      The object should have a notify(msg_type, param_dict) function.


   .. method:: cc_event(self, channel, control, value)


   .. method:: control_change(self, channel, control, value)

      Send a control change message.
      
      See the MIDI specification for more information.


   .. method:: detach(self, listener)

      Detach a listening object so that it won't receive any events
      anymore.


   .. method:: init(self)


   .. method:: instr_event(self, channel, instr, bank)


   .. method:: main_volume(self, channel, value)

      Set the main volume.


   .. method:: modulation(self, channel, value)

      Set the modulation.


   .. method:: notify_listeners(self, msg_type, params)

      Send a message to all the observers.


   .. attribute:: output

      Attribute of type: NoneType
      ``None``

   .. method:: pan(self, channel, value)

      Set the panning.


   .. method:: play_Bar(self, bar, channel=1, bpm=120)

      Play a Bar object.
      
      Return a dictionary with the bpm lemma set on success, an empty dict
      on some kind of failure.
      
      The tempo can be changed by setting the bpm attribute on a
      NoteContainer.


   .. method:: play_Bars(self, bars, channels, bpm=120)

      Play several bars (a list of Bar objects) at the same time.
      
      A list of channels should also be provided. The tempo can be changed
      by providing one or more of the NoteContainers with a bpm argument.


   .. method:: play_Composition(self, composition, channels=None, bpm=120)

      Play a Composition object.


   .. method:: play_Note(self, note, channel=1, velocity=100)

      Play a Note object on a channel with a velocity[0-127].
      
      You can either specify the velocity and channel here as arguments or
      you can set the Note.velocity and Note.channel attributes, which
      will take presedence over the function arguments.


   .. method:: play_NoteContainer(self, nc, channel=1, velocity=100)

      Play the Notes in the NoteContainer nc.


   .. method:: play_Track(self, track, channel=1, bpm=120)

      Play a Track object.


   .. method:: play_Tracks(self, tracks, channels, bpm=120)

      Play a list of Tracks.
      
      If an instance of MidiInstrument is used then the instrument will be
      set automatically.


   .. method:: play_event(self, note, channel, velocity)


   .. method:: set_instrument(self, channel, instr, bank=0)

      Set the channel to the instrument _instr_.


   .. method:: sleep(self, seconds)


   .. method:: stop_Note(self, note, channel=1)

      Stop a note on a channel.
      
      If Note.channel is set, it will take presedence over the channel
      argument given here.


   .. method:: stop_NoteContainer(self, nc, channel=1)

      Stop playing the notes in NoteContainer nc.


   .. method:: stop_event(self, note, channel)


   .. method:: stop_everything(self)

      Stop all the notes on all channels.

----



:doc:`Back to Index</index>`
