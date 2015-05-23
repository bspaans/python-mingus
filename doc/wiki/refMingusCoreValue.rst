=================
mingus.core.value
=================

Module for dealing with values.

A note value indicates the relative duration of a note.

In mingus, note values are represented by floating point numbers.
A quarter note is 4, because it stands for 1/4 note, an eighth note is 8
because it stands for 1/8, a sixteenth note is 16, etc.

These are all pretty straight forward, but how do you define a sixteenth
triplet? Well, sixteenth triplets are made by taking an eighth note
and deviding it in 3 equal parts. 1/8 times 1/3 = 1/24; so 24 is the number
we want. How about a dotted eighth note? A dotted eighth note has the length
of an eighth note plus half an eighth note. 1/8 + 1/16 = 3/16 = 1 / 16 / 3.
So 16/3 is the number we are looking for.

As you can see these calculations can be quite tiresome and can clutter
up your code. This module is here to help do the conversion.

Medieval backwards compatibility privided.


Attributes
----------


----

.. attribute::base_quintuplets

  * *Type*: list
  * *Value*: `[0.3125, 0.625, 1.25, 2.5, 5, 10, 20, 40, 80, 160]`


----

.. attribute::base_septuplets

  * *Type*: list
  * *Value*: `[0.4375, 0.875, 1.75, 3.5, 7, 14, 28, 56, 112, 224]`


----

.. attribute::base_triplets

  * *Type*: list
  * *Value*: `[0.375, 0.75, 1.5, 3, 6, 12, 24, 48, 96, 192]`


----

.. attribute::base_values

  * *Type*: list
  * *Value*: `[0.25, 0.5, 1, 2, 4, 8, 16, 32, 64, 128]`


----

.. attribute::breve

  * *Type*: float
  * *Value*: `0.5`


----

.. attribute::crotchet

  * *Type*: int
  * *Value*: `4`


----

.. attribute::demisemiquaver

  * *Type*: int
  * *Value*: `32`


----

.. attribute::eighth

  * *Type*: int
  * *Value*: `8`


----

.. attribute::half

  * *Type*: int
  * *Value*: `2`


----

.. attribute::hemidemisemiquaver

  * *Type*: int
  * *Value*: `64`


----

.. attribute::hundred_twenty_eighth

  * *Type*: int
  * *Value*: `128`


----

.. attribute::longa

  * *Type*: float
  * *Value*: `0.25`


----

.. attribute::minim

  * *Type*: int
  * *Value*: `2`


----

.. attribute::musicxml

  * *Type*: dict
  * *Value*: `{16: '16th', 1: 'whole', 2: 'half', 4: 'quarter', 32: '32th', 8: 'eighth', 64: '64th', 128: '128th'}`


----

.. attribute::quarter

  * *Type*: int
  * *Value*: `4`


----

.. attribute::quasihemidemisemiquaver

  * *Type*: int
  * *Value*: `128`


----

.. attribute::quaver

  * *Type*: int
  * *Value*: `8`


----

.. attribute::semibreve

  * *Type*: int
  * *Value*: `1`


----

.. attribute::semihemidemisemiquaver

  * *Type*: int
  * *Value*: `128`


----

.. attribute::semiquaver

  * *Type*: int
  * *Value*: `16`


----

.. attribute::sixteenth

  * *Type*: int
  * *Value*: `16`


----

.. attribute::sixty_fourth

  * *Type*: int
  * *Value*: `64`


----

.. attribute::thirty_second

  * *Type*: int
  * *Value*: `32`


----

.. attribute::whole

  * *Type*: int
  * *Value*: `1`

----

Functions
---------


----

.. function:: add(value1, value2)

  Return the value of the two combined.
  
  Example:
  
  >>> add(eighth, quarter)
  2.6666666666666665


----

.. function:: determine(value)

  Analyse the value and return a tuple containing the parts it's made of.
  
  The tuple respectively consists of the base note value, the number of
  dots, and the ratio (see tuplet).
  
  Examples:
  
  >>> determine(8)
  (8, 0, 1, 1)
  >>> determine(12)
  (8, 0, 3, 2)
  >>> determine(14)
  (8, 0, 7, 4)
  
  This function recognizes all the base values, triplets, quintuplets,
  septuplets and up to four dots. The values are matched on range.


----

.. function:: dots(value, nr=1)

  Return the dotted note value.
  
  A dot adds half the duration of the note. A second dot adds half of what
  was added before, etc. So a dotted eighth note has the length of three
  sixteenth notes. An eighth note with two dots has the length of seven
  thirty second notes.
  
  Examples:
  
  >>> dots(eighth)
  5.3333333333333333
  >>> dots(eighth, 2)
  4.5714285714285712
  >>> dots(quarter)
  2.6666666666666665


----

.. function:: quintuplet(value)

  Return the quintuplet note value.
  
  A quintuplet divides the base value two above into five parts. So a
  quintuplet eighth note is a fifth of a half note.
  
  Examples:
  
  >>> quintuplet(8)
  10
  >>> quintuplet(4)
  5


----

.. function:: septuplet(value, in_fourths=True)

  Return the septuplet note value.
  
  The usage of a septuplet is ambigious: seven notes can be played either
  in the duration of four or eighth notes.
  
  If in_fourths is set to True, this function will use 4, otherwise 8
  notes. So a septuplet eighth note is respectively either 14 or 7.
  
  Notice how
  
  >>> septuplet(8, False) == septuplet(4, True)
  True
  
  Examples:
  >>> septuplet(8)
  14
  >>> septuplet(8, False)
  7


----

.. function:: subtract(value1, value2)

  Return the note value for value1 minus value2.
  
  There are no exceptions for producing negative values, which can be
  useful for taking differences.
  
  Example:
  
  >>> substract(quarter, eighth)
  8.0


----

.. function:: triplet(value)

  Return the triplet note value.
  
  A triplet divides the base value above into three parts. So a triplet
  eighth note is a third of a quarter note.
  
  Examples:
  
  >>> triplet(eighth)
  12
  >>> triplet(4)
  6


----

.. function:: tuplet(value, rat1, rat2)

  Return a tuplet.
  
  A tuplet can be written as a ratio. For example: 5:4 means that you play
  5 notes in the duration of 4 (a quintuplet), 3:2 means that you play 3
  notes in the duration of 2 (a triplet), etc. This function calculates
  the note value when playing in rat1:rat2.
  
  Example:
  
  >>> tuplet(8, 3, 2)
  12

----

:doc:`Back to Index</index>`
