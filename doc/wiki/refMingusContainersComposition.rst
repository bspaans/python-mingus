.. module:: mingus.containers.composition

=============================
mingus.containers.composition
=============================


.. class:: Composition


   .. method:: __add__(self, value)

      Enable the '+' operator for Compositions.
      
      Notes, note strings, NoteContainers, Bars and Tracks are accepted.


   .. method:: __getitem__(self, index)

      Enable the '[]' notation.


   .. method:: __init__(self)


   .. method:: __len__(self)

      Enable the len() function.


   .. method:: __repr__(self)

      Return a string representing the class.


   .. method:: __setitem__(self, index, value)

      Enable the '[] =' notation.


   .. method:: add_note(self, note)

      Add a note to the selected tracks.
      
      Everything container.Track supports in __add__ is accepted.


   .. method:: add_track(self, track)

      Add a track to the composition.
      
      Raise an UnexpectedObjectError if the argument is not a
      mingus.containers.Track object.


   .. attribute:: author

      Attribute of type: str
      ``''``

   .. attribute:: description

      Attribute of type: str
      ``''``

   .. attribute:: email

      Attribute of type: str
      ``''``

   .. method:: empty(self)

      Remove all the tracks from this class.


   .. method:: reset(self)

      Reset the information in this class.
      
      Remove the track and composer information.


   .. attribute:: selected_tracks

      Attribute of type: list
      ``[]``

   .. method:: set_author(self, author=, email=)

      Set the title and author of the piece.


   .. method:: set_title(self, title=Untitled, subtitle=)

      Set the title and subtitle of the piece.


   .. attribute:: subtitle

      Attribute of type: str
      ``''``

   .. attribute:: title

      Attribute of type: str
      ``'Untitled'``

   .. attribute:: tracks

      Attribute of type: list
      ``[]``
----



:doc:`Back to Index</index>`
