.. module:: mingus.containers.suite

=======================
mingus.containers.suite
=======================


.. class:: Suite


   .. method:: __add__(self, composition)

      Enable the '+' operator for Compositions.


   .. method:: __getitem__(self, index)

      Enable the '[]' notation.


   .. method:: __init__(self)


   .. method:: __len__(self)

      Enable the len() function.


   .. method:: __setitem__(self, index, value)

      Enable the '[] =' notation.


   .. method:: add_composition(self, composition)

      Add a composition to the suite.
      
      Raise an UnexpectedObjectError when the supplied argument is not a
      Composition object.


   .. attribute:: author

      Attribute of type: str
      ``''``

   .. attribute:: compositions

      Attribute of type: list
      ``[]``

   .. attribute:: description

      Attribute of type: str
      ``''``

   .. attribute:: email

      Attribute of type: str
      ``''``

   .. method:: set_author(self, author, email=)

      Set the author of the suite.


   .. method:: set_title(self, title, subtitle=)

      Set the title and the subtitle of the suite.


   .. attribute:: subtitle

      Attribute of type: str
      ``''``

   .. attribute:: title

      Attribute of type: str
      ``'Untitled'``
----



:doc:`Back to Index</index>`
