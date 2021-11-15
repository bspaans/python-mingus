# -*- coding: utf-8 -*-

#    mingus - Music theory Python package, scales module.
#    Copyright (C) 2008-2009, Bart Spaans
#    Copyright (C) 2011, Carlo Stemberger
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Module for dealing with scales.

The scales module allows you to create a plethora of scales. Here's a
little overview:

The diatonic scales
 * Diatonic(note, semitones)

Ancient scales - major modes
 * Ionian(note)
 * Dorian(note)
 * Phrygian(note)
 * Lydian(note)
 * Mixolydian(note)
 * Aeolian(note)
 * Locrian(note)
 
Ancient scales - harmonic minor modes
 * LocrianNat6(note)
 * IonianSharp5(note)
 * DorianSharp4(note)
 * PhrygianDominant(note)
 * LydianSharp2(note)
 * AlteredDominantbb7(note)

 Ancient scales - melodic minor modes
 * Dorianb2(note)
 * LydianSharp5(note)
 * LydianDominant(note)
 * Mixolydianb6(note)
 * LocrianNat2(note)
 * AlteredDominant(note)
 
The major scales
 * Major(note)
 * HarmonicMajor(note)

The minor scales
 * NaturalMinor(note)
 * HarmonicMinor(note)
 * MelodicMinor(note)
 * Bachian(note)
 * MinorNeapolitan(note)

 The bebop scales 
 * MajorBebop(note)
 * DorianBebop(note)
 * AltDorianBebop(note)
 * MixolydianBebop(note) # aka dominant bebop
 * MelodicMinorBebop(note)
 * HarmonicMinorBebop(note)

Other scales
 * Chromatic(note)
 * WholeTone(note)
 * Octatonic(note)
