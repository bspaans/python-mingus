﻿Tutorial 4 - Triads, Sevenths and Extended Chords
=================================================

This module is build upon the interval module and provides a way to generate and recognise various chords. 


>>> import mingus.core.chords as chords


----


Triads
------

Triads are chords made of three notes. 

Natural Diatonic Triads
^^^^^^^^^^^^^^^^^^^^^^^

Natural diatonic triads are probably the most common chords. As was hinted in the last exercises of the intervals tutorial, they are constructed by choosing a base note in a key and adding its third and fifth. For instance, here are the notes in C again:



>>> diatonic.get_notes("C")
['C', 'D', 'E', 'F', 'G', 'A', 'B']



Let's say we want the triad starting on D. We pick its third, 'F', and its fifth, 'A', and we're already done. 

This, in a nutshell, is what the following procedure does. To get the triad starting on a certain note in a certain key we can use the `chords.triad(note, key)` function:



>>> chords.triad("E", "C")
["E", "G", "B"]
>>> chords.triad("E", "E")
["E", "G#", "B"]
>>> chords.triad("E", "F")
["E", "G", "Bb"]




We can also request all the triads in a certain key with `chords.triads(key)`:



>>> chords.triads("C")
[["C", "E", "G"], ["D", "F", "A"], ["E", "G", "B"], ["F", "A", "C"], ["G", "B", "D"], ["A", "C", "E"], ["B", "D", "F"]]



Absolute Triads
^^^^^^^^^^^^^^^

The natural triads are ubiquitous, but so is the ability of musicians and composers to stray of the path and put in their own chords to keep things interesting. That's why working with only the naturally appearing chords within a key is often not enough. 



>>> chords.major_triad("C")
["C", "E", "G"]
>>> chords.minor_triad("C")
["C", "Eb", "G"]
>>> chords.diminished_triad("C")
["C", "Eb", "Gb"]
>>> chords.augmented_triad("C")
["C", "E", "G#"]
>>> chords.suspended_triad("C")
["C", "F", "G"]



As you can see these functions work without a key argument and always give back notes with the same absolute intervals between them.


----


Sevenths
--------

Natural Diatonic Sevenths
^^^^^^^^^^^^^^^^^^^^^^^^^

Triads and sevenths are constructed in the same way, in that thirds are added to a base note. For a triad, we'd take the base note, its third and its fifth. For a seventh chord, we also take its seventh (which is again a third away from the last added note).



>>> chords.seventh("C", "C")
["C", "E", "G", "B"]
>>> chords.seventh("D", "C")
["D", "F", "A", "C"]
>>> chords.seventh("E", "C")
["E", "G", "B", "D"]



You can also use `chords.sevenths(key)` to get all the seventh chords in that key.


Absolute Sevenths
^^^^^^^^^^^^^^^^^

Once again, you can also request a specific seventh chord, but this time there are a lot more of them. 



