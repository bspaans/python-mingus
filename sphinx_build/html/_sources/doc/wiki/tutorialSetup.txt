#summary Tips on setting up mingus
#sidebar mingusSidebar

----

= Setup =

== Installing from Source ==

  # Get the `tar.gz` archive.
  # Unpack
  # Open a terminal or 'prompt' and `cd` to the directory to which you unpacked.
  # Type `python setup.py install`

== Installing .deb or Windows Package ==

  # Get the `deb` or `exe` installer.
  # Run it.

== Installing from your default package manager ==

mingus might be packaged for your distribution's package manager. See [tutorialGettingmingus getting mingus] for a list.


== Recommended Programs == 

  # You may also want to install !LilyPond to generate sheet music: http://www.lilypond.org/
  # Additionally, you can install !FluidSynth for realtime MIDI playback support: http://fluidsynth.resonance.org/trac

=== Installing !FluidSynth on Windows ===

Installing !FluidSynth on Linux and Mac shouldn't be a problem, doing it on Windows is a little bit more complex:

  # Download and install QSynth (http://qsynth.sourceforge.net) which contains a patched version of !FluidSynth which works on Windows.
  # Add the QSynth directory to your PATH.
  # In the QSynth directory, copy libfluidsynth-1.dll to libfluidsynth.dll

----

  * [mingusIndex Back to Index]