"""
from __future__ import absolute_import

from mingus.core import intervals
from mingus.core.notes import augment, diminish, reduce_accidentals
from mingus.core.keys import keys, get_notes
from mingus.core.mt_exceptions import NoteFormatError, FormatError, RangeError
from six.moves import range


def determine(notes):
    """Determine the scales containing the notes.

    All major and minor scales are recognized.

    Example:
    >>> determine(['A', 'Bb', 'E', 'F#', 'G'])
    ['G melodic minor', 'G Bachian', 'D harmonic major']
    """
    notes = set(notes)
    res = []

    for key in keys:
        for scale in _Scale.__subclasses__():
            if scale.type == "major":
                if notes <= set(scale(key[0]).ascending()) or notes <= set(
                    scale(key[0]).descending()
                ):
                    res.append(scale(key[0]).name)
            elif scale.type == "minor":
                if notes <= set(scale(get_notes(key[1])[0]).ascending()) or notes <= set(
                    scale(get_notes(key[1])[0]).descending()
                ):
                    res.append(scale(get_notes(key[1])[0]).name)
    return res


class _Scale(object):

    """General class implementing general methods.

    Not to be used by the final user.
    """

    def __init__(self, note, octaves):
        if note.islower():
            raise NoteFormatError("Unrecognised note '%s'" % note)

        self.tonic = note
        self.octaves = octaves

    def __repr__(self):
        return "<Scale object ('{0}')>".format(self.name)

    def __str__(self):
        return "Ascending:  {0}\nDescending: {1}".format(
            " ".join(self.ascending()), " ".join(self.descending())
        )

    def __eq__(self, other):
        if self.ascending() == other.ascending():
            if self.descending() == other.descending():
                return True
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __len__(self):
        return len(self.ascending())

    def ascending(self):
        """Return the list of ascending notes."""
        raise NotImplementedError

    def descending(self):
        """Return the list of descending notes."""
        return list(reversed(self.ascending()))

    def degree(self, degree_number, direction="a"):
        """Return the asked scale degree.

        The direction of the scale is 'a' for ascending (default) and 'd'
        for descending.
        """
        if degree_number < 1:
            raise RangeError("degree '%s' out of range" % degree_number)
        if direction == "a":
            notes = self.ascending()[:-1]
            return notes[degree_number - 1]
        elif direction == "d":
            notes = list(reversed(self.descending())[:-1])
            return notes[degree_number - 1]
        else:
            raise FormatError("Unrecognised direction '%s'" % direction)


# The diatonic scales


class Diatonic(_Scale):

    """The diatonic scale.

    Example:
    >>> print Diatonic('C', (3, 7))
    Ascending:  C D E F G A B C
    Descending: C B A G F E D C
    """

    type = "diatonic"

    def __init__(self, note, semitones, octaves=1):
        """Create the diatonic scale starting on the chosen note.

        The second parameter is a tuple representing the position of
        semitones.
        """
        super(Diatonic, self).__init__(note, octaves)
        self.semitones = semitones
        self.name = "{0} diatonic, semitones in {1}".format(self.tonic, self.semitones)

    def ascending(self):
        notes = [self.tonic]
        for n in range(1, 7):
            if n in self.semitones:
                notes.append(intervals.minor_second(notes[-1]))
            else:
                notes.append(intervals.major_second(notes[-1]))
        return notes * self.octaves + [notes[0]]


# Ancient scales


class Ionian(_Scale):

    """The ionian scale.

    Example:
    >>> print Ionian('C')
    Ascending:  C D E F G A B C
    Descending: C B A G F E D C
    """

    type = "ancient"

    def __init__(self, note, octaves=1):
        """Create the ionian mode scale starting on the chosen note."""
        super(Ionian, self).__init__(note, octaves)
        self.name = "{0} ionian".format(self.tonic)

    def ascending(self):
        notes = Diatonic(self.tonic, (3, 7)).ascending()[:-1]
        return notes * self.octaves + [notes[0]]


class Dorian(_Scale):

    """The dorian scale.

    Example:
    >>> print Dorian('D')
    Ascending:  D E F G A B C D
    Descending: D C B A G F E D
    """

    type = "ancient"

    def __init__(self, note, octaves=1):
        """Create the dorian mode scale starting on the chosen note."""
        super(Dorian, self).__init__(note, octaves)
        self.name = "{0} dorian".format(self.tonic)

    def ascending(self):
        notes = Diatonic(self.tonic, (2, 6)).ascending()[:-1]
        return notes * self.octaves + [notes[0]]


class Phrygian(_Scale):

    """The phrygian scale.

    Example:
    >>> print Phrygian('E')
    Ascending:  E F G A B C D E
    Descending: E D C B A G F E
    """

    type = "ancient"

    def __init__(self, note, octaves=1):
        """Create the phrygian mode scale starting on the chosen note."""
        super(Phrygian, self).__init__(note, octaves)
        self.name = "{0} phrygian".format(self.tonic)

    def ascending(self):
        notes = Diatonic(self.tonic, (1, 5)).ascending()[:-1]
        return notes * self.octaves + [notes[0]]


class Lydian(_Scale):

    """The lydian scale.

    Example:
    >>> print Lydian('F')
    Ascending:  F G A B C D E F
    Descending: F E D C B A G F
    """

    type = "ancient"

    def __init__(self, note, octaves=1):
        """Create the lydian mode scale starting on the chosen note."""
        super(Lydian, self).__init__(note, octaves)
        self.name = "{0} lydian".format(self.tonic)

    def ascending(self):
        notes = Diatonic(self.tonic, (4, 7)).ascending()[:-1]
        return notes * self.octaves + [notes[0]]


class Mixolydian(_Scale):

    """The mixolydian scale.

    Example:
    >>> print Mixolydian('G')
    Ascending:  G A B C D E F G
    Descending: G F E D C B A G
    """

    type = "ancient"

    def __init__(self, note, octaves=1):
        """Create the mixolydian mode scale starting on the chosen note."""
        super(Mixolydian, self).__init__(note, octaves)
        self.name = "{0} mixolydian".format(self.tonic)

    def ascending(self):
        notes = Diatonic(self.tonic, (3, 6)).ascending()[:-1]
        return notes * self.octaves + [notes[0]]


class Aeolian(_Scale):

    """The aeolian scale.

    Example:
    >>> print Aeolian('A')
    Ascending:  A B C D E F G A
    Descending: A G F E D C B A
    """

    type = "ancient"

    def __init__(self, note, octaves=1):
        """Create the aeolian mode scale starting on the chosen note."""
        super(Aeolian, self).__init__(note, octaves)
        self.name = "{0} aeolian".format(self.tonic)

    def ascending(self):
        notes = Diatonic(self.tonic, (2, 5)).ascending()[:-1]
        return notes * self.octaves + [notes[0]]


class Locrian(_Scale):

    """The locrian scale.

    Example:
    >>> print Locrian('B')
    Ascending:  B C D E F G A B
    Descending: B A G F E D C B
    """

    type = "ancient"

    def __init__(self, note, octaves=1):
        """Create the locrian mode scale starting on the chosen note."""
        super(Locrian, self).__init__(note, octaves)
        self.name = "{0} locrian".format(self.tonic)

    def ascending(self):
        notes = Diatonic(self.tonic, (1, 4)).ascending()[:-1]
        return notes * self.octaves + [notes[0]]


# The major scales


class Major(_Scale):

    """The major scale.

    Example:
    >>> print Major('A')
    Ascending:  A B C# D E F# G# A
    Descending: A G# F# E D C# B A
    """

    type = "major"

    def __init__(self, note, octaves=1):
        """Create the major scale starting on the chosen note."""
        super(Major, self).__init__(note, octaves)
        self.name = "{0} major".format(self.tonic)

    def ascending(self):
        notes = get_notes(self.tonic)
        return notes * self.octaves + [notes[0]]


class HarmonicMajor(_Scale):

    """The harmonic major scale.

    Example:
    >>> print HarmonicMajor('C')
    Ascending:  C D E F G Ab B C
    Descending: C B Ab G F E D C
    """

    type = "major"

    def __init__(self, note, octaves=1):
        """Create the harmonic major scale starting on the chosen note."""
        super(HarmonicMajor, self).__init__(note, octaves)
        self.name = "{0} harmonic major".format(self.tonic)

    def ascending(self):
        notes = Major(self.tonic).ascending()[:-1]
        notes[5] = diminish(notes[5])
        return notes * self.octaves + [notes[0]]


# The minor scales


class NaturalMinor(_Scale):

    """The natural minor scale.

    Example:
    >>> print NaturalMinor('A')
    Ascending:  A B C D E F G A
    Descending: A G F E D C B A
    """

    type = "minor"

    def __init__(self, note, octaves=1):
        """Return the natural minor scale starting on the chosen note."""
        super(NaturalMinor, self).__init__(note, octaves)
        self.name = "{0} natural minor".format(self.tonic)

    def ascending(self):
        notes = get_notes(self.tonic.lower())
        return notes * self.octaves + [notes[0]]


class HarmonicMinor(_Scale):

    """The harmonic minor scale.

    Example:
    >>> print HarmonicMinor('A')
    Ascending:  A B C D E F G# A
    Descending: A G# F E D C B A
    """

    type = "minor"

    def __init__(self, note, octaves=1):
        """Create the harmonic minor scale starting on the chosen note."""
        super(HarmonicMinor, self).__init__(note, octaves)
        self.name = "{0} harmonic minor".format(self.tonic)

    def ascending(self):
        notes = NaturalMinor(self.tonic).ascending()[:-1]
        notes[6] = augment(notes[6])
        return notes * self.octaves + [notes[0]]


class MelodicMinor(_Scale):

    """The melodic minor scale.

    Example:
    >>> print MelodicMinor('A')
    Ascending:  A B C D E F# G# A
    Descending: A G F E D C B A
    """

    type = "minor"

    def __init__(self, note, octaves=1):
        """Create the melodic minor scale starting on the chosen note."""
        super(MelodicMinor, self).__init__(note, octaves)
        self.name = "{0} melodic minor".format(self.tonic)

    def ascending(self):
        notes = NaturalMinor(self.tonic).ascending()[:-1]
        notes[5] = augment(notes[5])
        notes[6] = augment(notes[6])
        return notes * self.octaves + [notes[0]]

    def descending(self):
        notes = NaturalMinor(self.tonic).descending()[:-1]
        return notes * self.octaves + [notes[0]]


class Bachian(_Scale):

    """The Bachian scale.

    Example:
    >>> print Bachian('A')
    Ascending:  A B C D E F# G# A
    Descending: A G# F# E D C B A
    """

    type = "minor"

    def __init__(self, note, octaves=1):
        """Create the Bachian (also known as "real melodic minor" and "jazz")
        scale starting on the chosen note."""
        super(Bachian, self).__init__(note, octaves)
        self.name = "{0} Bachian".format(self.tonic)

    def ascending(self):
        notes = MelodicMinor(self.tonic).ascending()[:-1]
        return notes * self.octaves + [notes[0]]


class MinorNeapolitan(_Scale):

    """The minor Neapolitan scale.

    Example:
    >>> print MinorNeapolitan('A')
    Ascending:  A Bb C D E F G# A
    Descending: A G F E D C Bb A
    """

    type = "minor"

    def __init__(self, note, octaves=1):
        """Create the minor Neapolitan scale starting on the chosen note."""
        super(MinorNeapolitan, self).__init__(note, octaves)
        self.name = "{0} minor Neapolitan".format(self.tonic)

    def ascending(self):
        notes = HarmonicMinor(self.tonic).ascending()[:-1]
        notes[1] = diminish(notes[1])
        return notes * self.octaves + [notes[0]]

    def descending(self):
        notes = NaturalMinor(self.tonic).descending()[:-1]
        notes[6] = diminish(notes[6])
        return notes * self.octaves + [notes[0]]

class LocrianNat6(_Scale):

    """The locrian natural 6 scale.

    Example:
    >>> print(LocrianNat6('C'))
    Ascending:  C Db Eb F Gb A Bb C
    Descending: C Bb A Gb F Eb Db C
    """

    type = 'ancient'

    def __init__(self, note, octaves=1):
        """Create the locrian nat6 mode scale starting on the chosen note."""
        super(LocrianNat6, self).__init__(note, octaves)
        self.name = '{0} locrian nat6'.format(self.tonic)

    def ascending(self):
        relative_tonic = TemporalNote().from_int(int(TemporalNote(self.tonic))-2).name
        notes = HarmonicMinor(relative_tonic).ascending()[:-1][1:] + HarmonicMinor(relative_tonic).ascending()[:-1][:1]
        return notes * self.octaves + [notes[0]]
    
class IonianSharp5(_Scale):

    """The ionian #5 (augmented) scale.

    Example:
    >>> print(IonianSharp5('C'))
    Ascending:  C D E F G# A B C
    Descending: C B A G# F E D C
    """

    type = 'ancient'

    def __init__(self, note, octaves=1):
        """Create the ionian #5 mode scale starting on the chosen note."""
        super(IonianSharp5, self).__init__(note, octaves)
        self.name = '{0} ionian #5'.format(self.tonic)

    def ascending(self):
        relative_tonic = TemporalNote().from_int(int(TemporalNote(self.tonic))-3).name
        notes = HarmonicMinor(relative_tonic).ascending()[:-1][2:] + HarmonicMinor(relative_tonic).ascending()[:-1][:2]
        return notes * self.octaves + [notes[0]]

