====================
mingus.extra.tunings
====================

Dozens of standard tunings, a StringTuning class and some functions to help
you search through them.


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
