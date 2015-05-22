#summary Overview of mingus' features
#sidebar mingusSidebar

----

= Features =

== mingus 0.4 features ==

The mingus package is currently divided into four sub-packages named `core`, `containers`, `midi` and `extra`:

=== mingus.core features ===

  * Work with notes, intervals, chords, scales, keys and meters in a simple and theoretically sound way.
  * Generate natural diatonic intervals (seconds, thirds, fourths, etc) and absolute intervals (minors second, perfect fifths, etc.)
  * Generate natural diatonic triads, seventh chords, and absolute chords directly or from shorthand (min7, m/M7, etc). mingus also knows about inversions, slashed chords and polychords.
  * Refer to chords by their diatonic function (tonic, subtonic, etc. or I, ii, iii, IV, etc).
  * Generate chords from abstract chord progressions (eg. ["I", "IV", "V"]). Substitution algorithms are included.
  * Work with diatonic scales and their modes (ionian, mixolydian, etc.), generate the minor (natural, harmonic and melodic) and chromatic or whole note scales.
  * Recognize intervals, scales and hundreds of chords from lists of notes.
  * Recognize the harmonic functions of chords.

=== mingus.containers features ===

  * The Note class: can keep track of octaves, dynamics and effect and also allows you to compare Notes: eg. `Note("A") <= Note("B")` and convert to and from Hertz.
  * An Instrument class that can be subclassed. This can be used to work with the appropriate ranges, clefs, etc.
  * Data structures that group notes together in blocks of notes (!NoteContainers), Bars, Tracks, Compositions and Suites.
  * Transpose functions on Notes, NoteContainers, Bars and Tracks.

=== mingus.midi features ===

  * Can convert all the objects in mingus.containers to MIDI events.
  * Can save MIDI events - and thus mingus.containers - as MIDI files.
  * A MIDI sequencer which uses the container objects and can send timed MIDI messages to an output function.
  * Support for fluidsynth (a software MIDI synthesizer), so that objects can be played in real-time.

=== mingus.extra features ===

  * Create png's and pdf's from Bars, Tracks, Compositions and Suites using !LilyPond.

----

== Documentation ==

All functions and classes are appropriately documented  and most modules have special tutorials that walk you through their usage. Reference documentation and tutorials are accessible through the [mingusIndex wiki].

----

  * [mingusIndex Back to Index]