class DorianSharp4(_Scale):

    """The dorian #4 scale.

    Example:
    >>> print(DorianSharp4('C'))
    Ascending:  C D Eb F# G A Bb C
    Descending: C Bb A G F# Eb D C
    """

    type = 'ancient'

    def __init__(self, note, octaves=1):
        """Create the dorian #4 mode scale starting on the chosen note."""
        super(DorianSharp4, self).__init__(note, octaves)
        self.name = '{0} dorian #4'.format(self.tonic)

    def ascending(self):
        relative_tonic = TemporalNote().from_int(int(TemporalNote(self.tonic))-5).name
        notes = HarmonicMinor(relative_tonic).ascending()[:-1][3:] + HarmonicMinor(relative_tonic).ascending()[:-1][:3]
        return notes * self.octaves + [notes[0]]

class PhrygianDominant(_Scale):

    """The phrygian dominant scale.

    Example:
    >>> print(PhrygianDominant('C'))
    Ascending:  C Db E F G Ab Bb C
    Descending: C Bb Ab G F E Db C
    """

    type = 'ancient'

    def __init__(self, note, octaves=1):
        """Create the phrygian dominant mode scale starting on the chosen note."""
        super(PhrygianDominant, self).__init__(note, octaves)
        self.name = '{0} phrygian dominant'.format(self.tonic)

    def ascending(self):
        relative_tonic = TemporalNote().from_int(int(TemporalNote(self.tonic))-7).name
        notes = HarmonicMinor(relative_tonic).ascending()[:-1][4:] + HarmonicMinor(relative_tonic).ascending()[:-1][:4]
        return notes * self.octaves + [notes[0]]

