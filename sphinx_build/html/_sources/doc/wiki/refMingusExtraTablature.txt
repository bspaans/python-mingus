======================
mingus.extra.tablature
======================

Functions to convert mingus.containers to pretty ASCII tablature.

Attributes
----------

default_tuning
^^^^^^^^^^^^^^

  * *Type*: mingus.extra.tunings.StringTuning
  * *Value*: `<mingus.extra.tunings.StringTuning object at 0x7f3cd5da3e90>`

----

Functions
---------

_get_qsize(tuning, width)
^^^^^^^^^^^^^^^^^^^^^^^^^

Return a reasonable quarter note size for 'tuning' and 'width'.

_get_width(maxwidth)
^^^^^^^^^^^^^^^^^^^^

Return the width of a single bar, when width of the page is given.

add_headers(width, title, subtitle, author, email, description, tunings)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  * *Default values*: width = 80, title = 'Untitled', subtitle = '', author = '', email = '', description = '', tunings = []
Create a nice header in the form of a list of strings using the
information that has been filled in.

All arguments except 'width' and 'tunings' should be strings. 'width'
should be an integer and 'tunings' a list of tunings representing the
instruments.

begin_track(tuning, padding)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  * *Default values*: padding = 2
Helper function that builds the first few characters of every bar.

from_Bar(bar, width, tuning, collapse)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  * *Default values*: width = 40, tuning = None, collapse = True
Convert a mingus.containers.Bar object to ASCII tablature.

Throw a FingerError if no playable fingering can be found.

'tuning' should be a StringTuning object or None for the default tuning.
If 'collapse' is False this will return a list of lines, if it's True
all lines will be concatenated with a newline symbol.

Use 'string' and 'fret' attributes on Notes to force certain fingerings.

from_Composition(composition, width)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  * *Default values*: width = 80
Convert a mingus.containers.Composition to an ASCII tablature string.

Automatically add an header based on the title, subtitle, author, e-mail
and description attributes. An extra description of the piece can also
be given.

Tunings can be set by using the Track.instrument.tuning or Track.tuning
attribute.

from_Note(note, width, tuning)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  * *Default values*: width = 80, tuning = None
Return a string made out of ASCII tablature representing a Note object
or note string.

Throw a RangeError if a suitable fret can't be found.

'tuning' should be a StringTuning object or None for the default tuning.

To force a certain fingering you can use a 'string' and 'fret' attribute
on the Note. If the fingering is valid, it will get used instead of the
default one.

from_NoteContainer(notes, width, tuning)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  * *Default values*: width = 80, tuning = None
Return a string made out of ASCII tablature representing a
NoteContainer object or list of note strings / Note objects.

Throw a FingerError if no playable fingering can be found.

'tuning' should be a StringTuning object or None for the default tuning.

To force a certain fingering you can use a 'string' and 'fret' attribute
on one or more of the Notes. If the fingering is valid, it will get used
instead of the default one.

from_Suite(suite, maxwidth)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

  * *Default values*: maxwidth = 80
Convert a mingus.containers.Suite to an ASCII tablature string, complete
with headers.

This function makes use of the Suite's title, subtitle, author, email
and description attributes.

from_Track(track, maxwidth, tuning)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  * *Default values*: maxwidth = 80, tuning = None
Convert a mingus.containers.Track object to an ASCII tablature string.

'tuning' should be set to a StringTuning object or to None to use the
Track's tuning (or alternatively the default if the Track hasn't got its
own tuning).

'string' and 'fret' attributes on Notes are taken into account.

----

:doc:`Back to Index</index>`
