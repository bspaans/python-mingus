.. module:: mingus.midi.fluidsynth

======================
mingus.midi.fluidsynth
======================

FluidSynth support for mingus.

FluidSynth is a software MIDI synthesizer which allows you to play the
containers in mingus.containers real-time. To work with this module, you'll
need fluidsynth and a nice instrument collection (look here:
http://www.hammersound.net, go to Sounds → Soundfont Library → Collections).

To start using FluidSynth with mingus, do:
>>> from mingus.midi import fluidsynth
>>> fluidsynth.init('soundfontlocation.sf2')

Now you are ready to play Notes, NoteContainers, etc.



.. class:: FluidSynthSequencer


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

   .. method:: __del__(self)


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


   .. method:: load_sound_font(self, sf2)

      Load a sound font.
      
      Return True on success, False on failure.
      
      This function should be called before your audio can be played,
      since the instruments are kept in the sf2 file.


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


   .. method:: start_audio_output(self, driver=None)

      Start the audio output.
      
      The optional driver argument can be any of 'alsa', 'oss', 'jack',
      'portaudio', 'sndmgr', 'coreaudio', 'Direct Sound', 'dsound',
      'pulseaudio'. Not all drivers will be available for every platform.


   .. method:: start_recording(self, file=mingus_dump.wav)

      Initialize a new wave file for recording.


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

.. data:: initialized

      Attribute of type: bool
      ``False``

----

.. data:: midi

      Attribute of type: mingus.midi.fluidsynth.FluidSynthSequencer
      ``<mingus.midi.fluidsynth.FluidSynthSequencer object at 0x7f906636a890>``

----

.. function:: control_change(channel, control, value)

      Send a control change event on channel.


----

.. function:: init(sf2, driver=None, file=None)

      Initialize the audio.
      
      Return True on success, False on failure.
      
      This function needs to be called before you can have any audio.
      
      The sf2 argument should be the location of a valid soundfont file.
      
      The optional driver argument can be any of 'alsa', 'oss', 'jack',
      'portaudio', 'sndmgr', 'coreaudio' or 'Direct Sound'.
      
      If the file argument is not None, then instead of loading the driver, a
      new wave file will be initialized to store the audio data.


----

.. function:: main_volume(channel, value)


----

.. function:: modulation(channel, value)


----

.. function:: pan(channel, value)


----

.. function:: play_Bar(bar, channel=1, bpm=120)

      Play a Bar object using play_NoteContainer and stop_NoteContainer.
      
      Set a bpm attribute on a NoteContainer to change the tempo.


----

.. function:: play_Bars(bars, channels, bpm=120)

      Play a list of bars on the given list of channels.
      
      Set a bpm attribute on a NoteContainer to change the tempo.


----

.. function:: play_Composition(composition, channels=None, bpm=120)

      Play a composition.


----

.. function:: play_Note(note, channel=1, velocity=100)

      Convert a Note object to a 'midi on' command.
      
      The channel and velocity can be set as Note attributes as well. If
      that's the case those values take presedence over the ones given here as
      function arguments.
      
      Example:
      
      >>> n = Note('C', 4)
      >>> n.channel = 9
      >>> n.velocity = 50
      >>> FluidSynth.play_Note(n)


----

.. function:: play_NoteContainer(nc, channel=1, velocity=100)

      Use play_Note to play the Notes in the NoteContainer nc.


----

.. function:: play_Track(track, channel=1, bpm=120)

      Use play_Bar to play a Track object.


----

.. function:: play_Tracks(tracks, channels, bpm=120)

      Use play_Bars to play a list of Tracks on the given list of channels.


----

.. function:: set_instrument(channel, instr, bank=0)


----

.. function:: stop_Note(note, channel=1)

      Stop the Note playing at channel.
      
      If a channel attribute is set on the note, it will take presedence.


----

.. function:: stop_NoteContainer(nc, channel=1)

      Use stop_Note to stop the notes in NoteContainer nc.


----

.. function:: stop_everything()

      Stop all the playing notes on all channels.

----



:doc:`Back to Index</index>`
