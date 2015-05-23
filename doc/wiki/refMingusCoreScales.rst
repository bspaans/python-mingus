.. module:: mingus.core.scales

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



.. class:: Aeolian


   .. method:: __eq__(self, other)


   .. method:: __init__(self, note, octaves=1)

      Create the aeolian mode scale starting on the chosen note.


   .. method:: __len__(self)


   .. method:: __ne__(self, other)


   .. method:: __repr__(self)


   .. method:: __str__(self)


   .. method:: ascending(self)


   .. method:: degree(self, degree_number, direction=a)

      Return the asked scale degree.
      
      The direction of the scale is 'a' for ascending (default) and 'd'
      for descending.


   .. method:: descending(self)

      Return the list of descending notes.


   .. attribute:: type

      Attribute of type: str
      ``'ancient'``

.. class:: Bachian


   .. method:: __eq__(self, other)


   .. method:: __init__(self, note, octaves=1)

      Create the Bachian (also known as "real melodic minor" and "jazz")
      scale starting on the chosen note.


   .. method:: __len__(self)


   .. method:: __ne__(self, other)


   .. method:: __repr__(self)


   .. method:: __str__(self)


   .. method:: ascending(self)


   .. method:: degree(self, degree_number, direction=a)

      Return the asked scale degree.
      
      The direction of the scale is 'a' for ascending (default) and 'd'
      for descending.


   .. method:: descending(self)

      Return the list of descending notes.


   .. attribute:: type

      Attribute of type: str
      ``'minor'``

.. class:: Chromatic


   .. method:: __eq__(self, other)


   .. method:: __init__(self, key, octaves=1)

      Create the chromatic scale in the chosen key.


   .. method:: __len__(self)


   .. method:: __ne__(self, other)


   .. method:: __repr__(self)


   .. method:: __str__(self)


   .. method:: ascending(self)


   .. method:: degree(self, degree_number, direction=a)

      Return the asked scale degree.
      
      The direction of the scale is 'a' for ascending (default) and 'd'
      for descending.


   .. method:: descending(self)


   .. attribute:: type

      Attribute of type: str
      ``'other'``

.. class:: Diatonic


   .. method:: __eq__(self, other)


   .. method:: __init__(self, note, semitones, octaves=1)

      Create the diatonic scale starting on the chosen note.
      
      The second parameter is a tuple representing the position of
      semitones.


   .. method:: __len__(self)


   .. method:: __ne__(self, other)


   .. method:: __repr__(self)


   .. method:: __str__(self)


   .. method:: ascending(self)


   .. method:: degree(self, degree_number, direction=a)

      Return the asked scale degree.
      
      The direction of the scale is 'a' for ascending (default) and 'd'
      for descending.


   .. method:: descending(self)

      Return the list of descending notes.


   .. attribute:: type

      Attribute of type: str
      ``'diatonic'``

.. class:: Dorian


   .. method:: __eq__(self, other)


   .. method:: __init__(self, note, octaves=1)

      Create the dorian mode scale starting on the chosen note.


   .. method:: __len__(self)


   .. method:: __ne__(self, other)


   .. method:: __repr__(self)


   .. method:: __str__(self)


   .. method:: ascending(self)


   .. method:: degree(self, degree_number, direction=a)

      Return the asked scale degree.
      
      The direction of the scale is 'a' for ascending (default) and 'd'
      for descending.


   .. method:: descending(self)

      Return the list of descending notes.


   .. attribute:: type

      Attribute of type: str
      ``'ancient'``

.. class:: HarmonicMajor


   .. method:: __eq__(self, other)


   .. method:: __init__(self, note, octaves=1)

      Create the harmonic major scale starting on the chosen note.


   .. method:: __len__(self)


   .. method:: __ne__(self, other)


   .. method:: __repr__(self)


   .. method:: __str__(self)


   .. method:: ascending(self)


   .. method:: degree(self, degree_number, direction=a)

      Return the asked scale degree.
      
      The direction of the scale is 'a' for ascending (default) and 'd'
      for descending.


   .. method:: descending(self)

      Return the list of descending notes.


   .. attribute:: type

      Attribute of type: str
      ``'major'``

.. class:: HarmonicMinor


   .. method:: __eq__(self, other)


   .. method:: __init__(self, note, octaves=1)

      Create the harmonic minor scale starting on the chosen note.


   .. method:: __len__(self)


   .. method:: __ne__(self, other)


   .. method:: __repr__(self)


   .. method:: __str__(self)


   .. method:: ascending(self)


   .. method:: degree(self, degree_number, direction=a)

      Return the asked scale degree.
      
      The direction of the scale is 'a' for ascending (default) and 'd'
      for descending.


   .. method:: descending(self)

      Return the list of descending notes.


   .. attribute:: type

      Attribute of type: str
      ``'minor'``