class LydianSharp2(_Scale):

    """The lydian #2 (#9) scale.

    Example:
    >>> print(LydianSharp2('C'))
    Ascending:  C D# E F# G A B C
    Descending: C B A G F# E D# C
    """

    type = 'ancient'

    def __init__(self, note, octaves=1):
        """Create the lydian #2 mode scale starting on the chosen note."""
        super(LydianSharp2, self).__init__(note, octaves)
        self.name = '{0} lydian #2'.format(self.tonic)

    def ascending(self):
        relative_tonic = TemporalNote().from_int(int(TemporalNote(self.tonic))-8).name
        notes = HarmonicMinor(relative_tonic).ascending()[:-1][5:] + HarmonicMinor(relative_tonic).ascending()[:-1][:5]
        return notes * self.octaves + [notes[0]]

class AlteredDominantbb7(_Scale):

    """The altered dominant bb7 (superlocrian bb7) scale.

    Example:
    >>> print(AlteredDominantbb7('C'))
    Ascending:  C Db Eb Fb Gb Ab Bbb C
    Descending: C Bbb Ab Gb Fb Eb Db C
    """

    type = 'ancient'

    def __init__(self, note, octaves=1):
        """Create the altered dominant bb7 (superlocrian bb7) mode scale starting on the chosen note."""
        super(AlteredDominantbb7, self).__init__(note, octaves)
        self.name = '{0} altered dominant bb7'.format(self.tonic)

    def ascending(self):
        relative_tonic = TemporalNote().from_int(int(TemporalNote(self.tonic))-11).name
        notes = HarmonicMinor(relative_tonic).ascending()[:-1][6:] + HarmonicMinor(relative_tonic).ascending()[:-1][:6]
        return notes * self.octaves + [notes[0]]

