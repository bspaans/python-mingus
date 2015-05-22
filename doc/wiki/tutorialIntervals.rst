#summary Exploring `mingus.core.intervals`

----

= Tutorial 3 - Intervals =

An interval in music theory describes the relationship between the pitches of two notes and is a building block for chords and scales. This module can be used to build arbitrary intervals. It also has a special recognizing function, which can determine the interval between two notes.


== Importing Intervals ==

The same as before. A python shell and a simple import is all we need to get started:

{{{

>>> import mingus.core.intervals as intervals

}}}

----

== Natural Diatonic Intervals ==

Taking the natural unison, second, third, fourth, fifth, sixth or seventh of a certain note in a certain key is pretty easy with functions named just like that. The functions expect a note and a key:

{{{

>>> intervals.second("C", "C")
"D"
>>> intervals.second("E", "C")
"F"
>>> intervals.second("E", "D")
"F#"
>>> intervals.third("C", "C")
"E"
>>> intervals.seventh("C", "C")
"B"

}}}

For people who are uncertain about what's going on here, take a look at the notes in the key of C:

{{{

>>> diatonic.get_notes("C")
['C', 'D', 'E', 'F', 'G', 'A', 'B']

}}}

If we want the natural second, starting on C in the key of C, we move one step to the right and get D. If we start on the E, we get an F, etc.
Now, if we want to get the third we move two steps to the right, for the fourth, three steps, etc. If we reach the end, we start back at the beginning. For instance, the natural fourth of A in the key of C is D.

----

== Absolute Intervals ==

The second, third, etc. functions work great and are heavily used in the chord module, but sometimes you need a specific interval starting on a note. The same function names, but prefixed with minor or major will take care of that:

{{{

>>> intervals.minor_second("C")
"Db"
>>> intervals.major_sixth("C")
"A"
>>> intervals.minor_third("Cb")
"Ebb"

}}}

The theory behind this is a bit harder, though. If we look at the notes in the key of C again, we find that the number of half steps between C and D is two and the number of half steps between C and E is four. We know that these are respectively the second and the third natural interval. By convention we call these major. Db and Eb would be a minor second and a minor third. The same works for the other natural intervals. (See also exercise 1)

*Note* `major_fifth` and `major_fourth` are better known as `perfect_fifth` and `perfect_fourth`. Both functions may be used.

----

=== Interval Shorthand ===

The `from_shorthand` function gives you a way to handle intervals programmatically. You can use the numbers 1-7 combined with an optional accidental prefix to get the interval from a certain note. Any number of accidentals can be used, but -again- use it cautiously. No prefix means that you want the major interval, a 'b' will return the minor interval, 'bb' the diminished, '#' the augmented. 

{{{

>>> from_shorthand("A", "3")
'C#'
>>> from_shorthand("A", "b3")
'C'

}}}

The interval usually goes up, but you can let it go down as well.

{{{

>>> from_shorthand("E", "2", False)
'D'

}}}

=== Recognize Intervals ===

To determine what the interval between note1 and note2 is called, we can use `interval.determine(note1, note2)`. This is where we really start to notice that 'Cb' and 'B' are not the same:

{{{

>>> interval.determine("C", "E"):
"major third"
>>> interval.determine("C", "Cb"):
"minor unison"
>>> interval.determine("C", "B"):
"major seventh"
>>> interval.determine("A", "G"):
"minor seventh"
>>> interval.determine("Gbb", "Ab"):
"augmented second"


}}}


The determine function can also output the result in shorthand, which can be fed back into `from_shorthand`.

{{{

>>> interval.determine("C", "E", True)
"3"
>>> interval.determine("C", "Eb", True)
"b3"

}}}

----

=== Measuring ===

Sometimes it's just more convenient to work with integers than with shorthand. For those occasions you can use the `measure` function, which will return the number of half note steps between two notes. Also notice how the steps between C and D are different from the steps between D and C:

{{{

>>> interval.measure("C", "D")
2
>>> interval.measure("D", "C")
10

}}}

----

== Exercises ==

  # Take the minor and major thirds and fourths of the note C. Output the note and the note as integer to the screen. Do you notice something?
  # Create a program where a user can input a key and a note and gets the note + the natural third + the natural fifth back. This is a called a natural triad (= chord made out of three notes).

----

= End of Tutorial 3 = 

You can learn more about [refMingusCoreIntervals mingus.core.intervals] in the reference section.

  * [tutorialNote Tutorial 1 - Working with Notes]
  * [tutorialDiatonic Tutorial 2 - Keys and the Diatonic Scale]
  * Tutorial 3 - Intervals
  * [tutorialChords Tutorial 4 - Triads, Sevenths and Extended Chords]
  * [mingusIndex Back to Index]