.. class:: Ionian


   .. method:: __eq__(self, other)


   .. method:: __init__(self, note, octaves=1)

      Create the ionian mode scale starting on the chosen note.


   .. method:: __len__(self)


   .. method:: __ne__(self, other)


   .. method:: __repr__(self)


   .. method:: __str__(self)


   .. method:: ascending(self)


   .. method:: degree(self, degree_number, direction=a)

      Return the asked scale degree.
      
      The direction of the scale is 'a' for ascending (default) and 'd'
      for descending.


   .. method:: descending(self)

      Return the list of descending notes.


   .. attribute:: type

      Attribute of type: str
      ``'ancient'``

.. class:: Locrian


   .. method:: __eq__(self, other)


   .. method:: __init__(self, note, octaves=1)

      Create the locrian mode scale starting on the chosen note.


   .. method:: __len__(self)


   .. method:: __ne__(self, other)


   .. method:: __repr__(self)


   .. method:: __str__(self)


   .. method:: ascending(self)


   .. method:: degree(self, degree_number, direction=a)

      Return the asked scale degree.
      
      The direction of the scale is 'a' for ascending (default) and 'd'
      for descending.


   .. method:: descending(self)

      Return the list of descending notes.


   .. attribute:: type

      Attribute of type: str
      ``'ancient'``

.. class:: Lydian


   .. method:: __eq__(self, other)


   .. method:: __init__(self, note, octaves=1)

      Create the lydian mode scale starting on the chosen note.


   .. method:: __len__(self)


   .. method:: __ne__(self, other)


   .. method:: __repr__(self)


   .. method:: __str__(self)


   .. method:: ascending(self)


   .. method:: degree(self, degree_number, direction=a)

      Return the asked scale degree.
      
      The direction of the scale is 'a' for ascending (default) and 'd'
      for descending.


   .. method:: descending(self)

      Return the list of descending notes.


   .. attribute:: type

      Attribute of type: str
      ``'ancient'``

.. class:: Major


   .. method:: __eq__(self, other)


   .. method:: __init__(self, note, octaves=1)

      Create the major scale starting on the chosen note.


   .. method:: __len__(self)


   .. method:: __ne__(self, other)


   .. method:: __repr__(self)


   .. method:: __str__(self)


   .. method:: ascending(self)


   .. method:: degree(self, degree_number, direction=a)

      Return the asked scale degree.
      
      The direction of the scale is 'a' for ascending (default) and 'd'
      for descending.


   .. method:: descending(self)

      Return the list of descending notes.


   .. attribute:: type

      Attribute of type: str
      ``'major'``

.. class:: MelodicMinor


   .. method:: __eq__(self, other)


   .. method:: __init__(self, note, octaves=1)

      Create the melodic minor scale starting on the chosen note.


   .. method:: __len__(self)


   .. method:: __ne__(self, other)


   .. method:: __repr__(self)


   .. method:: __str__(self)


   .. method:: ascending(self)


   .. method:: degree(self, degree_number, direction=a)

      Return the asked scale degree.
      
      The direction of the scale is 'a' for ascending (default) and 'd'
      for descending.


   .. method:: descending(self)


   .. attribute:: type

      Attribute of type: str
      ``'minor'``

.. class:: MinorNeapolitan


   .. method:: __eq__(self, other)


   .. method:: __init__(self, note, octaves=1)

      Create the minor Neapolitan scale starting on the chosen note.


   .. method:: __len__(self)


   .. method:: __ne__(self, other)


   .. method:: __repr__(self)


   .. method:: __str__(self)


   .. method:: ascending(self)


   .. method:: degree(self, degree_number, direction=a)

      Return the asked scale degree.
      
      The direction of the scale is 'a' for ascending (default) and 'd'
      for descending.


   .. method:: descending(self)


   .. attribute:: type

      Attribute of type: str
      ``'minor'``

.. class:: Mixolydian


   .. method:: __eq__(self, other)


   .. method:: __init__(self, note, octaves=1)

      Create the mixolydian mode scale starting on the chosen note.


   .. method:: __len__(self)


   .. method:: __ne__(self, other)


   .. method:: __repr__(self)


   .. method:: __str__(self)


   .. method:: ascending(self)


   .. method:: degree(self, degree_number, direction=a)

      Return the asked scale degree.
      
      The direction of the scale is 'a' for ascending (default) and 'd'
      for descending.


   .. method:: descending(self)

      Return the list of descending notes.


   .. attribute:: type

      Attribute of type: str
      ``'ancient'``

