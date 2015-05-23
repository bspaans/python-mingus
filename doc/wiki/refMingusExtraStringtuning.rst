.. module:: mingus.extra.StringTuning

=========================
mingus.extra.StringTuning
=========================

A class to store and work with tunings and fingerings.


----

.. function:: __init__(self, instrument, description, tuning)

      Create a new StringTuning instance.
      
      The instrument and description parameters should be strings; tuning
      should be a list of strings or a list of lists of strings that
      denote courses.
      
      See tunings.add_tuning for examples.


----

.. function:: count_courses(self)

      Return the average number of courses per string.


----

.. function:: count_strings(self)

      Return the number of strings.


----

.. function:: find_chord_fingering(self, notes, max_distance=4, maxfret=18, max_fingers=4, return_best_as_NoteContainer=False)

      Return a list of fret lists that are considered possible fingerings.
      
      This function only looks at and matches on the note _names_ so it
      does more than find_fingering.
      
      Example:
      
      >>> t = tunings.get_tuning('guitar', 'standard', 6, 1)
      >>> t.find_chord_fingering(NoteContainer().from_chord('Am'))
      [[0, 0, 2, 2, 1, 0], [0, 3, 2, 2, 1, 0], ......]


----

.. function:: find_fingering(self, notes, max_distance=4, not_strings=[])

      Return a list [(string, fret)] of possible fingerings for
      'notes'.
      
      The notes parameter should be a list of strings or Notes or a
      NoteContainer; max_distance denotes the maximum distance between
      frets; not_strings can be used to disclude certain strings and is
      used internally to recurse.
      
      Example:
      
      >>> t = tunings.StringTuning('test', 'test', ['A-3', 'E-4', 'A-5'])
      >>> t.find_fingering(['E-4', 'B-4'])
      [[(0, 7), (1, 7)], [(1, 0), (0, 14)]]


----

.. function:: find_frets(self, note, maxfret=24)

      Return a list with for each string the fret on which the note is
      played or None if it can't be played on that particular string.
      
      The maxfret parameter is the highest fret that can be played; note
      should either be a string or a Note object.
      
      Example:
      
      >>> t = tunings.StringTuning('test', 'test', ['A-3', 'E-4'])
      >>> t.find_frets(Note('C-4')
      [3, None]
      >>> t.find_frets(Note('A-4')
      [12, 5]


----

.. function:: find_note_names(self, notelist, string=0, maxfret=24)

      Return a list [(fret, notename)] in ascending order.
      
      Notelist should be a list of Notes, note-strings or a NoteContainer.
      
      Example:
      
      >>> t = tunings.StringTuning('test', 'test', ['A-3', 'A-4'])
      >>> t.find_note_names(['A', 'C', 'E'], 0, 12)
      [(0, 'E'), (5, 'A'), (8, 'C'), (12, 'E')]


----

.. function:: frets_to_NoteContainer(self, fingering)

      Convert a list such as returned by find_fret to a NoteContainer.


----

.. function:: get_Note(self, string=0, fret=0, maxfret=24)

      Return the Note on 'string', 'fret'.
      
      Throw a RangeError if either the fret or string is unplayable.
      
      Examples:
      
      >>> t = tunings.StringTuning('test', 'test', ['A-3', 'A-4'])
      >>> t,get_Note(0, 0)
      'A-3'
      >>> t.get_Note(0, 1)
      'A#-3'
      >>> t.get_Note(1, 0)
      'A-4'

----



:doc:`Back to Index</index>`
