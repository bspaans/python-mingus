=====================
mingus.extra.musicxml
=====================

Convert mingus.containers to MusicXML files.

The MusicXML format represents common Western musical notation from the 17th
century onwards. It lets you distribute interactive sheet music online, and
use sheet music files with a wide variety of musical applications.

The MusicXML format is open for use by anyone under a royalty-free license,
and is supported by over 100 applications.

http://www.musicxml.org/xml.html


Attributes
----------

major_keys
^^^^^^^^^^

  * *Type*: list
  * *Value*: `['Cb', 'Gb', 'Db', 'Ab', 'Eb', 'Bb', 'F', 'C', 'G', 'D', 'A', 'E', 'B', 'F#', 'C#']`

minor_keys
^^^^^^^^^^

  * *Type*: list
  * *Value*: `['ab', 'eb', 'bb', 'f', 'c', 'g', 'd', 'a', 'e', 'b', 'f#', 'c#', 'g#', 'd#', 'a#']`

----

Functions
---------

.. function:: _bar2musicxml(bar).. function:: _composition2musicxml(comp).. function:: _gcd(a, b, terms)  * *Default values*: a = None, b = None, terms = None
Return greatest common divisor using Euclid's Algorithm.

.. function:: _lcm(a, b, terms)  * *Default values*: a = None, b = None, terms = None
Return lowest common multiple.

.. function:: _note2musicxml(note).. function:: _track2musicxml(track).. function:: from_Bar(bar).. function:: from_Composition(comp).. function:: from_Note(note).. function:: from_Track(track).. function:: write_Composition(composition, filename, zip)  * *Default values*: zip = False
Create an XML file (or MXL if compressed) for a given composition.

----

:doc:`Back to Index</index>`
