.. module:: mingus.core.progressions

========================
mingus.core.progressions
========================

Module for dealing with progressions.

In music and music theory you often deal with sequencesi of chords. These
chord sequences are called progressions and are often written down using
roman numerals. In this system the 'I' refers to the first natural triad in
a key, the II to the second, etc. We can add prefixes and suffixes to denote
more complex progressions, like: #V7, bIIdim7, etc.

This module provides methods which can convert progressions to chords and
vice versa.



----

.. data:: numeral_intervals

      Attribute of type: list
      ``[0, 2, 4, 5, 7, 9, 11]``

----

.. data:: numerals

      Attribute of type: list
      ``['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']``

----

.. function:: determine(chord, key, shorthand=False)

      Determine the harmonic function of chord in key.
      
      This function can also deal with lists of chords.
      
      Examples:
      
      >>> determine(['C', 'E', 'G'], 'C')
      ['tonic']
      >>> determine(['G', 'B', 'D'], 'C')
      ['dominant']
      >>> determine(['G', 'B', 'D', 'F'], 'C', True)
      ['V7']
      >>> determine([['C', 'E', 'G'], ['G', 'B', 'D']], 'C', True)
      [['I'], ['V']]


----

.. function:: interval_diff(progression1, progression2, interval)

      Return the number of half steps progression2 needs to be diminished or
      augmented until the interval between progression1 and progression2 is
      interval.


----

.. function:: parse_string(progression)

      Return a tuple (roman numeral, accidentals, chord suffix).
      
      Examples:
      
      >>> parse_string('I')
      ('I', 0, '')
      >>> parse_string('bIM7')
      ('I', -1, 'M7')


----

.. function:: skip(roman_numeral, skip=1)

      Skip the given places to the next roman numeral.
      
      Examples:
      
      >>> skip('I')
      'II'
      >>> skip('VII')
      'I'
      >>> skip('I', 2)
      'III'


----

.. function:: substitute(progression, substitute_index, depth=0)

      Give a list of possible substitutions for progression[substitute_index].
      
      If depth > 0 the substitutions of each result will be recursively added
      as well.
      
      Example:
      
      >>> substitute(['I', 'IV', 'V', 'I'], 0)
      ['III', 'III7', 'VI', 'VI7', 'I7']


----

.. function:: substitute_diminished_for_diminished(progression, substitute_index, ignore_suffix=False)

      Substitute a diminished chord for another diminished chord.
      
      'dim' and 'dim7' suffixes recognized, and 'VI' if there is no suffix.
      
      Example:
      
      >>> substitute_diminished_for_diminished(['VII'], 0)
      ['IIdim', 'bIVdim', 'bbVIdim']


----

.. function:: substitute_diminished_for_dominant(progression, substitute_index, ignore_suffix=False)


----

.. function:: substitute_harmonic(progression, substitute_index, ignore_suffix=False)

      Do simple harmonic substitutions. Return a list of possible substitions
      for progression[substitute_index].
      
      If ignore_suffix is set to True the suffix of the chord being
      substituted will be ignored. Otherwise only progressions without a
      suffix, or with suffix '7' will be substituted.
      
      The following table is used to convert progressions:
      || I || III ||
      || I || VI ||
      || IV || II ||
      || IV || VI ||
      || V || VII ||


----

.. function:: substitute_major_for_minor(progression, substitute_index, ignore_suffix=False)

      Substitute major chords for their minor equivalent.
      
      'M' and 'M7' suffixes recognized, and ['I', 'IV', 'V'] if there is no
      suffix.
      
      Examples:
      
      >>> substitute_major_for_minor(['I'], 0)
      ['VI']
      >>> substitute_major_for_minor(['VM7'], 0)
      ['IIIm7']


----

.. function:: substitute_minor_for_major(progression, substitute_index, ignore_suffix=False)

      Substitute minor chords for its major equivalent.
      
      'm' and 'm7' suffixes recognized, and ['II', 'III', 'VI'] if there is no
      suffix.
      
      Examples:
      
      >>> substitute_minor_for_major(['VI'], 0)
      ['I']
      >>> substitute_minor_for_major(['Vm'], 0)
      ['bVIIM']
      >>> substitute_minor_for_major(['VIm7'], 0)
      ['IM7']


----

.. function:: to_chords(progression, key=C)

      Convert a list of chord functions or a string to a list of chords.
      
      Examples:
      
      >>> to_chords(['I', 'V7'])
      [['C', 'E', 'G'], ['G', 'B', 'D', 'F']]
      >>> to_chords('I7')
      [['C', 'E', 'G', 'B']]
      
      Any number of accidentals can be used as prefix to augment or diminish;
      for example: bIV or #I.
      
      All the chord abbreviations in the chord module can be used as suffixes;
      for example: Im7, IVdim7, etc.
      
      You can combine prefixes and suffixes to manage complex progressions:
      #vii7, #iidim7, iii7, etc.
      
      Using 7 as suffix is ambiguous, since it is classicly used to denote the
      seventh chord when talking about progressions instead of just the
      dominant seventh chord. We have taken the classic route; I7 will get
      you a major seventh chord. If you specifically want a dominanth seventh,
      use Idom7.


----

.. function:: tuple_to_string(prog_tuple)

      Create a string from tuples returned by parse_string.

----



:doc:`Back to Index</index>`
