.. module:: mingus.containers.Piano

=======================
mingus.containers.Piano
=======================


----

.. data:: clef

      Attribute of type: str
      ``'bass and treble'``

----

.. data:: name

      Attribute of type: str
      ``'Piano'``

----

.. data:: range

      Attribute of type: tuple
      ``('F-0', 'B-8')``

----

.. data:: tuning

      Attribute of type: NoneType
      ``None``

----

.. function:: __init__(self)


----

.. function:: __repr__(self)

      Return a string representing the object.


----

.. function:: can_play_notes(self, notes)

      Test if the notes lie within the range of the instrument.
      
      Return True if so, False otherwise.


----

.. function:: note_in_range(self, note)

      Test whether note is in the range of this Instrument.
      
      Return True if so, False otherwise.


----

.. function:: notes_in_range(self, notes)

      An alias for can_play_notes.


----

.. function:: set_range(self, range)

      Set the range of the instrument.
      
      A range is a tuple of two Notes or note strings.

----



:doc:`Back to Index</index>`
