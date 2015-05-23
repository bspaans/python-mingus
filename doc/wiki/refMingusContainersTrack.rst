.. module:: mingus.containers.track

=======================
mingus.containers.track
=======================


.. class:: Track


   .. method:: __add__(self, value)

      Enable the '+' operator for Tracks.
      
      Notes, notes as string, NoteContainers and Bars accepted.


   .. method:: __eq__(self, other)

      Enable the '==' operator for tracks.


   .. method:: __getitem__(self, index)

      Enable the '[]' notation for Tracks.


   .. method:: __init__(self, instrument=None)


   .. method:: __len__(self)

      Enable the len() function for Tracks.


   .. method:: __repr__(self)

      Return a string representing the class.


   .. method:: __setitem__(self, index, value)

      Enable the '[] =' notation for Tracks.
      
      Throw an UnexpectedObjectError if the value being set is not a
      mingus.containers.Bar object.


   .. method:: add_bar(self, bar)

      Add a Bar to the current track.


   .. method:: add_notes(self, note, duration=None)

      Add a Note, note as string or NoteContainer to the last Bar.
      
      If the Bar is full, a new one will automatically be created.
      
      If the Bar is not full but the note can't fit in, this method will
      return False. True otherwise.
      
      An InstrumentRangeError exception will be raised if an Instrument is
      attached to the Track, but the note turns out not to be within the
      range of the Instrument.


   .. method:: augment(self)

      Augment all the bars in the Track.


   .. attribute:: bars

      Attribute of type: list
      ``[]``

   .. method:: diminish(self)

      Diminish all the bars in the Track.


   .. method:: from_chords(self, chords, duration=1)

      Add chords to the Track.
      
      The given chords should be a list of shorthand strings or list of
      list of shorthand strings, etc.
      
      Each sublist divides the value by 2.
      
      If a tuning is set, chords will be expanded so they have a proper
      fingering.
      
      Example:
      
      >>> t = Track().from_chords(['C', ['Am', 'Dm'], 'G7', 'C#'], 1)


   .. method:: get_notes(self)

      Return an iterator that iterates through every bar in the this
      track.


   .. method:: get_tuning(self)

      Return a StringTuning object.
      
      If an instrument is set and has a tuning it will be returned.
      Otherwise the track's one will be used.


   .. attribute:: instrument

      Attribute of type: NoneType
      ``None``

   .. attribute:: name

      Attribute of type: str
      ``'Untitled'``

   .. method:: set_tuning(self, tuning)

      Set the tuning attribute on both the Track and its instrument (when
      available).
      
      Tuning should be a StringTuning or derivative object.


   .. method:: test_integrity(self)

      Test whether all but the last Bars contained in this track are
      full.


   .. method:: transpose(self, interval, up=True)

      Transpose all the notes in the track up or down the interval.
      
      Call transpose() on every Bar.


   .. attribute:: tuning

      Attribute of type: NoneType
      ``None``
----



:doc:`Back to Index</index>`
