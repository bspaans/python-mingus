.. module:: mingus.containers.bar

=====================
mingus.containers.bar
=====================


.. class:: Bar


   .. method:: __add__(self, note_container)

      Enable the '+' operator on Bars.


   .. method:: __eq__(self, other)

      Enable the '==' operator for Bars.


   .. method:: __getitem__(self, index)

      Enable the  '[]' notation on Bars to get the item at the index.


   .. method:: __init__(self, key=C, meter=(4, 4))


   .. method:: __len__(self)

      Enable the len() method for Bars.


   .. method:: __repr__(self)

      Enable str() and repr() for Bars.


   .. method:: __setitem__(self, index, value)

      Enable the use of [] = notation on Bars.
      
      The value should be a NoteContainer, or a string/list/Note
      understood by the NoteContainer.


   .. method:: augment(self)

      Augment the NoteContainers in Bar.


   .. attribute:: bar

      Attribute of type: list
      ``[]``

   .. method:: change_note_duration(self, at, to)

      Change the note duration at the given index to the given
      duration.


   .. attribute:: current_beat

      Attribute of type: float
      ``0.0``

   .. method:: determine_chords(self, shorthand=False)

      Return a list of lists [place_in_beat, possible_chords].


   .. method:: determine_progression(self, shorthand=False)

      Return a list of lists [place_in_beat, possible_progressions].


   .. method:: diminish(self)

      Diminish the NoteContainers in Bar.


   .. method:: empty(self)

      Empty the Bar, remove all the NoteContainers.


   .. method:: get_note_names(self)

      Return a list of unique note names in the Bar.


   .. method:: get_range(self)

      Return the highest and the lowest note in a tuple.


   .. method:: is_full(self)

      Return False if there is room in this Bar for another
      NoteContainer, True otherwise.


   .. attribute:: key

      Attribute of type: str
      ``'C'``

   .. attribute:: length

      Attribute of type: float
      ``0.0``

   .. attribute:: meter

      Attribute of type: tuple
      ``(4, 4)``

   .. method:: place_notes(self, notes, duration)

      Place the notes on the current_beat.
      
      Notes can be strings, Notes, list of strings, list of Notes or a
      NoteContainer.
      
      Raise a MeterFormatError if the duration is not valid.
      
      Return True if succesful, False otherwise (ie. the Bar hasn't got
      enough room for a note of that duration).


   .. method:: place_notes_at(self, notes, at)

      Place notes at the given index.


   .. method:: place_rest(self, duration)

      Place a rest of given duration on the current_beat.
      
      The same as place_notes(None, duration).


   .. method:: remove_last_entry(self)

      Remove the last NoteContainer in the Bar.


   .. method:: set_meter(self, meter)

      Set the meter of this bar.
      
      Meters in mingus are represented by a single tuple.
      
      If the format of the meter is not recognised, a MeterFormatError
      will be raised.


   .. method:: space_left(self)

      Return the space left on the Bar.


   .. method:: transpose(self, interval, up=True)

      Transpose the notes in the bar up or down the interval.
      
      Call transpose() on all NoteContainers in the bar.


   .. method:: value_left(self)

      Return the value left on the Bar.

----



:doc:`Back to Index</index>`
