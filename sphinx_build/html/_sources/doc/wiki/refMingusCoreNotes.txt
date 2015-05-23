.. module:: mingus.core.notes

=================
mingus.core.notes
=================

Basic module for notes.

This module is the foundation of the music theory package.

It handles conversions from integers to notes and vice versa and thus
enables simple calculations.



----

.. data:: fifths

      Attribute of type: list
      ``['F', 'C', 'G', 'D', 'A', 'E', 'B']``

----

.. function:: augment(note)

      Augment a given note.
      
      Examples:
      
      >>> augment('C')
      'C#'
      >>> augment('Cb')
      'C'


----

.. function:: diminish(note)

      Diminish a given note.
      
      Examples:
      
      >>> diminish('C')
      'Cb'
      >>> diminish('C#')
      'C'


----

.. function:: int_to_note(note_int, accidentals=#)

      Convert integers in the range of 0-11 to notes in the form of C or C#
      or Db.
      
      Throw a RangeError exception if the note_int is not in the range 0-11.
      
      If not specified, sharps will be used.
      
      Examples:
      
      >>> int_to_note(0)
      'C'
      >>> int_to_note(3)
      'D#'
      >>> int_to_note(3, 'b')
      'Eb'


----

.. function:: is_enharmonic(note1, note2)

      Test whether note1 and note2 are enharmonic, i.e. they sound the same.


----

.. function:: is_valid_note(note)

      Return True if note is in a recognised format. False if not.


----

.. function:: note_to_int(note)

      Convert notes in the form of C, C#, Cb, C##, etc. to an integer in the
      range of 0-11.
      
      Throw a NoteFormatError exception if the note format is not recognised.


----

.. function:: reduce_accidentals(note)

      Reduce any extra accidentals to proper notes.
      
      Example:
      
      >>> reduce_accidentals('C####')
      'E'


----

.. function:: remove_redundant_accidentals(note)

      Remove redundant sharps and flats from the given note.
      
      Examples:
      
      >>> remove_redundant_accidentals('C##b')
      'C#'
      >>> remove_redundant_accidentals('Eb##b')
      'E'

----



:doc:`Back to Index</index>`