# Melodic minor modes

class Dorianb2(_Scale):

    """The dorian flat 2 (phrygian nat6) scale.

    Example:
    >>> print(Dorianb2('C'))
    Ascending:  C Db Eb F G A Bb C
    Descending: C Bb A G F Eb Db C
    """

    type = 'ancient'

    def __init__(self, note, octaves=1):
        """Create the dorian b2 mode scale starting on the chosen note."""
        super(Dorianb2, self).__init__(note, octaves)
        self.name = '{0} dorian b2'.format(self.tonic)

    def ascending(self):
        relative_tonic = TemporalNote().from_int(int(TemporalNote(self.tonic))-2).name
        notes = MelodicMinor(relative_tonic).ascending()[:-1][1:] + MelodicMinor(relative_tonic).ascending()[:-1][:1]
        return notes * self.octaves + [notes[0]]
    
class LydianSharp5(_Scale):

    """The lydian #5 (augmented) scale.

    Example:
    >>> print(LydianSharp5('C'))
    Ascending:  C D E F# G# A B C
    Descending: C B A G# F# E D C
    """

    type = 'ancient'

    def __init__(self, note, octaves=1):
        """Create the lydian #5 mode scale starting on the chosen note."""
        super(LydianSharp5, self).__init__(note, octaves)
        self.name = '{0} lydian #5'.format(self.tonic)

    def ascending(self):
        relative_tonic = TemporalNote().from_int(int(TemporalNote(self.tonic))-3).name
        notes = MelodicMinor(relative_tonic).ascending()[:-1][2:] + MelodicMinor(relative_tonic).ascending()[:-1][:2]
        return notes * self.octaves + [notes[0]]

