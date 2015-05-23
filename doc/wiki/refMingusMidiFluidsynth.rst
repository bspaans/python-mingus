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



----

.. data:: initialized

   Attribute of type: bool
   ``False``

----

.. data:: midi

   Attribute of type: mingus.midi.fluidsynth.FluidSynthSequencer
   ``<mingus.midi.fluidsynth.FluidSynthSequencer object at 0x7f1b1a7cda10>``

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
