#summary Reference documentation for `mingus.core.keys`.

----

= mingus.core.keys =
Module for dealing with keys.

This module provides a simple interface for dealing with keys.


----

== Attributes ==
=== `base_scale` ===
  * *Type*: list
  * *Value*: `['C', 'D', 'E', 'F', 'G', 'A', 'B']`

=== `couple` ===
  * *Type*: tuple
  * *Value*: `('C#', 'a#')`

=== `keys` ===
  * *Type*: list
  * *Value*: `[('Cb', 'ab'), ('Gb', 'eb'), ('Db', 'bb'), ('Ab', 'f'), ('Eb', 'c'), ('Bb', 'g'), ('F', 'd'), ('C', 'a'), ('G', 'e'), ('D', 'b'), ('A', 'f#'), ('E', 'c#'), ('B', 'g#'), ('F#', 'd#'), ('C#', 'a#')]`

=== `major_keys` ===
  * *Type*: list
  * *Value*: `['Cb', 'Gb', 'Db', 'Ab', 'Eb', 'Bb', 'F', 'C', 'G', 'D', 'A', 'E', 'B', 'F#', 'C#']`

=== `minor_keys` ===
  * *Type*: list
  * *Value*: `['ab', 'eb', 'bb', 'f', 'c', 'g', 'd', 'a', 'e', 'b', 'f#', 'c#', 'g#', 'd#', 'a#']`


----

== Functions ==
=== `get_key(accidentals)` ===
  * *Default values*: accidentals = 0
Return the key corrisponding to accidentals.

Return the tuple containing the major key corrensponding to the
accidentals put as input, and his relative minor; negative numbers for
flats, positive numbers for sharps.

=== `get_key_signature(key)` ===
  * *Default values*: key = 'C'
Return the key signature.

0 for C or a, negative numbers for flat key signatures, positive numbers
for sharp key signatures.

=== `get_key_signature_accidentals(key)` ===
  * *Default values*: key = 'C'
Return the list of accidentals present into the key signature.

=== `get_notes(key)` ===
  * *Default values*: key = 'C'
Return an ordered list of the notes in this natural key.

Examples:
{{{
>>> get_notes('F')
['F', 'G', 'A', 'Bb', 'C', 'D', 'E']
>>> get_notes('c')
['C', 'D', 'Eb', 'F', 'G', 'Ab', 'Bb']
}}}

=== `is_valid_key(key)` ===
Return True if key is in a recognized format. False if not.

=== `relative_major(key)` ===
Return the relative major of a minor key.

Example:
{{{
>>> relative_major('a')
'C'
}}}

=== `relative_minor(key)` ===
Return the relative minor of a major key.

Example:
{{{
>>> relative_minor('C')
'a'
}}}


----

[mingusIndex Back to Index]
