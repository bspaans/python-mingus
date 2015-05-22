#summary The mingus.containers.Bar module

----

= Tutorial 3 - Bars =

Now that we can group notes vertically, we want to be able to group them horizontally. The Bar class (and later the Track class) can help us with that. A bar of music can be described as a collection of notes (!NoteContainers in our model) played in succession in a certain meter and key. This class tries to model that behaviour and provides ways to add and edit Notes and !NoteContainers.

== Import the Bar Class ==

{{{

>>> from mingus.containers.Bar import Bar

}}}

----

== Creating a New Bar ==

A Bar() accepts a key and a meter as its optional arguments; these arguments by default set the key to C and the meter to 4/4.

{{{

>>> b = Bar()
>>> b.key.name
'C'
>>> b.meter
(4, 4)

}}}

If you change the meter after its initial creation be sure to use the `set_meter` function instead of setting the `meter` attribute directly, because the length of the Bar needs to be changed as well (see 'The Bar internals explained' below).

{{{

>>> e = Bar('E', (6, 8))
>>> e.key.name
'E'
>>> e.meter
(6, 8)
>>> e.set_meter((4,4))
>>> e.meter
(4, 4)

}}}


----

== Adding Notes and !NoteContainers to a Bar ==

The `place_notes(notes, duration)` function is used to add notes to a Bar. Notes can be written as strings, but Note and NoteContainer objects, and lists of strings and Note objects are also accepted. The duration is entered as a float which stands for the note value. 1 Represents a whole note, 2 a half note, 4 a quarter note, etc. See the [refMingusCoreValue core.value] module and its [tutorialMeter tutorial] for more sophisticated note values. This function returns True if there was room enough in the Bar to place the notes and False otherwise.

{{{

>>> b = Bar()
>>> b.meter
(4, 4)
>>> b.place_notes("A-4", 4)
True
>>> b.place_notes("C-5", 4)
True
>>> b.place_notes(["E-5", "G-5"], 2)
True
>>> b.place_notes("D", 4)
False

}}}

As you can see, everything goes fine until we try to add another quarter note after we have already filled the Bar up.


== Adding Rests ==

Calling `place_rest(duration)` is the same as calling `place_notes(None, duration)` or adding an empty !NoteContainer.

{{{

>>> b = Bar()
>>> b.place_rest(4)
True
>>> b.place_notes(None, 4)
True

}}}

== The Overloaded '+' Operator ==

'+' can be used to add notes quickly. The downside is that you can't control the duration of the note which will default to the last item in the Bar.meter tuple (ie. 4 in (4, 4), 8 in (6, 8), etc.), but this shouldn't be a problem for simple uses. 

{{{

>>> b = Bar()
>>> b + "C"
True
>>> b + "Db"
True
>>> b + None
True
>>> b + "G"
True

}}}



----

== The Bar Internals Explained == 

As we have seen before, the Bar class has a couple of attributes from which `key` and `meter` are the ones that you should deal with yourself, directly or indirectly. To understand what goes on behind the scenes however, we should take a look at `length` and `current_beat`:

=== The length attribute ===

The length attribute gets calculated each time you set a meter and is used throughout the class to check whether the Bar can contain any more notes, etc.

{{{

>>> b = Bar()
>>> b.length
1.0
>>> b2 = Bar('C', (5, 4))
>>> b.length
1.25

}}}

The length gets calculated as follows: `meter[0] * (1.0 / meter[1])`. This is the reason it's important to use the `set_meter` method instead of overwriting the `meter` attribute directly (as you can safely do with `key`).

=== The current_beat attribute ===

The `current_beat` attribute gets updated each time a note is added, removed or updated. It keeps track of the current place in the Bar.

{{{

>>> b = Bar()
>>> b.current_beat
0.0
>>> b + "C"
True
>>> b.current_beat
0.25
>>> b + "D"
True
>>> b.current_beat
0.5

}}}

When a note gets added, `current_beat` gets incremented with `1 / duration`. This allows us to check in a fast way if a Bar is full or not (a common task) and how much space it has available.


=== Printing a Bar === 

When you print a Bar, this is what happens:

{{{

>>> b = Bar()
>>> b + "C"
True
>>> print b
[[0.0, 4, ['C-4']]]
>>> b + "E"
True
>>> print b
[[0.0, 4, ['C-4']], [0.25, 4, ['E-4']]]

}}}

As you might have noticed, the lists that get displayed when you print a Bar represent respectively the `current_beat` on which the NoteContainer is placed, the duration and the string representation of the NoteContainer itself. This can be handy when debugging.

----

== Edit Bars ==

Now that you know how a Bar works, you can use a couple of methods that can help reorganise a Bar. `place_notes_at(at, notes)` will add the notes to the NoteContainer at place `at` and  `change_note_duration(at, to)` will change the note duration at `at` to `to` (amazing sentence). 

----

== Using Bars as Lists ==

Just like NoteContainers, Bars can be used as lists, to some extent:

{{{

>>> b = Bar()
>>> b + "C"
True
>>> b + "E"
True
>>> b
[[0.0, 4, ['C-4']], [0.25, 4, ['E-4']]]
>>> b[0] = 'E'
>>> b
[[0.0, 4, ['E-4']], [0.25, 4, ['E-4']]]
>>> b[0]
[0.0, 4, ['E-4']]

}}}

----

== Other Methods ==

It should come as no surprise that the methods available in Note and !NoteContainer -transpose, augment, diminish, to_major and to_minor- are also available for Bars. A call to one of these functions will result into a call to that function on every !NoteContainer, which in turn calls the function on every Note. 

Some other methods and more information can be found in the reference section.

----

= End of Tutorial 3 = 

You can learn more about [refMingusContainersBar mingus.containers.Bar in the reference section].

  * [tutorialNoteModule Tutorial 1 - The Note Class]
  * [tutorialNoteContainerModule Tutorial 2 - NoteContainers]
  * Tutorial 3 - Bars
  * [tutorialInstrumentModule Tutorial 4 - Instruments]
  * [mingusIndex Back to Index]