class LydianDominant(_Scale):

    """The lydian dominant (overtone, lydian b7) scale.

    Example:
    >>> print(LydianDominant('C'))
    Ascending:  C D E F# G A Bb C
    Descending: C Bb A G F# E D C
    """

    type = 'ancient'

    def __init__(self, note, octaves=1):
        """Create the lydian dominant mode scale starting on the chosen note."""
        super(LydianDominant, self).__init__(note, octaves)
        self.name = '{0} lydian dominant'.format(self.tonic)

    def ascending(self):
        relative_tonic = TemporalNote().from_int(int(TemporalNote(self.tonic))-5).name
        notes = MelodicMinor(relative_tonic).ascending()[:-1][3:] + MelodicMinor(relative_tonic).ascending()[:-1][:3]
        return notes * self.octaves + [notes[0]]

class Mixolydianb6(_Scale):

    """The mixolydian b6 scale.

    Example:
    >>> print(Mixolydianb6('C'))
    Ascending:  C D E F G Ab Bb C
    Descending: C Bb Ab G F E D C
    """

    type = 'ancient'

    def __init__(self, note, octaves=1):
        """Create the mixolydian b6 mode scale starting on the chosen note."""
        super(Mixolydianb6, self).__init__(note, octaves)
        self.name = '{0} mixolydian b6'.format(self.tonic)

    def ascending(self):
        relative_tonic = TemporalNote().from_int(int(TemporalNote(self.tonic))-7).name
        notes = MelodicMinor(relative_tonic).ascending()[:-1][4:] + MelodicMinor(relative_tonic).ascending()[:-1][:4]
        return notes * self.octaves + [notes[0]]

class LocrianNat2(_Scale):

    """The locrian natural 2 (half-diminished) scale.

    Example:
    >>> print(LocrianNat2('C'))
    Ascending:  C D Eb F Gb Ab Bb C
    Descending: C Bb Ab Gb F Eb D C
    """

    type = 'ancient'

    def __init__(self, note, octaves=1):
        """Create the locrian natural 2 mode scale starting on the chosen note."""
        super(LocrianNat2, self).__init__(note, octaves)
        self.name = '{0} locrian nat2'.format(self.tonic)

    def ascending(self):
        relative_tonic = TemporalNote().from_int(int(TemporalNote(self.tonic))-9).name
        notes = MelodicMinor(relative_tonic).ascending()[:-1][5:] + MelodicMinor(relative_tonic).ascending()[:-1][:5]
        return notes * self.octaves + [notes[0]]

