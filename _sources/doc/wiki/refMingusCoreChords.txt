.. module:: mingus.core.chords

==================
mingus.core.chords
==================

Module to create chords.

This module is a huge module that builds on the intervals module. It can be
used to generate and recognise a plethora of chords.

The following overview groups some of the functions you are most likely to
use together.

Generate Diatonic Chords
 * Triads
   * triad
   * triads
 * Sevenths
   * seventh
   * sevenths

Generate Absolute Chords
 * Triads
   * minor_triad
   * major_triad
   * diminished_triad
 * Sixths
   * minor_sixth
   * major_sixth
 * Sevenths
   * minor_seventh
   * major_seventh
   * dominant_seventh
   * minor_major_seventh
   * minor_seventh_flat_five
   * diminished_seventh
 * Ninths
   * minor_ninth
   * major_ninth
   * dominant_ninth
 * Elevenths
   * minor_eleventh
   * eleventh
 * Thirteenths
   * minor_thirteenth
   * major_thirteenth
   * dominant_thirteenth
 * Augmented chords
   * augmented_triad
   * augmented_major_seventh
   * augmented_minor_seventh
 * Suspended chords
   * suspended_second_triad
   * suspended_fourth_triad
   * suspended_seventh
   * suspended_fourth_ninth
   * suspended_ninth
 * Altered chords
   * dominant_flat_ninth
   * dominant_sharp_ninth
   * dominant_flat_five
   * sixth_ninth
   * hendrix_chord

Get Chords by Function
 * Function
   * tonic and tonic7
   * supertonic and supertonic7
   * mediant and mediant7
   * subdominant and subdominant7
   * dominant and dominant7
   * submediant and submediant7
 * Aliases
   * I, II, III, IV, V, VI
   * ii, iii, vi, vii
   * I7, II7, III7, IV7, V7, VI7
   * ii7, iii7, vi7

Useful Functions
 * determine - Can recognize all the chords that can be generated with from_shorthand (a lot) and their inversions.
 * from_shorthand - Generates chords from shorthand (eg. 'Cmin7')



----

.. data:: chord_shorthand

      Attribute of type: dict
      ``{'': <function major_triad at 0x7f9068b4d410>, 'm11': <function minor_eleventh at 0x7f9068b4ded8>, 'm13': <function minor_thirteenth at 0x7f9068b4df50>, '67': <function dominant_sixth at 0x7f9068b4db18>, '69': <function sixth_ninth at 0x7f9068b4db90>, '7b12': <function hendrix_chord at 0x7f9068b63578>, 'hendrix': <function hendrix_chord at 0x7f9068b63578>, 'aug': <function augmented_triad at 0x7f9068b4d578>, 'm7': <function minor_seventh at 0x7f9068b4d758>, 'm6': <function minor_sixth at 0x7f9068b4da28>, '6': <function major_sixth at 0x7f9068b4daa0>, '5': <function <lambda> at 0x7f9068b64d70>, 'm9': <function minor_ninth at 0x7f9068b4dc08>, 'm7+': <function augmented_minor_seventh at 0x7f9068b63410>, '6/7': <function dominant_sixth at 0x7f9068b4db18>, '7#11': <function lydian_dominant_seventh at 0x7f9068b63500>, '6/9': <function sixth_ninth at 0x7f9068b4db90>, '11': <function eleventh at 0x7f9068b4de60>, 'dim': <function diminished_triad at 0x7f9068b4d500>, '13': <function dominant_thirteenth at 0x7f9068b630c8>, '7b5': <function dominant_flat_five at 0x7f9068b63488>, 'm7b5': <function minor_seventh_flat_five at 0x7f9068b4d8c0>, 'susb9': <function suspended_fourth_ninth at 0x7f9068b63320>, 'mM7': <function minor_major_seventh at 0x7f9068b4d9b0>, '7b9': <function dominant_flat_ninth at 0x7f9068b4dd70>, 'M13': <function major_thirteenth at 0x7f9068b63050>, 'sus47': <function suspended_seventh at 0x7f9068b632a8>, 'm': <function minor_triad at 0x7f9068b4d488>, 'sus4b9': <function suspended_fourth_ninth at 0x7f9068b63320>, 'M7': <function major_seventh at 0x7f9068b4d6e0>, 'M6': <function major_sixth at 0x7f9068b4daa0>, 'dim7': <function diminished_seventh at 0x7f9068b4d938>, 'M7+': <function augmented_major_seventh at 0x7f9068b63398>, 'M9': <function major_ninth at 0x7f9068b4dc80>, 'dom7': <function dominant_seventh at 0x7f9068b4d7d0>, 'M7+5': <function augmented_minor_seventh at 0x7f9068b63410>, '+': <function augmented_triad at 0x7f9068b4d578>, 'sus': <function suspended_triad at 0x7f9068b63140>, '7': <function dominant_seventh at 0x7f9068b4d7d0>, '9': <function dominant_ninth at 0x7f9068b4dcf8>, 'M': <function major_triad at 0x7f9068b4d410>, '7+': <function augmented_major_seventh at 0x7f9068b63398>, 'sus2': <function suspended_second_triad at 0x7f9068b631b8>, 'sus4': <function suspended_fourth_triad at 0x7f9068b63230>, '7#5': <function augmented_minor_seventh at 0x7f9068b63410>, '7#9': <function dominant_sharp_ninth at 0x7f9068b4dde8>, 'm/M7': <function minor_major_seventh at 0x7f9068b4d9b0>}``

