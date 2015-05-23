.. module:: mingus.containers.Guitar

========================
mingus.containers.Guitar
========================


----

.. data:: clef

      Attribute of type: str
      ``'Treble'``

----

.. data:: name

      Attribute of type: str
      ``'Guitar'``

----

.. data:: range

      Attribute of type: tuple
      ``('E-3', 'E-7')``

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