class AlteredDominant(_Scale):

    """The altered dominant (superlocrian) scale.

    Example:
    >>> print(AlteredDominant('C'))
    Ascending:  C Db Eb Fb Gb Ab Bb C
    Descending: C Bb Ab Gb Fb Eb Db C
    """

    type = 'ancient'

    def __init__(self, note, octaves=1):
        """Create the altered dominant (superlocrian) mode scale starting on the chosen note."""
        super(AlteredDominant, self).__init__(note, octaves)
        self.name = '{0} altered dominant'.format(self.tonic)

    def ascending(self):
        relative_tonic = TemporalNote().from_int(int(TemporalNote(self.tonic))-11).name
        notes = MelodicMinor(relative_tonic).ascending()[:-1][6:] + MelodicMinor(relative_tonic).ascending()[:-1][:6]
        return notes * self.octaves + [notes[0]]

# Bebop scales
        
class MajorBebop(_Scale):

    """The major bebop scale.

    Example:
    >>> print(Major('C'))
    Ascending:  C D E F G G# A B C
    Descending: C B A G# F E D C
    """

    type = 'bebop'

    def __init__(self, note, octaves=1):
        """Create the major bebop scale starting on the chosen note."""
        super(MajorBebop, self).__init__(note, octaves)
        self.name = '{0} major bebop'.format(self.tonic)

    def ascending(self):
        notes = Major(self.tonic).ascending()[:-3]
        notes.append(intervals.minor_sixth(notes[0]))
        notes += Major(self.tonic).ascending()[-3:-1]
        return notes * self.octaves + [notes[0]]
    
class DorianBebop(_Scale):

    """The dorian bebop scale.

    Example:
    >>> print(DorianBebop('C'))
    Ascending:  C D Eb E F G A Bb C
    Descending: C Bb A G F E Eb D C
    """

    type = 'bebop'

    def __init__(self, note, octaves=1):
        """Create the dorian bebop scale starting on the chosen note."""
        super(DorianBebop, self).__init__(note, octaves)
        self.name = '{0} dorian bebop'.format(self.tonic)

    def ascending(self):
        notes = Dorian(self.tonic).ascending()[:3]
        notes.append(intervals.major_third(notes[0]))
        notes += Dorian(self.tonic).ascending()[3:-1]
        return notes * self.octaves + [notes[0]]

class DorianBebopAlt(_Scale):

    """The alternative dorian bebop scale.

    Example:
    >>> print(DorianBebopAlt('C'))
    Ascending:  C D Eb F G A Bb B C
    Descending: C B Bb A G F Eb D C
    """

    type = 'bebop'

    def __init__(self, note, octaves=1):
        """Create the alternative dorian bebop scale starting on the chosen note."""
        super(DorianBebopAlt, self).__init__(note, octaves)
        self.name = '{0} alternative dorian bebop'.format(self.tonic)

    def ascending(self):
        notes = Dorian(self.tonic).ascending()[:7]
        notes.append(intervals.major_seventh(notes[0]))
        return notes * self.octaves + [notes[0]]
    
class MixolydianBebop(_Scale):

    """The mixolydian (dominant) bebop scale.

    Example:
    >>> print(MixolydianBebop('C'))
    Ascending:  C D E F G A Bb B C
    Descending: C B Bb A G F E D C
    """

    type = 'bebop'

    def __init__(self, note, octaves=1):
        """Create the mixolydian (dominant) bebop scale starting on the chosen note."""
        super(MixolydianBebop, self).__init__(note, octaves)
        self.name = '{0} mixolydian bebop'.format(self.tonic)

    def ascending(self):
        notes = Mixolydian(self.tonic).ascending()[:7]
        notes.append(intervals.major_seventh(notes[0]))
        return notes * self.octaves + [notes[0]]
    
class MelodicMinorBebop(_Scale):

    """The melodic minor bebop scale.

    Example:
    >>> print(MelodicMinorBebop('C'))
    Ascending:  C D Eb F G Ab A B C
    Descending: C B A Ab G F Eb D C
    """

    type = 'bebop'

    def __init__(self, note, octaves=1):
        """Create the melodic minor bebop scale starting on the chosen note."""
        super(MelodicMinorBebop, self).__init__(note, octaves)
        self.name = '{0} melodic minor bebop'.format(self.tonic)

    def ascending(self):
        notes = MelodicMinor(self.tonic).ascending()[:5]
        notes.append(intervals.minor_sixth(notes[0]))
        notes += MelodicMinor(self.tonic).ascending()[5:-1]
        return notes * self.octaves + [notes[0]]
    