----

.. data:: chord_shorthand_meaning

      Attribute of type: dict
      ``{'': ' major triad', 'm11': ' minor eleventh', 'add11': ' eleventh', '67': ' dominant sixth', '69': ' sixth ninth', '7b12': ' hendrix chord', 'hendrix': ' hendrix chord', 'aug': ' augmented triad', 'm7': ' minor seventh', 'm6': ' minor sixth', '6': ' major sixth', '5': ' perfect fifth', 'm9': ' minor ninth', 'm7+': ' augmented minor seventh', '6/7': ' dominant sixth', '7#11': ' lydian dominant seventh', '6/9': ' sixth ninth', '11': ' eleventh', 'dim': ' diminished triad', '13': ' dominant thirteenth', '7b5': ' dominant flat five', 'm7b5': ' half diminished seventh', 'susb9': ' suspended fourth ninth', 'mM7': ' minor/major seventh', 'm13': ' minor thirteenth', '7b9': ' dominant flat ninth', 'M13': ' major thirteenth', 'sus47': ' suspended seventh', 'm': ' minor triad', 'sus4b9': ' suspended fourth ninth', 'M7': ' major seventh', 'M6': ' major sixth', 'dim7': ' diminished seventh', 'M7+': ' augmented major seventh', 'M9': ' major ninth', 'add13': ' dominant thirteenth', 'dom7': ' dominant seventh', 'M7+5': ' augmented minor seventh', '+': ' augmented triad', 'sus': ' suspended fourth triad', '7': ' dominant seventh', '9': ' dominant ninth', 'M': ' major triad', '7+': ' augmented major seventh', 'sus2': ' suspended second triad', 'sus4': ' suspended fourth triad', '7#5': ' augmented minor seventh', '7#9': ' dominant sharp ninth', 'm/M7': ' minor/major seventh', 'add9': ' dominant ninth', '7sus4': ' suspended seventh'}``

----

.. function:: I(key)


----

.. function:: I7(key)


----

.. function:: II(key)


----

.. function:: II7(key)


----

.. function:: III(key)


----

.. function:: III7(key)


----

.. function:: IV(key)


----

.. function:: IV7(key)


----

.. function:: V(key)


----

.. function:: V7(key)


----

.. function:: VI(key)


----

.. function:: VI7(key)


----

.. function:: VII(key)


----

.. function:: VII7(key)


----

.. function:: augmented_major_seventh(note)

      Build an augmented major seventh chord on note.
      
      Example:
      
      >>> augmented_major_seventh('C')
      ['C', 'E', 'G#', 'B']


----

.. function:: augmented_minor_seventh(note)

      Build an augmented minor seventh chord on note.
      
      Example:
      
      >>> augmented_minor_seventh('C')
      ['C', 'E', 'G#', 'Bb']


----

.. function:: augmented_triad(note)

      Build an augmented triad on note.
      
      Example:
      
      >>> augmented_triad('C')
      ['C', 'E', 'G#']


----

.. function:: determine(chord, shorthand=False, no_inversions=False, no_polychords=False)

      Name a chord.
      
      This function can determine almost every chord, from a simple triad to a
      fourteen note polychord.


----

.. function:: determine_extended_chord5(chord, shorthand=False, no_inversions=False, no_polychords=False)

      Determine the names of an extended chord.


