#summary The simple mingus.core.progressions

----

= Tutorial 7 - Progressions =

In music theory you often deal with sequences of chords. These chord sequences are called progressions and are often written down using roman numerals. In this system the 'I' refers to the first natural triad in a key, the II to the second, etc. We can add prefixes and suffixes to denote more complex progressions like #V7, bIIdim7, etc.

The progressions module provides methods which can convert progressions into chords and vice versa. It can also give suggestions for chord-substitutions.

== Importing the Module == 

{{{

>>> import mingus.core.progressions as progressions

}}}

----

== Functions to Chords ==

Remember the chord functions from [tutorialChords the chords tutorial]? As handy as they can be, they feel a bit clunky. For example: we want to take the I, IV and V7 chord in a couple of different keys:

{{{

>>> [chords.I("C"), chords.IV("C"), chords.V7("C")]
>>> [chords.I("F"), chords.IV("F"), chords.V7("F")]

}}}

As you can see, you would have to retype the actual progression everytime you needed it. Instead we can do this:

{{{

>>> progression = ["I", "IV", "V7"]
>>> progressions.to_chords(progression, "C")
>>> progressions.to_chords(progression, "F")

}}}

Which will do exactly the same thing and is generally a lot nicer and more modular. 

Another advantage is that the `to_chords` function knows about prefixes and suffixes so you denote complex progressions. You can use any number of accidentals as prefix and any known chord shorthand as suffix:

{{{

>>> progressions.to_chords(["I", "bIV", "VIIdim7"])
[['C', 'E', 'G'], ['Fb', 'Ab', 'Cb'], ['B', 'D', 'F', 'Ab']]

}}}

Note: since the use of '7' as suffix classicly means that you want the natural seventh chord instead of the natural triad, you have to use the 'dom7' shorthand to get the dominanth seventh - where you would use '7' when talking about chords. In other words I7 will give you a major seventh, Idom7 a dominanth seventh. 

----

== Chords to Functions ==

Now that we can convert progressions to chords, it would be nice if we could hand mingus some chords and get the progressions back. That's what `determine` is for. Here's an example that uses the chords from the previous example:

{{{

>>> a = progressions.to_chords(["I", "bIV", "VIIdim7"])
>>> a
[['C', 'E', 'G'], ['Fb', 'Ab', 'Cb'], ['B', 'D', 'F', 'Ab']]
>>> progressions.determine(a, "C")
[['tonic'], ['minor subdominant'], ['subtonic diminished seventh']]
>>> progressions.determine(a, "C", True)
[['I'], ['bIV'], ['viidim7']]

}}}

----

== Substitutions ==

`substitute(progression, index, depth = 0)` gives a list of possible substitutions for `progression[index]`. If depth > 0 the substitutions of each result will be recursively added as well.

{{{
>>> progressions.substitute(["I", "IV", "V", "I"], 0)
["III", "VI", etc.
}}}

`substitute` performs all kinds of substitutions. If you want more fine grained control you can use the functions `substitute_harmonic`, `substitute_major_for_minor`, `substitute_minor_for_major`, `substitute_diminished_for_diminished` and `substitute_diminished_for_dominant`. Check the reference section of this module to read more about them.

----

= End of Tutorial 7 =

You can learn more about [refMingusCoreProgressions mingus.core.progressions] in the reference section.

  * [tutorialNote Tutorial 1 - Working with Notes]
  * [tutorialDiatonic Tutorial 2 - Keys and the Diatonic Scale]
  * [tutorialIntervals Tutorial 3 - Intervals]
  * [tutorialChords Tutorial 4 - Triads, Sevenths and Extended Chords]
  * [tutorialScales Tutorial 5 - Scales]
  * [tutorialMeter Tutorial 6 - Note Value and Meter]
  * Tutorial 7 - Progressions
  * [tutorialCore Tutorial 8 - Working with the Core]
  * [mingusIndex Back to Index]
