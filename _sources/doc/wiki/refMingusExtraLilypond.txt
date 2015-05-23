.. module:: mingus.extra.lilypond

=====================
mingus.extra.lilypond
=====================

Functions to generate files in the LilyPond format.

This allows you to create sheet music from some of the objects in
mingus.containers.



----

.. function:: from_Bar(bar, showkey=True, showtime=True)

      Get a Bar object and return the LilyPond equivalent in a string.
      
      The showkey and showtime parameters can be set to determine whether the
      key and the time should be shown.


----

.. function:: from_Composition(composition)

      Return the LilyPond equivalent of a Composition in a string.


----

.. function:: from_Note(note, process_octaves=True, standalone=True)

      Get a Note object and return the LilyPond equivalent in a string.
      
      If process_octaves is set to False, all data regarding octaves will be
      ignored. If standalone is True, the result can be used by functions
      like to_png and will produce a valid output. The argument is mostly here
      to let from_NoteContainer make use of this function.


----

.. function:: from_NoteContainer(nc, duration=None, standalone=True)

      Get a NoteContainer object and return the LilyPond equivalent in a
      string.
      
      The second argument determining the duration of the NoteContainer is
      optional. When the standalone argument is True the result of this
      function can be used directly by functions like to_png. It is mostly
      here to be used by from_Bar.


----

.. function:: from_Suite(suite)


----

.. function:: from_Track(track)

      Process a Track object and return the LilyPond equivalent in a string.


----

.. function:: save_string_and_execute_LilyPond(ly_string, filename, command)

      A helper function for to_png and to_pdf. Should not be used directly.


----

.. function:: to_pdf(ly_string, filename)

      Save a string in LilyPond format to a PDF.
      
      LilyPond in the $PATH is needed.


----

.. function:: to_png(ly_string, filename)

      Save a string in LilyPond format to a PNG.
      
      LilyPond in the $PATH is needed.

----



:doc:`Back to Index</index>`
