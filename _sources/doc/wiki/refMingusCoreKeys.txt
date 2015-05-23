.. module:: mingus.core.keys

================
mingus.core.keys
================

Module for dealing with keys.

This module provides a simple interface for dealing with keys.



.. class:: Key


   .. method:: __eq__(self, other)


   .. method:: __init__(self, key=C)


   .. method:: __ne__(self, other)


----

.. data:: base_scale

      Attribute of type: list
      ``['C', 'D', 'E', 'F', 'G', 'A', 'B']``

----

.. data:: couple

      Attribute of type: tuple
      ``('C#', 'a#')``

----

.. data:: keys

      Attribute of type: list
      ``[('Cb', 'ab'), ('Gb', 'eb'), ('Db', 'bb'), ('Ab', 'f'), ('Eb', 'c'), ('Bb', 'g'), ('F', 'd'), ('C', 'a'), ('G', 'e'), ('D', 'b'), ('A', 'f#'), ('E', 'c#'), ('B', 'g#'), ('F#', 'd#'), ('C#', 'a#')]``

----

.. data:: major_keys

      Attribute of type: list
      ``['Cb', 'Gb', 'Db', 'Ab', 'Eb', 'Bb', 'F', 'C', 'G', 'D', 'A', 'E', 'B', 'F#', 'C#']``

----

.. data:: minor_keys

      Attribute of type: list
      ``['ab', 'eb', 'bb', 'f', 'c', 'g', 'd', 'a', 'e', 'b', 'f#', 'c#', 'g#', 'd#', 'a#']``

----

.. function:: get_key(accidentals=0)

      Return the key corrisponding to accidentals.
      
      Return the tuple containing the major key corrensponding to the
      accidentals put as input, and his relative minor; negative numbers for
      flats, positive numbers for sharps.


----

.. function:: get_key_signature(key=C)

      Return the key signature.
      
      0 for C or a, negative numbers for flat key signatures, positive numbers
      for sharp key signatures.


----

.. function:: get_key_signature_accidentals(key=C)

      Return the list of accidentals present into the key signature.


----

.. function:: get_notes(key=C)

      Return an ordered list of the notes in this natural key.
      
      Examples:
      
      >>> get_notes('F')
      ['F', 'G', 'A', 'Bb', 'C', 'D', 'E']
      >>> get_notes('c')
      ['C', 'D', 'Eb', 'F', 'G', 'Ab', 'Bb']


----

.. function:: is_valid_key(key)

      Return True if key is in a recognized format. False if not.


----

.. function:: relative_major(key)

      Return the relative major of a minor key.
      
      Example:
      
      >>> relative_major('a')
      'C'


----

.. function:: relative_minor(key)

      Return the relative minor of a major key.
      
      Example:
      
      >>> relative_minor('C')
      'a'

----



:doc:`Back to Index</index>`
