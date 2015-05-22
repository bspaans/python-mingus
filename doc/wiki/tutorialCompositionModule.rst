#summary The mingus.containers.Composition module

----

= Tutorial 6 - Composition =

A Composition can be used to organize Tracks and to add some metadata such as `title`, `subtitle` and `author`.

== Import the Composition Class ==

{{{

>>> from mingus.containers.Composition import Composition

}}}

----

== Creating Compositions ==

The Composition class takes no argument to create:

{{{

>>> c= Composition()

}}}


== Setting Attributes ==

The `author`, `email`, `title` and `subtitle` attributes can be easily handled with the functions `set_author` and `set_title`:

{{{

>>> c = Composition()
>>> c.set_author('Author', 'author@email.com')
>>> c.set_title('First Mingus Composition')

}}}


----

This should sound pretty familiar by now:

== Adding Tracks == 

{{{

>>> c = Composition()
>>> t = Track()
>>> c.add_track(t)

}}}

== Adding Notes ==

This might seem a little strange, and you probably won't use it much. 

{{{

>>> c = Composition()
>>> c.add_note("C")

}}}

The note gets added to the tracks in `Composition.selected_tracks` which is automatically set when you use `add_track`, but which you can also use yourself.

== The Overloaded '+' Operator ==

This operator accepts Notes, note strings, !NoteContainers, Bars and Tracks.

{{{

>>> c = Composition()
>>> c + "C"

}}}

== List Notation ==

{{{
>>> c = Composition()
>>> len(c)
0
>>> c + Track()
>>> c[0] = Track
}}}

----

= End of Tutorial 6 = 

You can learn more about [refMingusContainersComposition mingus.containers.Composition] in the reference section.

  * [tutorialNoteModule Tutorial 1 - The Note Class]
  * [tutorialNoteContainerModule Tutorial 2 - NoteContainers]
  * [tutorialBarModule Tutorial 3 - Bars]
  * [tutorialInstrumentModule Tutorial 4 - Instruments]
  * [tutorialTrackModule Tutorial 5 - Tracks]
  * Tutorial 6 - Compositions
  * [tutorialSuiteModule Tutorial 7 - Suites]
  * [mingusIndex Back to Index]
