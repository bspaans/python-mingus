Tutorial 7 - Suite
==================

The Suite class can be used to store compositions together and will probably not be used as much (if you want to write a symphony, knock yourself out though).


>>> from mingus.containers import Suite




----


Creating Suites
---------------

A Suite class takes no arguments to create:



>>> s = Suite()



Setting Attributes
------------------

The following functions will set some useful attributes. Note however that the authors and titles won't be reset on the actual compositions, only on the Suite:



>>> s = Suite()
>>> s.set_author('Author', 'author@email.com')
>>> s.set_title('Title', 'Subtitle')






----


Adding Compositions
-------------------



>>> c = Composition()
>>> s = Suite()
>>> s.add_composition(c)




List Notation
-------------



>>> c = Composition()
>>> len(c)
0
>>> c.add_composition(Composition())
>>> c[0] = Composition()




----


You can learn more about `mingus.containers.Suite <refMingusContainersSuite>`_ in the reference section.

  * `Tutorial 1 - The Note Class <tutorialNoteModule>`_
  * `Tutorial 2 - NoteContainers <tutorialNoteContainerModule>`_
  * `Tutorial 3 - Bars <tutorialBarModule>`_
  * `Tutorial 4 - Instruments <tutorialInstrumentModule>`_
  * `Tutorial 5 - Tracks <tutorialTrackModule>`_
  * `Tutorial 6 - Compositions <tutorialCompositionModule>`_
  * Tutorial 7 - Suites
  * :doc:`Back to Index </index>`