----

.. function:: determine_extended_chord6(chord, shorthand=False, no_inversions=False, no_polychords=False)

      Determine the names of an 6 note chord.


----

.. function:: determine_extended_chord7(chord, shorthand=False, no_inversions=False, no_polychords=False)

      Determine the names of an 7 note chord.


----

.. function:: determine_polychords(chord, shorthand=False)

      Determine the polychords in chord.
      
      This function can handle anything from polychords based on two triads to
      6 note extended chords.


----

.. function:: determine_seventh(seventh, shorthand=False, no_inversion=False, no_polychords=False)

      Determine the type of seventh chord; return the results in a list,
      ordered on inversions.
      
      This function expects seventh to be a list of 4 notes.
      
      If shorthand is set to True, results will be returned in chord shorthand
      ('Cmin7', etc.); inversions will be dropped in that case.
      
      Example:
      
      >>> determine_seventh(['C', 'E', 'G', 'B'])
      ['C major seventh']


----

.. function:: determine_triad(triad, shorthand=False, no_inversions=False, placeholder=None)

      Name the triad; return answers in a list.
      
      The third argument should not be given. If shorthand is True the answers
      will be in abbreviated form.
      
      This function can determine major, minor, diminished and suspended
      triads. Also knows about invertions.
      
      Examples:
      
      >>> determine_triad(['A', 'C', 'E'])
      'A minor triad'
      >>> determine_triad(['C', 'E', 'A'])
      'A minor triad, first inversion'
      >>> determine_triad(['A', 'C', 'E'], True)
      'Am'


----

.. function:: diminished_seventh(note)

      Build a diminished seventh chord on note.
      
      Example:
      
      >>> diminished_seventh('C')
      ['C', 'Eb', 'Gb', 'Bbb']


----

.. function:: diminished_triad(note)

      Build a diminished triad on note.
      
      Example:
      
      >>> diminished_triad('C')
      ['C', 'Eb', 'Gb']


----

.. function:: dominant(key)

      Return the dominant chord in key.
      
      Example:
      
      >>> dominant('C')
      ['G', 'B', 'D']


----

.. function:: dominant7(key)

      Return the dominant seventh chord in key.


----

.. function:: dominant_flat_five(note)

      Build a dominant flat five chord on note.
      
      Example:
      
      >>> dominant_flat_five('C')
      ['C', 'E', 'Gb', 'Bb']


----

.. function:: dominant_flat_ninth(note)

      Build a dominant flat ninth chord on note.
      
      Example:
      
      >>> dominant_ninth('C')
      ['C', 'E', 'G', 'Bb', 'Db']


----

.. function:: dominant_ninth(note)

      Build a dominant ninth chord on note.
      
      Example:
      
      >>> dominant_ninth('C')
      ['C', 'E', 'G', 'Bb', 'D']


----

.. function:: dominant_seventh(note)

      Build a dominant seventh on note.
      
      Example:
      
      >>> dominant_seventh('C')
      ['C', 'E', 'G', 'Bb']


----

.. function:: dominant_sharp_ninth(note)

      Build a dominant sharp ninth chord on note.
      
      Example:
      
      >>> dominant_ninth('C')
      ['C', 'E', 'G', 'Bb', 'D#']


----

.. function:: dominant_sixth(note)

      Build the altered chord 6/7 on note.
      
      Example:
      
      >>> dominant_sixth('C')
      ['C', 'E', 'G', 'A', 'Bb']


----

.. function:: dominant_thirteenth(note)

      Build a dominant thirteenth chord on note.
      
      Example:
      
      >>> dominant_thirteenth('C')
      ['C', 'E', 'G', 'Bb', 'D', 'A']


----

.. function:: eleventh(note)

      Build an eleventh chord on note.
      
      Example:
      
      >>> eleventh('C')
      ['C', 'G', 'Bb', 'F']


----

.. function:: first_inversion(chord)

      Return the first inversion of a chord.


----

