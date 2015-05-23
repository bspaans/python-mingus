.. module:: mingus.core.intervals

=====================
mingus.core.intervals
=====================

Module to create intervals from notes.

When you are working in a key (for instance 'F'), you can use the functions
second ('G'), third ('A'), fourth ('Bb'), fifth ('C'), sixth ('D') and
seventh ('E') to get to the respective natural intervals of that note.

When you want to get the absolute intervals you can use the minor and major
functions. For example: minor_third('F') returns 'Ab' while major_third('F')
returns 'A'.

This modules also contains other useful helper functions like measure,
determine, invert, is_consonant and is_dissonant.



----

.. function:: augment_or_diminish_until_the_interval_is_right(note1, note2, interval)

      A helper function for the minor and major functions.
      
      You should probably not use this directly.


----

.. function:: augmented_unison(note)


----

.. function:: determine(note1, note2, shorthand=False)

      Name the interval between note1 and note2.
      
      Examples:
      
      >>> determine('C', 'E')
      'major third'
      >>> determine('C', 'Eb')
      'minor third'
      >>> determine('C', 'E#')
      'augmented third'
      >>> determine('C', 'Ebb')
      'diminished third'
      
      This works for all intervals. Note that there are corner cases for major
      fifths and fourths:
      >>> determine('C', 'G')
      'perfect fifth'
      >>> determine('C', 'F')
      'perfect fourth'


----

.. function:: fifth(note, key)

      Take the diatonic fifth of note in key.
      
      Raise a KeyError exception if the note is not found in the given key.
      
      Examples:
      
      >>> fifth('E', 'C')
      'B'
      >>> fifth('E', 'F')
      'Bb'


----

.. function:: fourth(note, key)

      Take the diatonic fourth of note in key.
      
      Raise a KeyError exception if the note is not found in the given key.
      
      Examples:
      
      >>> fourth('E', 'C')
      'A'
      >>> fourth('E', 'B')
      'A#'


----

.. function:: from_shorthand(note, interval, up=True)

      Return the note on interval up or down.
      
      Examples:
      
      >>> from_shorthand('A', 'b3')
      'C'
      >>> from_shorthand('D', '2')
      'E'
      >>> from_shorthand('E', '2', False)
      'D'


----

.. function:: get_interval(note, interval, key=C)

      Return the note an interval (in half notes) away from the given note.
      
      This will produce mostly theoretical sound results, but you should use
      the minor and major functions to work around the corner cases.


----

.. function:: interval(key, start_note, interval)

      Return the note found at the interval starting from start_note in the
      given key.
      
      Raise a KeyError exception if start_note is not a valid note.
      
      Example:
      
      >>> interval('C', 'D', 1)
      'E'


----

.. function:: invert(interval)

      Invert an interval.
      
      Example:
      
      >>> invert(['C', 'E'])
      ['E', 'C']


----

.. function:: is_consonant(note1, note2, include_fourths=True)

      Return True if the interval is consonant.
      
      A consonance is a harmony, chord, or interval considered stable, as
      opposed to a dissonance.
      
      This function tests whether the given interval is consonant. This
      basically means that it checks whether the interval is (or sounds like)
      a unison, third, sixth, perfect fourth or perfect fifth.
      
      In classical music the fourth is considered dissonant when used
      contrapuntal, which is why you can choose to exclude it.


----

.. function:: is_dissonant(note1, note2, include_fourths=False)

      Return True if the insterval is dissonant.
      
      This function tests whether an interval is considered unstable,
      dissonant.
      
      In the default case perfect fourths are considered consonant, but this
      can be changed by setting exclude_fourths to True.


----

.. function:: is_imperfect_consonant(note1, note2)

      Return True id the interval is an imperfect consonant one.
      
      Imperfect consonances are either minor or major thirds or minor or major
      sixths.


----

.. function:: is_perfect_consonant(note1, note2, include_fourths=True)

      Return True if the interval is a perfect consonant one.
      
      Perfect consonances are either unisons, perfect fourths or fifths, or
      octaves (which is the same as a unison in this model).
      
      Perfect fourths are usually included as well, but are considered
      dissonant when used contrapuntal, which is why you can exclude them.


----

.. function:: major_fifth(note)


----

.. function:: major_fourth(note)


----

.. function:: major_second(note)


----

.. function:: major_seventh(note)


----

.. function:: major_sixth(note)


----

.. function:: major_third(note)


----

.. function:: major_unison(note)


----

.. function:: measure(note1, note2)

      Return an integer in the range of 0-11, determining the half note steps
      between note1 and note2.
      
      Examples:
      
      >>> measure('C', 'D')
      2
      >>> measure('D', 'C')
      10


----

.. function:: minor_fifth(note)


----

.. function:: minor_fourth(note)


----

.. function:: minor_second(note)


----

.. function:: minor_seventh(note)


----

.. function:: minor_sixth(note)


----

.. function:: minor_third(note)


----

.. function:: minor_unison(note)


----

.. function:: perfect_fifth(note)


----

.. function:: perfect_fourth(note)


----

.. function:: second(note, key)

      Take the diatonic second of note in key.
      
      Raise a KeyError exception if the note is not found in the given key.
      
      Examples:
      
      >>> second('E', 'C')
      'F'
      >>> second('E', 'D')
      'F#'


----

.. function:: seventh(note, key)

      Take the diatonic seventh of note in key.
      
      Raise a KeyError exception if the note is not found in the given key.
      
      Examples:
      
      >>> seventh('E', 'C')
      'D'
      >>> seventh('E', 'B')
      'D#'


----

.. function:: sixth(note, key)

      Take the diatonic sixth of note in key.
      
      Raise a KeyError exception if the note is not found in the given key.
      
      Examples:
      
      >>> sixth('E', 'C')
      'C'
      >>> sixth('E', 'B')
      'C#'


----

.. function:: third(note, key)

      Take the diatonic third of note in key.
      
      Raise a KeyError exception if the note is not found in the given key.
      
      Examples:
      
      >>> third('E', 'C')
      'G'
      >>> third('E', 'E')
      'G#'


----

.. function:: unison(note, key=None)

      Return the unison of note.
      
      Raise a KeyError exception if the note is not found in the given key.
      
      The key is not at all important, but is here for consistency reasons
      only.
      
      Example:
      
      >>> unison('C')
      'C'

----



:doc:`Back to Index</index>`
