.. module:: mingus.containers.note

======================
mingus.containers.note
======================


.. class:: Note


   .. method:: __eq__(self, other)

      Compare Notes for equality by comparing their note values.


   .. method:: __ge__(self, other)


   .. method:: __gt__(self, other)


   .. method:: __init__(self, name=C, octave=4, dynamics={})


   .. method:: __int__(self)

      Return the current octave multiplied by twelve and add
      notes.note_to_int to it.
      
      This means a C-0 returns 0, C-1 returns 12, etc. This method allows
      you to use int() on Notes.


   .. method:: __le__(self, other)


   .. method:: __lt__(self, other)

      Enable the comparing operators on Notes (>, <, \ ==, !=, >= and <=).
      
      So we can sort() Intervals, etc.
      
      Examples:
      
      >>> Note('C', 4) < Note('B', 4)
      True
      >>> Note('C', 4) > Note('B', 4)
      False


   .. method:: __ne__(self, other)


   .. method:: __repr__(self)

      Return a helpful representation for printing Note classes.


   .. method:: augment(self)

      Call notes.augment with this note as argument.


   .. method:: change_octave(self, diff)

      Change the octave of the note to the current octave + diff.


   .. method:: diminish(self)

      Call notes.diminish with this note as argument.


   .. attribute:: dynamics

      Attribute of type: dict
      ``{}``

   .. method:: empty(self)

      Remove the data in the instance.


   .. method:: from_hertz(self, hertz, standard_pitch=440)

      Set the Note name and pitch, calculated from the hertz value.
      
      The standard_pitch argument can be used to set the pitch of A-4,
      from which the rest is calculated.


   .. method:: from_int(self, integer)

      Set the Note corresponding to the integer.
      
      0 is a C on octave 0, 12 is a C on octave 1, etc.
      
      Example:
      
      >>> Note().from_int(12)
      'C-1'


   .. method:: from_shorthand(self, shorthand)

      Convert from traditional Helmhotz pitch notation.
      
      Examples:
      
      >>> Note().from_shorthand("C,,")
      'C-0'
      >>> Note().from_shorthand("C")
      'C-2'
      >>> Note().from_shorthand("c'")
      'C-4'


   .. method:: measure(self, other)

      Return the number of semitones between this Note and the other.
      
      Examples:
      
      >>> Note('C').measure(Note('D'))
      2
      >>> Note('D').measure(Note('C'))
      -2


   .. attribute:: name

      Attribute of type: str
      ``'C'``

   .. attribute:: octave

      Attribute of type: int
      ``4``

   .. method:: octave_down(self)

      Decrement the current octave with 1.


   .. method:: octave_up(self)

      Increment the current octave with 1.


   .. method:: remove_redundant_accidentals(self)

      Call notes.remove_redundant_accidentals on this note's name.


   .. method:: set_note(self, name=C, octave=4, dynamics={})

      Set the note to name in octave with dynamics.
      
      Return the objects if it succeeded, raise an NoteFormatError
      otherwise.


   .. method:: to_hertz(self, standard_pitch=440)

      Return the Note in Hz.
      
      The standard_pitch argument can be used to set the pitch of A-4,
      from which the rest is calculated.


   .. method:: to_shorthand(self)

      Give the traditional Helmhotz pitch notation.
      
      Examples:
      
      >>> Note('C-4').to_shorthand()
      "c'"
      >>> Note('C-3').to_shorthand()
      'c'
      >>> Note('C-2').to_shorthand()
      'C'
      >>> Note('C-1').to_shorthand()
      'C,'


   .. method:: transpose(self, interval, up=True)

      Transpose the note up or down the interval.
      
      Examples:
      
      >>> a = Note('A')
      >>> a.transpose('3')
      >>> a
      'C#-5'
      >>> a.transpose('3', False)
      >>> a
      'A-4'

----



:doc:`Back to Index</index>`
