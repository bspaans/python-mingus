Tutorial 1 - Playing Containers with FluidSynth 
===============================================

`FluidSynth` is a MIDI synthesizer which uses SoundFont (.SF2) files to generate audio. To work with this module, you'll need the FluidSynth library (usually packaged with the stand-alone program) and a nice instrument collection (look here: http://www.hammersound.net, go to Sounds -> Soundfont Library -> Collections). 


>>> from mingus.midi import fluidsynth




----


Loading a SoundFont
-------------------

To load the SoundFont and initialize FluidSynth we'll only have to call `init`.


>>> fluidsynth.init("soundfont.SF2")


You can give an optional second argument to specify a driver (one of 'alsa', 'oss', 'jack', 'portaudio', 'sndmgr', 'coreaudio' or 'Direct Sound'), otherwise the default driver for the system will be used.


>>> fluidsynth.init("soundfont.SF2", "alsa")



----


Playing mingus.containers Objects
---------------------------------

play_Note
^^^^^^^^^

`play_Note(note, channel = 1, velocity = 100)` converts the given Note object to a midi `note on` command on `channel`. The velocity (0-127) stands for the speed with which the notes are hit. This roughly translates to volume.


>>> fluidsynth.play_Note(Note("C-5"))
True
>>> fluidsynth.play_Note(Note("E-5"))
True


The channel and velocity can be set as Note attributes as well. If that's the case those values take presedence over the ones given here as function arguments. 


>>> n = Note("C-5")
>>> n.channel = 5
>>> n.velocity = 50
>>> fluidsynth.play_Note(n)
True


stop_Note
^^^^^^^^^

If a playing note needs to be stopped, `stop_Note(note, channel = 1)` can be used. 


>>> fluidsynth.stop_Note(Note("C-5"), 1)
True


*Note* it doesn't matter if the note is actually playing; ie. nothing will break when you try to stop a note that is already stopped.

Playing and Stopping NoteContainers 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`play_NoteContainer(notecontainer, channel = 1, velocity = 100)` and stop_NoteContainer(notecontainer, channel = 1)` work the same as `play_Note` and `stop_Note`.


>>> fluidsynth.play_NoteContainer(NoteContainer(["C", "E"]))
True
>>> fluidsynth.stop_NoteContainer(NoteContainer(["C", "E"]))
True


Playing Bars, Tracks and Compositions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`play_Bar`, `play_Track` and `play_Composition` all take three arguments. The first is the object itself, the second is the channel which defaults to 1, and the last one is the number of beats per minute which denotes tempo. 


>>> b = Bar()

# Fill the Bar with NoteContainers.

>>> fluidsynth.play_Bar(b, 1, 150)


*Note* You can set a `bpm` attribute on a NoteContainer to change the tempo. Furthermore, you can set a Track's `instrument` attribute to a MidiInstrument object so that play_Track and play_Composition know which instrument to use.


----


Misc. MIDI Commands
-------------------

Change the Instrument
^^^^^^^^^^^^^^^^^^^^^

`set_instrument(channel, instr, bank = 0)` can be used to change the instrument that is being used on a channel. You can find a list of instruments by googling for `midi instruments table`, but you can also use the `names` attribute in the MidiInstrument class found in mingus.containers.Instrument. 


>>> fluidsynth.set_instrument(1, 14)


Panning, Modulation and Other Control Change Commands
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`panning(channel, value)` and `modulation(channel, value)` are shortcuts to the `control_change(channel, control, value)` function added for your convenience. There are more control change commands however. You can find tables by googling, but know that FluidSynth ignores some of the commands.


----


You can learn more about `mingus.midi.fluidsynth <refMingusMidiFluidsynth>`_ in the reference section.

  * `Saving Containers as Midi File <tutorialMidiFileOut>`_
  * :doc:`Back to Index </index>`