.. function:: from_shorthand(shorthand_string, slash=None)

      Take a chord written in shorthand and return the notes in the chord.
      
      The function can recognize triads, sevenths, sixths, ninths, elevenths,
      thirteenths, slashed chords and a number of altered chords.
      
      The second argument should not be given and is only used for a recursive
      call when a slashed chord or polychord is found.
      
      See http://tinyurl.com/3hn6v8u for a nice overview of chord patterns.
      
      Examples:
      
      >>> from_shorthand('Amin')
      ['A', 'C', 'E']
      >>> from_shorthand('Am/M7')
      ['A', 'C', 'E', 'G#']
      >>> from_shorthand('A')
      ['A', 'C#', 'E']
      >>> from_shorthand('A/G')
      ['G', 'A', 'C#', 'E']
      >>> from_shorthand('Dm|G')
      ['G', 'B', 'D', 'F', 'A']
      
      Recognised abbreviations: the letters "m" and "M" in the following
      abbreviations can always be substituted by respectively "min", "mi" or
      "-" and "maj" or "ma".
      
      Example:
      >>> from_shorthand('Amin7') == from_shorthand('Am7')
      True
      
      Triads: 'm', 'M' or '', 'dim'
      
      Sevenths: 'm7', 'M7', '7', 'm7b5', 'dim7', 'm/M7' or 'mM7'
      
      Augmented chords: 'aug' or '+', '7#5' or 'M7+5', 'M7+', 'm7+', '7+'
      
      Suspended chords: 'sus4', 'sus2', 'sus47' or '7sus4', 'sus', '11',
      'sus4b9' or 'susb9'
      
      Sixths: '6', 'm6', 'M6', '6/7' or '67', '6/9' or '69'
      
      Ninths: '9' or 'add9', 'M9', 'm9', '7b9', '7#9'
      
      Elevenths: '11' or 'add11', '7#11', 'm11'
      
      Thirteenths: '13' or 'add13', 'M13', 'm13'
      
      Altered chords: '7b5', '7b9', '7#9', '67' or '6/7'
      
      Special: '5', 'NC', 'hendrix'


----

