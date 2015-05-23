Tutorial 5 - Scales
===================

This module isn't 100% complete yet, but might already be of use to you.



>>> import mingus.core.scales as scales



----


The Diatonic Scale and Its Modes
--------------------------------

Throughout these tutorials we have been using a sequence of notes called the diatonic scale. You can already get it from the `diatonic` module, but it's also linked here for completeness:



>>> scales.diatonic("C")
["C", "D", "E", "F", "G", "A", "B"]



Sometimes we want to refer to a particular mode of the diatonic scale. This means that you start the scale on another note. The ionian mode, which is the same as the diatonic, starts on C, the dorian mode starts on D, etc.



>>> scales.ionian("C")
["C", "D", "E", "F", "G", "A", "B"]
>>> scales.dorian("D")
["D", "E", "F", "G", "A", "B", "C"]
>>> scales.phrygian("E")
["E", "F", "G", "A", "B", "C", "D"]
>>> scales.lydian("F")
["F", "G", "A", "B", "C", "D", "E"]
>>> scales.mixolydian("G")
["G", "A", "B", "C", "D", "E", "F"]
>>> scales.aeolian("A")
["A", "B", "C", "D", "E", "F", "G"]
>>> scales.locrian("B")
["B", "C", "D", "E", "F", "G", "A"]




For more on modes, see `wikipedia <http://en.wikipedia.org/wiki/Musical_mode>`_


----


The Minor Scales 
----------------

The natural minor scale is the scale starting on the minor of a key and is thus the same as the aeolian mode:



>>> scales.natural_minor("A")
["A", "B", "C", "D", "E", "F", "G"]



The harmonic minor differentiates from the natural minor in its raised seventh, which gives the scale a dominant seventh chord. 



>>> scales.harmonic_minor("A")
["A", "B", "C", "D", "E", "F", "G#"]



The melodic minor also has a raised sixth to fill the gap, but 'officially' only when it's used in an ascending order. When descending, the scale to use is a minor scale. I use the word officially lightly, because this rule has been used rather inconsistently.



>>> scales.melodic_minor("A")
["A", "B", "C", "D", "E", "F#", "G#"]




----


Other Scales 
------------

Some other common scales are the chromatic and whole note ones. The chromatic scale basically consists of twelve notes each a minor second step apart (there are some notational differences (`source <http://en.wikipedia.org/wiki/Chromatic_scale>`_), but they are not supported at this point). 



>>> scales.chromatic("C")
["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"]



The whole note scale consists of six notes each a major second apart:


>>> scales.whole_note("C")
["C", "D", "E", "F#", "G#", "A#"]




----


As stated before, the scales module isn't 100% finished. There has been some work done on a scale recognition function (scales.determine), but that hasn't been completed yet (see issue #17). It can do exact matches on scales that are known, but it should be able to do fuzzy matches so that it can also return possible scales over a given chord (see issue #14).


----

You can learn more about `mingus.core.scales in the reference section <refMingusCoreScales>`_.

  * `Tutorial 1 - Working with Notes <tutorialNote>`_
  * `Tutorial 2 - Keys and the Diatonic Scale <tutorialDiatonic>`_
  * `Tutorial 3 - Intervals <tutorialIntervals>`_
  * `Tutorial 4 - Triads, Sevenths and Extended Chords <tutorialChords>`_
  * Tutorial 5 - Scales
  * `Tutorial 6 - Note Value and Meter <tutorialMeter>`_
  * :doc:`Back to Index </index>`
