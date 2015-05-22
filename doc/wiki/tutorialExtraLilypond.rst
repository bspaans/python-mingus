#summary The mingus.extra.LilyPond module

----

= Tutorial 1 - Generating Sheet Music with LilyPond = 

The LilyPond module provides some methods to help you generate files in the LilyPond format. This allows you to create sheet music from some of the objects in mingus.containers.

== Importing the LilyPond Module ==

{{{

>>> import mingus.extra.LilyPond as LilyPond

}}}

----

== Generate LilyPond Strings ==

LilyPond creates sheet music from files formatted in the LilyPond format. This module can convert instances of the `mingus.containers` module to formatted LilyPond strings. The functions `from_Note`, `from_NoteContainer`, `from_Bar`, `from_Track`, `from_Composition` and `from_Suite` can all be used to do that job. We will look at one simple example, to find out more about the respective functions and their arguments, you can check the [refMingusExtraLilypond reference section].

{{{

>>> b = Bar()
>>> b + "C"
>>> b + "E"
>>> b + "G"
>>> b + "B"
>>> LilyPond.from_Bar(b)
"{ \\time 4/4 \\key c \\major c'4 e'4 g'4 b'4 }"

}}}
----

== Generating Files from LilyPond Strings ==

To do something useful with the strings generated in the previous section, we can use the `to_png` and `to_pdf` functions. This does assume that you have !LilyPond installed and in your $PATH.

{{{

>>> b = Bar()
>>> b + "C"
>>> b + "E"
>>> b + "G"
>>> b + "B"
>>> bar = LilyPond.from_Bar(b)
>>> LilyPond.to_png(bar, "my_first_bar")

}}}

http://www.onderstekop.nl/dump/lpexample.png

----

= End of Tutorial 1 =

  * [mingusIndex Back to Index]