>>> chords.major_seventh("C")
["C", "E", "G", "B"]
>>> chords.minor_seventh("C")
["C", "Eb", "G", "Bb"]
>>> chords.dominant_seventh("C")
["C", "E", "G", "Bb"]
>>> chords.half_diminished_seventh("C")
["C", "Eb", "Gb", "Bb"]
>>> chords.minor_seventh_flat_five("C")
["C", "Eb", "Gb", "Bb"]
>>> chords.diminished_seventh("C")
["C", "Eb", "Gb", "Bbb"]
>>> chords.minor_major_seventh(C")
["C", "Eb", "G", "B"]
>>> chords.augmented_major_seventh("C")
["C", "E", "G#", "B"]
>>> chords.augmented_minor_seventh("C")
["C", "E", "G#", "Bb"]




----


Get Chords from Shorthand
-------------------------

Usually you don't want to remember and type all the different functions just to get some simple chords. The `from_shorthand(string)` function tries to make life easier. from_shorthand takes a string representation of a chord and returns a list of notes.



>>> from_shorthand("C")
['C', 'E', 'G']
>>> from_shorthand("Cm")
['C', 'Eb', 'G']



The `from_shorthand` function can deal with almost any chord and knows about most common abbreviations. Here is a slashed chord and a polychord, just to give you a flavour:



>>> from_shorthand("A/G")
['G', 'A', 'C#', 'E']
>>> from_shorthand("Cm/M7|FM")
['F', 'A', 'C', 'Eb', 'G', 'B']



Currently the following abbreviations are recognised: 

	* Triads: *'m'*, *'M'* or *''*, *'dim'*. 
	* Sevenths: *'m7'*, *'M7'*, *'7'*, *'m7b5'*, *'dim7'*, *'m/M7'* or *'mM7'*
	* Augmented chords: *'aug'* or *'+'*, *'7#5'* or *'M7+5'*, *'M7+'*, *'m7+'*, *'7+'*
	* Suspended chords: *'sus4'*, *'sus2'*, *'sus47'*, *'sus'*, *'11'*, *'sus4b9'* or *'susb9'*
	* Sixths: *'6'*, *'m6'*, *'M6'*, *'6/7'* or *'67'*, *6/9* or *69*
	* Ninths: *'9'*, *'M9'*, *'m9'*, *'7b9'*, *'7#9'*
	* Elevenths: *'11'*, *'7#11'*, *'m11'*
	* Thirteenths: *'13'*, *'M13'*, *'m13'*
	* Altered chords: *'7b5'*, *'7b9'*, *'7#9'*, *'67'* or *'6/7'*
	* Special: *'5'*, *'NC'*, *'hendrix'*

The letters `m` and `M` in the abbreviations  can always be substituted by respectively `min`, `mi` or `-` and `maj` or `ma` (eg. `from_shorthand("Amin7") == from_shorthand("Am7")`, etc.).
	

----


Chords by Harmonic Function
---------------------------

You can also refer to chords by their harmonic function. For instance `tonic(key)` will get you the tonic triad; `tonic7(key)` the tonic seventh. 



>>> chords.tonic("C")
["C", "E", "G"]
>>> chords.supertonic("C")
["D", "F", "A"]
>>> chords.mediant("C")
["E", "G", "B"]
>>> chords.subdominant("C")
["F", "A", "C"]
>>> chords.dominant("C")
["G", "B", "D"]
>>> chords.submediant("C")
["A", "C", "E"]



Roman Numbering
^^^^^^^^^^^^^^^

It's often easier to refer to harmonic functions using roman numbers. 



>>> chords.I("C")
["C", "E", "G"]
>>> chords.IV("C")
["F", "A", "C"]
>>> chords.V7('C')
['G', 'B', 'D', 'F']


The functions I-VI and I7-VI7 may all be used. The numbers II, III, VI and their sevenths may also be refered to using lower-case numbers (ii, ii7, etc) to indicate that they are minor. See the progressions tutorial for more about harmonic sequences + an advanced to_chords function.


----


Inversions
----------

Inverting a chord can be pretty common depending on genre. Here is a quick way to do take the first inversion in mingus:



>>> chords.first_inversion(["C", "E", "G"])
["E", "G", "C"]
>>> chords.first_inversion(["E", "G", "C"])
["G", "C", "E"]
>>> chords.first_inversion(["G", "C", "E"])
["C", "E", "G"]



Other functions that can be used:



>>> chords.second_inversion(["C", "E", "G"])
["G", "C", "E"]
>>> chords.third_inversion(["C", "E", "G", "B"])
["B", "C", "E", "G"]




----



Recognize
---------

One of the cool things about this module is that it can not only generate but also recognise various chords and their inversions.



>>> chords.determine(["C", "E", "G"])
['C major triad']
>>> chords.determine(["B", "C", "E", "G"])
['C major seventh, third inversion']
>>> chords.determine(["B", "C", "E", "G#"])
['C augmented major seventh, third inversion']



As you can see, the `chords.determine` will recognize pretty complex chords. You might wonder why the function returns a list. This is because certain chord can have multiple (or no) interpretations. Whenever their is more than one interpretation, the list will be ordered from less to most inversions, followed by polychords (the `|` notation). Therefore, the first item in the list is probably the most likely interpretation: 



>>> chords.determine(["C", "Eb", "Gb", "Bb"])
['C half diminished seventh', 'Eb minor sixth, third inversion', 'Ebm|Cdim']
>>> chords.determine(["C", "C", "C", "C"])
[]



_Note:_ Currently `chords.determine` can take lists containing one to fourteen notes. A list of one item will just return the note. A list of two notes will be redirected to `intervals.determine`. The rest will be interpreted as chords.

Shorthand
---------

The chord descriptions returned by determine can be quite lengthy. That's why you can also request the chords to be returned in shorthand. The chord description will be replaced by an abbreviation (often found in jazz) and the inversion won't be included in the result.



>>> chords.determine(["C", "E", "G", "B"], True)
["Cmaj7"]
>>> chords.determine(["E", "G", "B", "C"], True)
["Cmaj7"]
>>> chords.determine(["C", "Eb", "Gb", "Bb"], True)
["Cmin7b5", "Ebmin6", "Ebm|Cdim"]




----


Exercises
---------

* Write a program that takes a key and prints out all the triads and sevenths as shorthand.
* Determine what _type_ of triads and sevenths are naturally occuring in every key.
* The chord sequence I, IV, V, I is a simple song. Write a program that takes a key and prints out the corresponding chords in shorthand. 


----


You can learn more about `mingus.core.chords in the reference section <refMingusCoreChords>`_.

  * `Tutorial 1 - Working with Notes <tutorialNote>`_
  * `Tutorial 2 - Keys and the Diatonic Scale <tutorialKeys>`_
  * `Tutorial 3 - Intervals <tutorialIntervals>`_
  * Tutorial 4 - Triads, Sevenths and Extended Chords 
  * `Tutorial 5 - Scales <tutorialScales>`_
  * :doc:`Back to Index </index>`
