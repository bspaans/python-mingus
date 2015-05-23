========================
mingus.midi.midi_file_in
========================

Read a MIDI file and convert it into mingus.containers objects.

Functions
---------



.. function:: MIDI_to_Composition(file)

  Convert a MIDI file to a mingus.containers.Composition and return it
in a tuple with the last used tempo in beats per minute (this will
change in the future).

This function can raise all kinds of exceptions (IOError, HeaderError,
TimeDivisionError, FormatError), so be sure to try and catch.

----

:doc:`Back to Index</index>`
