=========================
mingus.midi.midi_file_out
=========================

Functions that can generate MIDI files from the objects in
mingus.containers.

Functions
---------

.. function:: write_Bar(file, bar, bpm, repeat, verbose)  * *Default values*: bpm = 120, repeat = 0, verbose = False
Write a mingus.Bar to a MIDI file.

Both the key and the meter are written to the file as well.

.. function:: write_Composition(file, composition, bpm, repeat, verbose)  * *Default values*: bpm = 120, repeat = 0, verbose = False
Write a mingus.Composition to a MIDI file.

.. function:: write_Note(file, note, bpm, repeat, verbose)  * *Default values*: bpm = 120, repeat = 0, verbose = False
Expect a Note object from mingus.containers and save it into a MIDI
file, specified in file.

You can set the velocity and channel in Note.velocity and Note.channel.

.. function:: write_NoteContainer(file, notecontainer, bpm, repeat, verbose)  * *Default values*: bpm = 120, repeat = 0, verbose = False
Write a mingus.NoteContainer to a MIDI file.

.. function:: write_Track(file, track, bpm, repeat, verbose)  * *Default values*: bpm = 120, repeat = 0, verbose = False
Write a mingus.Track to a MIDI file.

Write the name to the file and set the instrument if the instrument has
the attribute instrument_nr, which represents the MIDI instrument
number. The class MidiInstrument in mingus.containers.Instrument has
this attribute by default.

----

:doc:`Back to Index</index>`
