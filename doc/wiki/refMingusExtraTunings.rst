.. module:: mingus.extra.tunings

====================
mingus.extra.tunings
====================

Dozens of standard tunings, a StringTuning class and some functions to help
you search through them.


.. class:: StringTuning


   .. method:: __init__(self, instrument, description, tuning)

      Create a new StringTuning instance.
      
      The instrument and description parameters should be strings; tuning
      should be a list of strings or a list of lists of strings that
      denote courses.
      
      See tunings.add_tuning for examples.


   .. method:: count_courses(self)

      Return the average number of courses per string.


   .. method:: count_strings(self)

      Return the number of strings.


   .. method:: find_chord_fingering(self, notes, max_distance=4, maxfret=18, max_fingers=4, return_best_as_NoteContainer=False)

      Return a list of fret lists that are considered possible fingerings.
      
      This function only looks at and matches on the note _names_ so it
      does more than find_fingering.
      
      Example:
      
      >>> t = tunings.get_tuning('guitar', 'standard', 6, 1)
      >>> t.find_chord_fingering(NoteContainer().from_chord('Am'))
      [[0, 0, 2, 2, 1, 0], [0, 3, 2, 2, 1, 0], ......]


   .. method:: find_fingering(self, notes, max_distance=4, not_strings=[])

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


   .. method:: find_frets(self, note, maxfret=24)

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


   .. method:: find_note_names(self, notelist, string=0, maxfret=24)

      Return a list [(fret, notename)] in ascending order.
      
      Notelist should be a list of Notes, note-strings or a NoteContainer.
      
      Example:
      
      >>> t = tunings.StringTuning('test', 'test', ['A-3', 'A-4'])
      >>> t.find_note_names(['A', 'C', 'E'], 0, 12)
      [(0, 'E'), (5, 'A'), (8, 'C'), (12, 'E')]


   .. method:: frets_to_NoteContainer(self, fingering)

      Convert a list such as returned by find_fret to a NoteContainer.


   .. method:: get_Note(self, string=0, fret=0, maxfret=24)

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

.. function:: add_tuning(instrument, description, tuning)

      Add a new tuning to the index.
      
      The instrument and description parameters should be strings; tuning
      should be a list of strings or a list of lists to denote courses.
      
      Example:
      
      >>> std_strings = ['E-2', 'A-2', 'D-3', 'G-3', 'B-3', 'E-4']
      >>> tuning.add_tuning('Guitar', 'standard', std_strings)
      >>> tw_strings = [['E-2', 'E-3'], ['A-2', 'A-3'], ...........]
      >>> tuning.add_tuning('Guitar', 'twelve string', tw_string)


----

.. function:: fingers_needed(fingering)

      Return the number of fingers needed to play the given fingering.


----

.. function:: get_instruments()

      Return a sorted list of instruments that have string tunings defined
      for them.


----

.. function:: get_tuning(instrument, description, nr_of_strings=None, nr_of_courses=None)

      Get the first tuning that satisfies the constraints.
      
      The instrument and description arguments are treated like
      case-insensitive prefixes. So search for 'bass' is the same is
      'Bass Guitar'.
      
      Example:
      
      >>> tunings.get_tuning('guitar', 'standard')
      <tunings.StringTuning instance at 0x139ac20>


----

.. function:: get_tunings(instrument=None, nr_of_strings=None, nr_of_courses=None)

      Search tunings on instrument, strings, courses or a combination.
      
      The instrument is actually treated like a case-insensitive prefix. So
      asking for 'bass' yields the same tunings as 'Bass Guitar'; the string
      'ba' yields all the instruments starting with 'ba'.
      
      Example:
      
      >>> tunings.get_tunings(nr_of_string = 4)
      >>> tunings.get_tunings('bass')

----



:doc:`Back to Index</index>`
