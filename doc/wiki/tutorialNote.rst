Tutorial 1 - Working with notes
===============================

mingus was written out of a desire to have a pythonic way of working with
music: simple but also correct. This module lies at the heart of the package
and introduces the first building blocks: note names, accidentals and an
int-to-note converter (and vice versa).


To start this tutorial, open up a python shell and enter:


>>> import mingus.core.notes as notes


Now we are ready to work with notes.


----


Notes as Strings
----------------

A note in mingus is represented by a name (A...G) and some or no accidentals
('#' and 'b'); where 'b' lowers and '#' raises the note by one half note step.
To test whether an arbitrary string is a valid note we can use
`notes.is_valid_note(str)`.

Some examples of valid notes:


>>> notes.is_valid_note("C")
True
>>> notes.is_valid_note("D#")
True
>>> notes.is_valid_note("Eb")
True
>>> notes.is_valid_note("Fbb")
True
>>> notes.is_valid_note("G##")
True


Some examples of invalid notes:


>>> notes.is_valid_note("c")
False
>>> notes.is_valid_note("D #")
False
>>> notes.is_valid_note("E-b")
False

Some, perhaps suprisingly valid notes:


>>> notes.is_valid_note("C######bb")
True
>>> notes.is_valid_note("C#b#bb##b##bb")
True


As you can see, mingus can handle any number of accidentals, whether it is the
sensible thing to do or not. If you want to clean up messy accidentals, you can
use remove_redundant_accidentals(note). Because it's all fun and games until
someone gets hurt.


>>> notes.remove_redundant_accidentals("C##b")
'C#'
>>> notes.remove_redundant_accidentals("C#b#bb##b##bb")
'C'



----


Notes as Integers
-----------------

Sometimes it is easier to work with notes as integers in range(0,12). This is possible with the functions `notes.note_to_int(str)` and `notes.int_to_note(int)`.

Note to integer
^^^^^^^^^^^^^^^

>>> notes.note_to_int("C")
0
>>> notes.note_to_int("B")
11
>>> notes.note_to_int("Cb")
11
>>> notes.note_to_int("C#")
1
>>> notes.note_to_int("Db")
1


As you can see in the examples some notes return the same values. These notes are called enharmonic, because they sound the same. (There is `notes.is_enharmonic(note1, note2)` to test if two notes are enharmonic).

Integer to Note
^^^^^^^^^^^^^^^

Because enharmonic notes exist, it is impossible to create a sound int-to-note converter based on an integer alone. For example; in the last piece of code we saw that B and Cb are both 11. They sound the same, but they aren't theoretically the same. This can be important when building and recognizing intervals and thus scales and chords, because intervals depend on the note name. For instance: the interval between A and B is called a major second, while the interval between A and Cb is a diminished third. `diatonic.int_to_note` does a better job at the conversion, bearing the key in mind as well. The converter in [tutorialNoteModule Note] can also handles octaves on top of that. 
Anyway, if you don't care about theoretically sound conversions or don't need to differentiate, this function is fine (it sounds the same, after all):



>>> notes.int_to_note(0)
"C"
>>> notes.int_to_note(1)
"C#"
>>> notes.int_to_note(2)
"D"
>>> notes.int_to_note(3)
"D#"
>>> notes.int_to_note(4)
"E"



----


Helper Functions
----------------

Augment and Diminish
^^^^^^^^^^^^^^^^^^^^

Augmenting and diminishing a note is a little bit harder than just slapping a '#' or 'b' on at the end of the string. For instance: when you want to augment a 'Cb' note, a 'C' would be nicer than a 'Cb#' (although, again, they are the same, but it's like using double negative). `augment` and `diminish` do a nice job at this:


>>> notes.augment("C")
"C#"
>>> notes.augment("Cb")
"C"
>>> notes.augment("C#")
"C##"
>>> notes.augment("B")
"B#"


Diminishing a note:


>>> notes.diminish("C")
"Cb"
>>> notes.diminish("C#")
"C"
>>> notes.diminish("Cb")
"Cbb"
>>> notes.diminish("B#")
"B"



Minor and Major conversions
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Minor:


>>> notes.to_minor("C")
"A"
>>> notes.to_minor("F")
"D"
>>> notes.to_minor("D")
"B"
>>> notes.to_minor("B")
"G#"


Major:


>>> notes.to_major("A")
"C"
>>> notes.to_major("D")
"F"
>>> notes.to_major("B")
"D"
>>> notes.to_major("G#")
"B"


----


Exercises
---------

* Write a program that asks for a note, check if it's valid and output the note which is five half notes away from it.
* Get the minor equivalent of a valid note and diminish it.
* Generate the first thousand fibonacci numbers and use a modulo 12 operation (eg. `n % 12`) to convert each value to a note. 


----


You can learn more about `mingus.core.notes <refMingusCoreNotes>`_ in the reference section.

* `Tutorial 2 - Keys and the Diatonic Scale <tutorialDiatonic>`_
* :doc:`Back to Index </index>`
