#summary Reference documentation for `mingus.core.intervals`.
----
= mingus.core.intervals =
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
== Functions ==
=== `augment_or_diminish_until_the_interval_is_right(note1, note2, interval)` ===
A helper function for the minor and major functions.

You should probably not use this directly.

=== `augmented_unison(note)` ===
=== `determine(note1, note2, shorthand)` ===
  * *Default values*: shorthand = False
Name the interval between note1 and note2.

Examples:
{{{
>>> determine('C', 'E')
'major third'
>>> determine('C', 'Eb')
'minor third'
>>> determine('C', 'E#')
'augmented third'
>>> determine('C', 'Ebb')
'diminished third'
}}}

This works for all intervals. Note that there are corner cases for major
fifths and fourths:
{{{
>>> determine('C', 'G')
'perfect fifth'
>>> determine('C', 'F')
'perfect fourth'
}}}

=== `fifth(note, key)` ===
Take the diatonic fifth of note in key.

Raise a KeyError exception if the note is not found in the given key.

Examples:
{{{
>>> fifth('E', 'C')
'B'
>>> fifth('E', 'F')
'Bb'
}}}

=== `fourth(note, key)` ===
Take the diatonic fourth of note in key.

Raise a KeyError exception if the note is not found in the given key.

Examples:
{{{
>>> fourth('E', 'C')
'A'
>>> fourth('E', 'B')
'A#'
}}}

=== `from_shorthand(note, interval, up)` ===
  * *Default values*: up = True
Return the note on interval up or down.

Examples:
{{{
>>> from_shorthand('A', 'b3')
'C'
>>> from_shorthand('D', '2')
'E'
>>> from_shorthand('E', '2', False)
'D'
}}}

=== `get_interval(note, interval, key)` ===
  * *Default values*: key = 'C'
Return the note an interval (in half notes) away from the given note.

This will produce mostly theoretical sound results, but you should use
the minor and major functions to work around the corner cases.

=== `interval(key, start_note, interval)` ===
Return the note found at the interval starting from start_note in the
given key.

Raise a KeyError exception if start_note is not a valid note.

Example:
{{{
>>> interval('C', 'D', 1)
'E'
}}}

=== `invert(interval)` ===
Invert an interval.

Example:
{{{
>>> invert(['C', 'E'])
['E', 'C']
}}}

=== `is_consonant(note1, note2, include_fourths)` ===
  * *Default values*: include_fourths = True
Return True if the interval is consonant.

A consonance is a harmony, chord, or interval considered stable, as
opposed to a dissonance.

This function tests whether the given interval is consonant. This
basically means that it checks whether the interval is (or sounds like)
a unison, third, sixth, perfect fourth or perfect fifth.

In classical music the fourth is considered dissonant when used
contrapuntal, which is why you can choose to exclude it.

=== `is_dissonant(note1, note2, include_fourths)` ===
  * *Default values*: include_fourths = False
Return True if the insterval is dissonant.

This function tests whether an interval is considered unstable,
dissonant.

In the default case perfect fourths are considered consonant, but this
can be changed by setting exclude_fourths to True.

=== `is_imperfect_consonant(note1, note2)` ===
Return True id the interval is an imperfect consonant one.

Imperfect consonances are either minor or major thirds or minor or major
sixths.

=== `is_perfect_consonant(note1, note2, include_fourths)` ===
  * *Default values*: include_fourths = True
Return True if the interval is a perfect consonant one.

Perfect consonances are either unisons, perfect fourths or fifths, or
octaves (which is the same as a unison in this model).

Perfect fourths are usually included as well, but are considered
dissonant when used contrapuntal, which is why you can exclude them.

=== `major_fifth(note)` ===
=== `major_fourth(note)` ===
=== `major_second(note)` ===
=== `major_seventh(note)` ===
=== `major_sixth(note)` ===
=== `major_third(note)` ===
=== `major_unison(note)` ===
=== `measure(note1, note2)` ===
Return an integer in the range of 0-11, determining the half note steps
between note1 and note2.

Examples:
{{{
>>> measure('C', 'D')
2
>>> measure('D', 'C')
10
}}}

=== `minor_fifth(note)` ===
=== `minor_fourth(note)` ===
=== `minor_second(note)` ===
=== `minor_seventh(note)` ===
=== `minor_sixth(note)` ===
=== `minor_third(note)` ===
=== `minor_unison(note)` ===
=== `perfect_fifth(note)` ===
=== `perfect_fourth(note)` ===
=== `second(note, key)` ===
Take the diatonic second of note in key.

Raise a KeyError exception if the note is not found in the given key.

Examples:
{{{
>>> second('E', 'C')
'F'
>>> second('E', 'D')
'F#'
}}}

=== `seventh(note, key)` ===
Take the diatonic seventh of note in key.

Raise a KeyError exception if the note is not found in the given key.

Examples:
{{{
>>> seventh('E', 'C')
'D'
>>> seventh('E', 'B')
'D#'
}}}

=== `sixth(note, key)` ===
Take the diatonic sixth of note in key.

Raise a KeyError exception if the note is not found in the given key.

Examples:
{{{
>>> sixth('E', 'C')
'C'
>>> sixth('E', 'B')
'C#'
}}}

=== `third(note, key)` ===
Take the diatonic third of note in key.

Raise a KeyError exception if the note is not found in the given key.

Examples:
{{{
>>> third('E', 'C')
'G'
>>> third('E', 'E')
'G#'
}}}

=== `unison(note, key)` ===
  * *Default values*: key = None
Return the unison of note.

Raise a KeyError exception if the note is not found in the given key.

The key is not at all important, but is here for consistency reasons
only.

Example:
{{{
>>> unison('C')
'C'
}}}

----
[mingusIndex Back to Index]
