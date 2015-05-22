#summary The mingus.containers.Note module

----

= Tutorial 1 - The Note Class =

`mingus.core.notes` provides a way to work with notes. However, what if we want to work with notes in different octaves? Or what if we want to set the amplitude or some effects on a note? This Note class solves those problems and also provides the cornerstone of the `mingus.containers` package.

== Importing the Note Class ==

{{{

>>> from mingus.containers.Note import Note

}}}

----

== Creating and Setting Notes ==

Defining and setting notes is pretty easy and can be done in a variety of ways.

{{{

>>> Note("C")
'C-4'
>>> Note("C", 4)
'C-4'
>>> Note("C", 5)
'C-5'
>>> Note("C-3")
'C-3'
>>> n = Note()
>>> n.set_note("C", 5)
>>> n
'C-5'

}}}

== Note Attributes == 

The attributes `name`, `octave` and `dynamics` are always set and accessible from the outside:

{{{

>>> c = Note("C")
>>> c
'C-4'
>>> c.name
'C'
>>> c.octave
4
>>> c.dynamics
{}

}}}

The dynamics dictionary can be used to store additional information such as volume and effects.

*NB* If you are using the mingus.midi package: setting the `velocity`, `channel` and `bpm` attribute will have an effect on the output. 

----

== A Better Note to Integer Converter ==

A problem with `mingus.core.notes.note_to_int` is that it returns integers in the range 0-11. This would mean that 'Cb' and 'B' are both 11. This can be helpful, but when you are dealing with octaves you don't want this. The Note class fixes this and also overloads the int() function to make it simpler to use:

{{{

>>> int(Note("C", 4))
48
>>> int(Note("Cb", 4))
47
>>> int(Note("B", 4))
59

}}}

== A Better Integer to Note Converter ==

The opposite of the previous function is `from_int(integer)`, which sets the note to the corresponding integer where 0 is a C on octave 0, 12 is a C on octave 1, etc.

{{{
>>> c = Note()
>>> c.from_int(12)
'C-1'

}}}

----

== Methods on Notes ==

=== Octaves ===

Changing the octave can be done by setting the octave attribute, but the following methods can also be used:

{{{

>>> a = Note("A", 5)
>>> a 
'A-5'
>>> a.octave_up()
>>> a
'A-6'
>>> a.octave_down()
>>> a
'A-5'
>>> a.change_octave(+2)
'A-7'
>>> a.change_octave(-2)
'A-5'

}}}

=== Transposing ===

To move a Note an interval up or down, you can use the function `transpose(interval, up=True)`. The interval should be valid interval shorthand (see the [tutorialIntervals interval tutorial])

{{{
>>> a = Note("A")
>>> a.transpose("3")
>>> a
'C#-5'
>>> a.transpose("4", up=False)
>>> a
'G#-5'

}}}


=== Hertz ===

Converting from and to hertz can be done using the `from_hertz(hertz, standard_pitch=440)` and `to_hertz(standard_pitch=440)` functions, where `standard_pitch` can be used to set the pitch of A-4, from which the rest is calculated.


=== Migrated Methods ===

Some of the functions in `mingus.core.notes` were added to the Note class as methods for convenience.

{{{

>>> a = Note("A")
>>> a
'A-4'

}}}

{{{
>>> a.augment()
>>> a
'A#-4'

}}}

{{{
>>> a.diminish()
>>> a
'A-4'
}}}

{{{
>>> a.to_major()
>>> a
'C-4'
}}}

{{{
>>> a.to_minor()
>>> a
'A-4'
}}}

{{{
>>> a = Note("A#b#b")
>>> a.remove_redundant_accidentals()
'A-4'
}}}

----

= End of Tutorial 1 =

You can learn more about [refMingusContainersNote mingus.containers.Note] in the reference section

  * Tutorial 1 - The Note Class
  * [tutorialNoteContainerModule Tutorial 2 - NoteContainers]
  * [mingusIndex Back to Index]
