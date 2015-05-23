Tutorial 2 - NoteContainers
===========================

What if we want to store several Note objects at once (ie. intervals, chords)? We could use a simple list and be done with it, but we could 
also use a NoteContainer, which has some extra functionality and is used throughout this package. 




>>> from mingus.containers import NoteContainer




----


Creating a New NoteContainer 
-----------------------------

A new NoteContainer is easily created. You can create empty ones or ones already filled with notes:



>>> n = NoteContainer()
>>> n
[]
>>> n = NoteContainer(Note("A", 4))
>>> n
['A-4']
>>> n = NoteContainer("A")
>>> n
['A-4']
>>> n = NoteContainer(["A-3", "C-5", "E-5"])
>>> n
['A-3', 'C-5', 'E-5']




----


Adding Notes to a NoteContainer 
-------------------------------

Add a single note as a string ("C", "C-5", etc.) or a Note object.



>>> n = NoteContainer()
>>> n.add_note("C")
>>> n
['C-4']



Add multiple notes as a list of Note object or strings; or as another NoteContainer. Single notes still work as well. The following examples all produce the same NoteContainer:



>>> n = NoteContainer()
>>> n.add_notes(["C", "E"])





>>> n.empty()
>>> n.add_notes(NoteContainer(["C", "E"])





>>> n.empty()
>>> n.add_notes([Note("C"), Note("E")])





>>> n.empty()
>>> n.add_notes(Note("C"))
>>> n.add_notes(Note("E"))




----


Removing Notes from a NoteContainer
-----------------------------------

Remove a single note:



>>> n = NoteContainer(["C", "E", "G"])
>>> n.remove_note("E")
['C-4', 'G-4']
>>> n = NoteContainer(["C-4", "C-5"])
>>> n.remove_note("C")
[]



Removing a single note in a single octave:



>>> n = NoteContainer(["C-4", "C-5"])
>>> n.remove_note("C", 4)
['C-5']



Removing Multiple Notes from a NoteContainer
--------------------------------------------

Removing more than one note from a NoteContainer:



>>> n = NoteContainer(["C", "E", "G"])
>>> n.remove_notes(["C", "E"])
['G-4']



The function `remove_notes` accepts lists of strings and Note objects, but does also accepts all the things `remove_note` accepts.


----


Using NoteContainers as Lists 
-----------------------------

Some basic operators and functions are overloaded which will allow you to work on NoteContainers as if they were lists.



>>> n = NoteContainer(["C", "E", "G"])
>>> n[0]
'C-4'
>>> n[:-1]
['C-4', 'E-4']
>>> n[0] = "D"
>>> n
['D-4', 'E-4', 'G-4']
>>> len(n)
3




The Overloaded '+' Operator
---------------------------

The '+' operator is overloaded for NoteContainer objects. This means that you can use '+' instead of the verbose add_notes() function. 



>>> n = NoteContainer()
>>> n + "C"
['C-4']
>>> n + ["E", "G"]
["C-4", "E-4", "G-4"]




The Overloaded '-' Operator
---------------------------

The '-' operator is overloaded as well and redirects calls to `remove_notes`. It can be used like this:



>>> n = NoteContainer(["C", "E", "G"])
>>> n - "E"
['C-4', 'G-4']
>>> n - ["C", "G"]
[]



----


Other methods
-------------

The methods available in Note -transpose, augment, diminish, to_major and to_minor- are also available for NoteContainers. When one of these functions get called the NoteContainer calls the functions on every one of his Note objects.

An extra function is available to `determine` the type of chord or interval in the container.



>>> n = NoteContainer(["C", "E", "G"])
>>> n.determine()
['C major triad']
>>> n.determine(True)
['Cmaj']




----



You can learn more about `mingus.containers.NoteContainers <refMingusContainersNotecontainer>`_ in the reference section.

  * `Tutorial 1 - The Note Class <tutorialNoteModule>`_
  * Tutorial 2 - NoteContainers
  * `Tutorial 3 - Bars <tutorialBarModule>`_
  * :doc:`Back to Index </index>`
