Tutorial 2 - Keys and the Diatonic Scale
========================================

The diatonic module is another fundamental module providing support for keys and the diatonic scale. Without this module, mingus would be utterly useless. Let's open up a python shell and start exploring.


>>> import core.diatonic as diatonic



----


Keys
----

As we have seen in the previous tutorial, mingus accepts some funky syntax (eg. 'C####bbb#b'). While this is fine, it's normally not really helpful, especially not when talking about keys and scales. This module defines a list of basic notes (based on the circle of fifths):


>>> diatonic.basic_keys
['Gb', 'Db', 'Ab', 'Eb', 'Bb', 'F', 'C', 'G', 'D', 'A', 'E', 'B', 'F#', 'C#', 'G#', 'D#', 'A#'] 


Although the following functions will still work with the strange syntax, I'd advise you -for your own sanity- not to indulge in them.


----


The Notes in a Key
------------------


To get the notes in a certain key, you can use `diatonic.get_notes(note)`. This method returns a list of notes, starting with the tonic.



>>> diatonic.get_notes("C")
["C", "D", "E", "F", "G", "A", "B"]



If you were not completely sure what a key was before, it should now be pretty clear. The key of C consists of all the white notes, which have a certain number of half note steps between them. If we now want the notes in the key of E, we can take the same steps, but this time starting on 'E' instead of 'C'. (See exercise 1).


>>> diatonic.get_notes("E")
["E", "F#", "G#", "A", "B", "C#", "D#"]
>>> diatonic.get_notes("Bb")
["Bb", "C", "D", "Eb", "F", "G", "A"]





----


A Better Integer to Note Converter
----------------------------------

Remember how poorly a theoretic job `notes.int_to_note(int)` did? `notes.int_to_note` would always convert 10 to A#, regardless of what key you're in. This fact becomes really obvious when you are playing in Bb. A better function would pay attention to the key as well; we can do that now:



>>> diatonic.int_to_note(10, "C")
'A#'
>>> diatonic.int_to_note(10, "F")
'Bb'
>>> diatonic.int_to_note(11, "C")
'B'
>>> diatonic.int_to_note(11, "Gb")
'Cb'




----


Exercises
---------

* Write a program that lets the user input a key, get the notes in the key and print the half note steps between the notes. What do you notice when you ask for different keys?
* For every note in `basic_keys`: Convert the numbers 0-11 using `diatonic.int_to_note` and `notes.int_to_note`. If the values are different, output the values, the number and the key to screen.


----


You can learn more about `mingus.core.diatonic <refMingusCoreDiatonic>`_ in the reference section

  * `Tutorial 1 - Working with Notes <tutorialNote>`_
  * Tutorial 2 - Keys and the Diatonic Scale
  * `Tutorial 3 - Intervals <tutorialIntervals>`_
  * :doc:`Back to Index </index>`
