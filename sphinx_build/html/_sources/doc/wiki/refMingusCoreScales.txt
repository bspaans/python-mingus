==================
mingus.core.scales
==================

Module for dealing with scales.

The scales module allows you to create a plethora of scales. Here's a
little overview:

The diatonic scales
 * Diatonic(note, semitones)

Ancient scales
 * Ionian(note)
 * Dorian(note)
 * Phrygian(note)
 * Lydian(note)
 * Mixolydian(note)
 * Aeolian(note)
 * Locrian(note)

The major scales
 * Major(note)
 * HarmonicMajor(note)

The minor scales
 * NaturalMinor(note)
 * HarmonicMinor(note)
 * MelodicMinor(note)
 * Bachian(note)
 * MinorNeapolitan(note)

Other scales
 * Chromatic(note)
 * WholeTone(note)
 * Octatonic(note)


Attributes
----------

keys
^^^^

  * *Type*: list
  * *Value*: `[('Cb', 'ab'), ('Gb', 'eb'), ('Db', 'bb'), ('Ab', 'f'), ('Eb', 'c'), ('Bb', 'g'), ('F', 'd'), ('C', 'a'), ('G', 'e'), ('D', 'b'), ('A', 'f#'), ('E', 'c#'), ('B', 'g#'), ('F#', 'd#'), ('C#', 'a#')]`

----

Functions
---------

augment(note)
^^^^^^^^^^^^^

Augment a given note.

Examples:
>>> augment('C')
'C#'
>>> augment('Cb')
'C'

determine(notes)
^^^^^^^^^^^^^^^^

Determine the scales containing the notes.

All major and minor scales are recognized.

Example:
>>> determine(['A', 'Bb', 'E', 'F#', 'G'])
['G melodic minor', 'G Bachian', 'D harmonic major']

diminish(note)
^^^^^^^^^^^^^^

Diminish a given note.

Examples:
>>> diminish('C')
'Cb'
>>> diminish('C#')
'C'

get_notes(key)
^^^^^^^^^^^^^^

  * *Default values*: key = 'C'
Return an ordered list of the notes in this natural key.

Examples:
>>> get_notes('F')
['F', 'G', 'A', 'Bb', 'C', 'D', 'E']
>>> get_notes('c')
['C', 'D', 'Eb', 'F', 'G', 'Ab', 'Bb']

reduce_accidentals(note)
^^^^^^^^^^^^^^^^^^^^^^^^

Reduce any extra accidentals to proper notes.

Example:
>>> reduce_accidentals('C####')
'E'

----

:doc:`Back to Index</index>`