.. class:: NaturalMinor


   .. method:: __eq__(self, other)


   .. method:: __init__(self, note, octaves=1)

      Return the natural minor scale starting on the chosen note.


   .. method:: __len__(self)


   .. method:: __ne__(self, other)


   .. method:: __repr__(self)


   .. method:: __str__(self)


   .. method:: ascending(self)


   .. method:: degree(self, degree_number, direction=a)

      Return the asked scale degree.
      
      The direction of the scale is 'a' for ascending (default) and 'd'
      for descending.


   .. method:: descending(self)

      Return the list of descending notes.


   .. attribute:: type

      Attribute of type: str
      ``'minor'``

.. class:: Octatonic


   .. method:: __eq__(self, other)


   .. method:: __init__(self, note, octaves=1)

      Create the octatonic (also known as "diminshed") scale starting
      on the chosen note.


   .. method:: __len__(self)


   .. method:: __ne__(self, other)


   .. method:: __repr__(self)


   .. method:: __str__(self)


   .. method:: ascending(self)


   .. method:: degree(self, degree_number, direction=a)

      Return the asked scale degree.
      
      The direction of the scale is 'a' for ascending (default) and 'd'
      for descending.


   .. method:: descending(self)

      Return the list of descending notes.


   .. attribute:: type

      Attribute of type: str
      ``'other'``

.. class:: Phrygian


   .. method:: __eq__(self, other)


   .. method:: __init__(self, note, octaves=1)

      Create the phrygian mode scale starting on the chosen note.


   .. method:: __len__(self)


   .. method:: __ne__(self, other)


   .. method:: __repr__(self)


   .. method:: __str__(self)


   .. method:: ascending(self)


   .. method:: degree(self, degree_number, direction=a)

      Return the asked scale degree.
      
      The direction of the scale is 'a' for ascending (default) and 'd'
      for descending.


   .. method:: descending(self)

      Return the list of descending notes.


   .. attribute:: type

      Attribute of type: str
      ``'ancient'``

.. class:: WholeTone


   .. method:: __eq__(self, other)


   .. method:: __init__(self, note, octaves=1)

      Create the whole tone scale starting on the chosen note.


   .. method:: __len__(self)


   .. method:: __ne__(self, other)


   .. method:: __repr__(self)


   .. method:: __str__(self)


   .. method:: ascending(self)


   .. method:: degree(self, degree_number, direction=a)

      Return the asked scale degree.
      
      The direction of the scale is 'a' for ascending (default) and 'd'
      for descending.


   .. method:: descending(self)

      Return the list of descending notes.


   .. attribute:: type

      Attribute of type: str
      ``'other'``

.. class:: _Scale


   .. method:: __eq__(self, other)


   .. method:: __init__(self, note, octaves)


   .. method:: __len__(self)


   .. method:: __ne__(self, other)


   .. method:: __repr__(self)


   .. method:: __str__(self)


   .. method:: ascending(self)

      Return the list of ascending notes.


   .. method:: degree(self, degree_number, direction=a)

      Return the asked scale degree.
      
      The direction of the scale is 'a' for ascending (default) and 'd'
      for descending.


   .. method:: descending(self)

      Return the list of descending notes.


----

.. data:: keys

      Attribute of type: list
      ``[('Cb', 'ab'), ('Gb', 'eb'), ('Db', 'bb'), ('Ab', 'f'), ('Eb', 'c'), ('Bb', 'g'), ('F', 'd'), ('C', 'a'), ('G', 'e'), ('D', 'b'), ('A', 'f#'), ('E', 'c#'), ('B', 'g#'), ('F#', 'd#'), ('C#', 'a#')]``

----

.. function:: augment(note)

      Augment a given note.
      
      Examples:
      
      >>> augment('C')
      'C#'
      >>> augment('Cb')
      'C'


----

.. function:: determine(notes)

      Determine the scales containing the notes.
      
      All major and minor scales are recognized.
      
      Example:
      
      >>> determine(['A', 'Bb', 'E', 'F#', 'G'])
      ['G melodic minor', 'G Bachian', 'D harmonic major']


----

.. function:: diminish(note)

      Diminish a given note.
      
      Examples:
      
      >>> diminish('C')
      'Cb'
      >>> diminish('C#')
      'C'


----

.. function:: get_notes(key=C)

      Return an ordered list of the notes in this natural key.
      
      Examples:
      
      >>> get_notes('F')
      ['F', 'G', 'A', 'Bb', 'C', 'D', 'E']
      >>> get_notes('c')
      ['C', 'D', 'Eb', 'F', 'G', 'Ab', 'Bb']


----

.. function:: reduce_accidentals(note)

      Reduce any extra accidentals to proper notes.
      
      Example:
      
      >>> reduce_accidentals('C####')
      'E'

----



:doc:`Back to Index</index>`
