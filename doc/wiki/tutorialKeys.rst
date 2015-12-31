Tutorial 2 - Keys and the Diatonic Scale
========================================

The keys module is another fundamental module providing support for keys and the diatonic scale. Without this module, mingus would be utterly useless. Let's open up a python shell and start exploring.


>>> import core.keys as keys



----


Keys
----

As we have seen in the previous tutorial, mingus accepts some funky syntax (eg. 'C####bbb#b'). While this is fine, it's normally not really helpful, especially not when talking about keys and scales. This module defines a list of basic notes (based on the circle of fifths):


>>> keys.keys
[('Cb', 'ab'), ('Gb', 'eb'), ('Db', 'bb'), ('Ab', 'f'), ('Eb', 'c'), ('Bb', 'g'), ('F', 'd'), ('C', 'a'), ('G', 'e'), ('D', 'b'), ('A', 'f#'), ('E', 'c#'), ('B', 'g#'), ('F#', 'd#'), ('C#', 'a#')]


Although the following functions will still work with the strange syntax, I'd advise you -for your own sanity- not to indulge in them.


----


The Notes in a Key
------------------


To get the notes in a certain key, you can use `diatonic.get_notes(note)`. This method returns a list of notes, starting with the tonic.



>>> keys.get_notes('C')
['C', 'D', 'E', 'F', 'G', 'A', 'B']



If you were not completely sure what a key was before, it should now be pretty clear. The key of C consists of all the white notes, which have a certain number of half note steps between them. If we now want the notes in the key of E, we can take the same steps, but this time starting on 'E' instead of 'C'. (See exercise 1).


>>> keys.get_notes('E')
['E', 'F#', 'G#', 'A', 'B', 'C#', 'D#']
>>> keys.get_notes('Bb')
['Bb', 'C', 'D', 'Eb', 'F', 'G', 'A']





----


Exercises
---------

* Write a program that lets the user input a key, get the notes in the key and print the half note steps between the notes. What do you notice when you ask for different keys?


----


You can learn more about `mingus.core.keys <refMingusCoreKeys>`_ in the reference section

  * `Tutorial 1 - Working with Notes <tutorialNote>`_
  * Tutorial 2 - Keys and the Diatonic Scale
  * `Tutorial 3 - Intervals <tutorialIntervals>`_
  * :doc:`Back to Index </index>`