class HarmonicMinorBebop(_Scale):

    """The harmonic minor bebop scale.

    Example:
    >>> print(HarmonicMinorBebop('C'))
    Ascending:  C D Eb F G Ab Bb B C
    Descending: C B Bb Ab G F Eb D C
    """

    type = 'bebop'

    def __init__(self, note, octaves=1):
        """Create the harmonic minor bebop scale starting on the chosen note."""
        super(HarmonicMinorBebop, self).__init__(note, octaves)
        self.name = '{0} harmonic minor bebop'.format(self.tonic)

    def ascending(self):
        notes = HarmonicMinor(self.tonic).ascending()[:6]
        notes.append(intervals.minor_seventh(notes[0]))
        notes += HarmonicMinor(self.tonic).ascending()[6:-1]
        return notes * self.octaves + [notes[0]]


# Other scales


class Chromatic(_Scale):

    """The chromatic scale.

    Examples:
    >>> print Chromatic('C')
    Ascending:  C C# D D# E F F# G G# A A# B C
    Descending: C B Bb A Ab G Gb F E Eb D Db C
    >>> print Chromatic('f')
    Ascending:  F F# G Ab A Bb B C Db D Eb E F
    Descending: F E Eb D Db C B Bb A Ab G Gb F
    """

    type = "other"

    def __init__(self, key, octaves=1):
        """Create the chromatic scale in the chosen key."""
        self.key = key
        self.tonic = get_notes(key)[0]
        self.octaves = octaves
        self.name = "{0} chromatic".format(self.tonic)

    def ascending(self):
        notes = [self.tonic]
        for note in get_notes(self.key)[1:] + [self.tonic]:
            if intervals.determine(notes[-1], note) == ("major second"):
                notes.append(augment(notes[-1]))
                notes.append(note)
            else:
                notes.append(note)
        notes.pop()
        return notes * self.octaves + [notes[0]]

    def descending(self):
        notes = [self.tonic]
        for note in reversed(get_notes(self.key)):
            if intervals.determine(note, notes[-1]) == ("major second"):
                notes.append(reduce_accidentals(diminish(notes[-1])))
                notes.append(note)
            else:
                notes.append(note)
        notes.pop()
        return notes * self.octaves + [notes[0]]


class WholeTone(_Scale):

    """The whole tone scale.

    Example:
    >>> print WholeTone('C')
    Ascending:  C D E F# G# A# C
    Descending: C A# G# F# E D C
    """

    type = "other"

    def __init__(self, note, octaves=1):
        """Create the whole tone scale starting on the chosen note."""
        super(WholeTone, self).__init__(note, octaves)
        self.name = "{0} whole tone".format(self.tonic)

    def ascending(self):
        notes = [self.tonic]
        for note in range(5):
            notes.append(intervals.major_second(notes[-1]))
        return notes * self.octaves + [notes[0]]


class Octatonic(_Scale):

    """The octatonic scale.

    Example:
    >>> print Octatonic('C')
    Ascending:  C D Eb F Gb Ab A B C
    Descending: C B A Ab Gb F Eb D C
    """

    type = "other"

    def __init__(self, note, octaves=1):
        """Create the octatonic (also known as "diminshed") scale starting
        on the chosen note."""
        super(Octatonic, self).__init__(note, octaves)
        self.name = "{0} octatonic".format(self.tonic)

    def ascending(self):
        notes = [self.tonic]
        for i in range(3):
            notes.extend([intervals.major_second(notes[-1]), intervals.minor_third(notes[-1])])
        notes.append(intervals.major_seventh(notes[0]))
        notes[-2] = intervals.major_sixth(notes[0])
        return notes * self.octaves + [notes[0]]
