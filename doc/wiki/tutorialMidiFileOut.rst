Tutorial 2 - Saving Containers as Midi Files
============================================



>>> from mingus.midi import midi_file_out




----


Saving Notes, NoteContainers, Bars, Tracks and Compositions
-----------------------------------------------------------

The functions in this module all work the same and are very simple to use. `write_Note`, `write_NoteContainer`, `write_Bar`, `write_Track` and `write_Composition` all take four arguments, from which the last two are optional. The first argument specifies the filename, the second is the object itself, the third argument is the number of beats per minute (default = 120) and the last argument specifies the number of times the object should be repeated (default = 0).


>>> from mingus.containers import NoteContainer
>>> nc = NoteContainer(["A", "C", "E"])
>>> midi_file_out.write_NoteContainer("test.mid", nc)


As in the FluidSynth module you can set the channel and velocity on Notes by setting the `channel` and `velocity` attributes. And again, to change the tempo you can set the `bpm` attribute on a NoteContainer.


----


You can learn more about `mingus.midi.MidiFileOut <refMingusMidiMidifileout>`_ in the reference section.

  * `Playing Containers with FluidSynth <tutorialFluidsynth>`_
  * Saving Containers as Midi File
  * :doc:`Back to Index </index>`