.. function:: half_diminished_seventh(note)

      Build a half diminished seventh (also known as "minor seventh flat
      five") chord on note.
      
      Example:
      
      >>> half_diminished_seventh('C')
      ['C', 'Eb', 'Gb', 'Bb']


----

.. function:: hendrix_chord(note)

      Build the famous Hendrix chord (7b12).
      
      Example:
      
      >>> hendrix_chord('C')
      ['C', 'E', 'G', 'Bb', 'Eb']


----

.. function:: ii(key)


----

.. function:: ii7(key)


----

.. function:: iii(key)


----

.. function:: iii7(key)


----

.. function:: int_desc(tries)

      Return the inversion of the triad in a string.


----

.. function:: invert(chord)

      Invert a given chord one time.


----

.. function:: lydian_dominant_seventh(note)

      Build the lydian dominant seventh (7#11) on note.
      
      Example:
      
      >>> lydian_dominant_seventh('C')
      ['C', 'E', 'G', 'Bb', 'F#']


----

.. function:: major_ninth(note)

      Build a major ninth chord on note.
      
      Example:
      
      >>> major_ninth('C')
      ['C', 'E', 'G', 'B', 'D']


----

.. function:: major_seventh(note)

      Build a major seventh on note.
      
      Example:
      
      >>> major_seventh('C')
      ['C', 'E', 'G', 'B']


----

.. function:: major_sixth(note)

      Build a major sixth chord on note.
      
      Example:
      
      >>> major_sixth('C')
      ['C', 'E', 'G', 'A']


----

.. function:: major_thirteenth(note)

      Build a major thirteenth chord on note.
      
      Example:
      
      >>> major_thirteenth('C')
      ['C', 'E', 'G', 'B', 'D', 'A']


----

.. function:: major_triad(note)

      Build a major triad on note.
      
      Example:
      
      >>> major_triad('C')
      ['C', 'E', 'G']


----

.. function:: mediant(key)

      Return the mediant chord in key.
      
      Example:
      
      >>> mediant('C')
      ['E', 'G', 'B']


----

.. function:: mediant7(key)

      Returns the mediant seventh chord in key.


----

.. function:: minor_eleventh(note)

      Build a minor eleventh chord on note.
      
      Example:
      
      >>> minor_eleventh('C')
      ['C', 'Eb', 'G', 'Bb', 'F']


----

.. function:: minor_major_seventh(note)

      Build a minor major seventh chord on note.
      
      Example:
      
      >>> minor_major_seventh('C')
      ['C', 'Eb', 'G', 'B']


----

.. function:: minor_ninth(note)

      Build a minor ninth chord on note.
      
      Example:
      
      >>> minor_ninth('C')
      ['C', 'Eb', 'G', 'Bb', 'D']


----

.. function:: minor_seventh(note)

      Build a minor seventh on note.
      
      Example:
      
      >>> minor_seventh('C')
      ['C', 'Eb', 'G', 'Bb']


----

.. function:: minor_seventh_flat_five(note)

      Build a minor seventh flat five (also known as "half diminished
      seventh") chord on note.
      
      See half_diminished_seventh(note) for docs.


----

.. function:: minor_sixth(note)

      Build a minor sixth chord on note.
      
      Example:
      
      >>> minor_sixth('C')
      ['C', 'Eb', 'G', 'A']


----

.. function:: minor_thirteenth(note)

      Build a minor thirteenth chord on note.
      
      Example:
      
      >>> minor_thirteenth('C')
      ['C', 'Eb', 'G', 'Bb', 'D', 'A']


----

.. function:: minor_triad(note)

      Build a minor triad on note.
      
      Example:
      
      >>> minor_triad('C')
      ['C', 'Eb', 'G']


----

.. function:: second_inversion(chord)

      Return the second inversion of chord.


----

.. function:: seventh(note, key)

      Return the seventh chord on note in key.
      
      Example:
      
      >>> seventh('C', 'C')
      ['C', 'E', 'G', 'B']


----

.. function:: sevenths(key)

      Return all the sevenths chords in key in a list.


----

.. function:: sixth_ninth(note)

      Build the sixth/ninth chord on note.
      
      Example:
      
      >>> sixth_ninth('C')
      ['C', 'E', 'G', 'A', 'D']


----

.. function:: subdominant(key)

      Return the subdominant chord in key.
      
      Example:
      
      >>> subdominant('C')
      ['F', 'A', 'C']


----

.. function:: subdominant7(key)

      Return the subdominant seventh chord in key.


----

.. function:: submediant(key)

      Return the submediant chord in key.
      
      Example:
      
      >>> submediant('C')
      ['A', 'C', 'E']


----

.. function:: submediant7(key)

      Return the submediant seventh chord in key.


----

.. function:: subtonic(key)

      Return the subtonic chord in key.
      
      Example:
      
      >>> subtonic('C')
      ['B', 'D', 'F']


----

.. function:: subtonic7(key)

      Return the subtonic seventh chord in key.


----

.. function:: supertonic(key)

      Return the supertonic chord in key.
      
      Example:
      
      >>> supertonic('C')
      ['D', 'F', 'A']


----

.. function:: supertonic7(key)

      Return the supertonic seventh chord in key.


----

.. function:: suspended_fourth_ninth(note)

      Build a suspended fourth flat ninth chord on note.
      
      Example:
      
      >>> suspended_fourth_ninth('C')
      ['C', 'F', 'G', 'Db']


----

.. function:: suspended_fourth_triad(note)

      Build a suspended fourth triad on note.
      
      Example:
      
      >>> suspended_fourth_triad('C')
      ['C', 'F', 'G']


----

.. function:: suspended_second_triad(note)

      Build a suspended second triad on note.
      
      Example:
      
      >>> suspended_second_triad('C')
      ['C', 'D', 'G']


----

.. function:: suspended_seventh(note)

      Build a suspended (flat) seventh chord on note.
      
      Example:
      
      >>> suspended_seventh('C')
      ['C', 'F', 'G', 'Bb']


----

.. function:: suspended_triad(note)

      An alias for suspended_fourth_triad.


----

.. function:: third_inversion(chord)

      Return the third inversion of chord.


----

.. function:: tonic(key)

      Return the tonic chord in key.
      
      Examples:
      
      >>> tonic('C')
      ['C', 'E', 'G']
      >>> tonic('c')
      ['C', 'Eb', 'G']


----

.. function:: tonic7(key)

      Return the seventh chord in key.


----

.. function:: triad(note, key)

      Return the triad on note in key as a list.
      
      Examples:
      
      >>> triad('E', 'C')
      ['E', 'G', 'B']
      >>> triad('E', 'B')
      ['E', 'G#', 'B']


----

.. function:: triads(key)

      Return all the triads in key.
      
      Implemented using a cache.


----

.. function:: vi(key)


----

.. function:: vi7(key)


----

.. function:: vii(key)


----

.. function:: vii7(key)

----



:doc:`Back to Index</index>`
