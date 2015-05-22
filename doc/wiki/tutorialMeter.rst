#summary mingus.core.meter

----

= Tutorial 6 - Note Value and Meter =

----

== Importing the value Module ==

{{{

>>> import mingus.core.value as value

}}}


----

== Note Value ==

A note value indicates the relative duration of a note. In mingus, note values are represented by floating point numbers. A quarter note is 4, because it stands for 1/4 note, an eighth note is 8 because it stands for 1/8, a sixteenth note is 16, etc. These are all pretty straight forward, but how do you define a sixteenth triplet? Well, sixteenth triplets are made by taking an eighth note and deviding it in 3 equal parts. 1/8 times 1/3 = 1/24; so 24 is the number we want. How about a dotted eighth note? A dotted eighth note has the length of an eighth note plus half an eighth note. 1/8 + 1/16 = 3/16 = 1 / 16 / 3. So 16/3 is the number we are looking for. As you can see these calculations can be quite tiresome and can clutter up your code. This module is here to help do the conversion. 

=== English or Standard Notation ===

Let us start by looking at some constants.

{{{
>>> value.whole
1
>>> value.eighth
8
>>> value.sixteenth
16
}}}

Nothing spectular so far. 

For medieval backwards compatibility the English notation has also been included.

{{{
>>> value.longa
0.25
>>> value.quaver
8
>>> value.quasihemidemisemiquaver
128
}}}

Never again will you have to remember the difference between a semibreve and a semihemidemisemiquaver! 

----

== Making Dotted Notes ==

A dot adds half the duration of the note. A second dot adds half of what was added before, etc. For example: a dotted eighth note has the length of three sixteenth notes and an eighth note with two dots has the length of seven thirty second notes. The function `dots(value, nr=1)` returns the dotted note value.

{{{
>>> value.dots(value.eighth)
5.3333333333333333
>>> value.dots(value.eighth, 2)
4.5714285714285712

}}}

----

== Making Tuplets ==

A tuplet can be written as a ratio. For example: 5:4 means that you play 5 notes in the duration of 4 (this is also called a quintuplet), 3:2 means that you play 3 notes in the duration of 2 (a triplet), etc. The tuplet function calculates the note value when playing in a certain ratio.

{{{
>>> value.tuplet(value.eighth, 5, 4)
10.0
>>> value.tuplet(value.eighth, 3, 2)
12.0
}}}

There are a couple of 'shortcut' functions to tuplet that have predefined ratios; triplet (3:2) and quintuplet (5:4).

{{{
>>> value.triplet(value.eighth)
12.0
>>> value.quintuplet(value.eighth)
10.0
}}}

A septuplet function also exists and defaults to the ratio 7:4. When the second argument is set to False, the ratio is the less common 7:8.

{{{
>>> value.septuplet(value.eighth)
14.0
>>> value.septuplet(value.eighth, False)
7.0
}}}

----

== Adding and Subtracting Note Values ==

In the container modules we will see that it is often handy to have some simple functions for basic adding and subtracting available.

{{{
>>> value.add(value.eighth, value.quarter)
2.6666666666666665
>>> value.add(value.eighth, value.eighth)
4.0
>>> value.subtract(2.6666666666666665, 8)
4.0
}}}

----

== Recognising Note Values ==

The floating point numbers are a fast and simple way to store the length of a note, but for some reasons (mainly notation related) it would be nice to know the basic note value, the number of dots and the ratio. Determine returns just that:

{{{
>>> value.determine(value.eighth)
(8, 0, 1, 1)
>>> value.determine(12)
(8, 0, 3, 2)
>>> value.determine(14)
(8, 0, 7, 4)
>>> value.determine(dots(value.eighth))
(8, 1, 1, 1)
}}}

----

Now that we have seen how note values are handled, let's take a look at a slightly related and small module dealing with meter.

== Importing meter Module ==

{{{

>>> import mingus.core.meter as meter

}}}


----

== Simple Meters ==

Meters in mingus are represented by a tuple consisting of respectively the nominator and the denominator. We can use is_valid to test whether an arbitrary tuple is a valid representation or not:

{{{

>>> meter.is_valid((4, 4))
True
>>> meter.is_valid((4, 5))
False
>>> meter.is_valid((5, 4))
True

}}}

Some constants are also included:

{{{

>>> meter.common_time
(4, 4)
>>> meter.cut_time
(2, 2)

}}}

----

== Compound Meters ==

Compound meter is a meter in which each measure is divided into three or more or two uneven parts (as opposed to two even parts). To test whether a meter is compound or not, we can use `is_compound`:

{{{

>>> meter.is_compound((3, 4))
True
>>> meter.is_compound((6, 8))
True
>>> meter.is_compound((4, 4))
False

}}}

----

== Asymmetrical Meters ==

Asymmetrical meters represent meters that can't be divided into parts of two. is_assymetrical test whether this is true or not.

{{{

>>> meter.is_assymetrical((3, 4))
True
>>> meter.is_assymetrical((5, 4))
True
>>> meter.is_assymetrical((7, 4))
True
>>> meter.is_assymetrical((4, 4))
False
>>> meter.is_assymetrical((6, 4))
False


}}}

----

= End of Tutorial 6 =

You can learn more about [refMingusCoreValue mingus.core.value] and [refMingusCoreMeter mingus.core.meter] in the reference section.

  * [tutorialNote Tutorial 1 - Working with Notes]
  * [tutorialDiatonic Tutorial 2 - Keys and the Diatonic Scale]
  * [tutorialIntervals Tutorial 3 - Intervals]
  * [tutorialChords Tutorial 4 - Triads, Sevenths and Extended Chords]
  * [tutorialScales Tutorial 5 - Scales]
  * Tutorial 6 - Note Value and Meter
  * [tutorialProgressions Tutorial 7 - Progressions]
  * [tutorialCore Tutorial 8 - ...And Now What?]
  * [mingusIndex Back to Index]
