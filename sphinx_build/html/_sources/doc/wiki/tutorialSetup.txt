Setup
=====

Using pip
----------

1. `pip install mingus`


Installing from Source
----------------------

1. Clone https://github.com/bspaans/python-mingus or unpack the source archive
2. `python setup.py install`



Using your package manager
--------------------------

mingus might be packaged for your distribution's package manager. See :doc:`getting mingus<tutorialGettingmingus>` for a list.


----


Recommended Programs
--------------------

* You may also want to install LilyPond to generate sheet music: http://www.lilypond.org/
* Additionally, you can install FluidSynth for realtime MIDI playback support: http://fluidsynth.resonance.org/trac

Installing FluidSynth on Windows
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Installing FluidSynth on Linux and Mac shouldn't be a problem, doing it on Windows is a little bit more complex:

* Download and install QSynth (http://qsynth.sourceforge.net) which contains a patched version of FluidSynth which works on Windows.
* Add the QSynth directory to your PATH.
* In the QSynth directory, copy libfluidsynth-1.dll to libfluidsynth.dll


----

:doc:`Back to Index </index>`
