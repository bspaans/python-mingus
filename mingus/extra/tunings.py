#!/usr/bin/python
# -*- coding: utf-8 -*-

#    mingus - Music theory Python package, tunings module.
#    Copyright (C) 2009, Bart Spaans
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

"""Dozens of standard tunings, a StringTuning class and some functions to help
you search through them."""

from mingus.containers.note import Note
from mingus.containers.note_container import NoteContainer
from mingus.core.mt_exceptions import RangeError
import mingus.core.notes as notes

class StringTuning(object):

    """A class to store and work with tunings and fingerings."""

    def __init__(self, instrument, description, tuning):
        """Create a new StringTuning instance.

        The instrument and description parameters should be strings; tuning
        should be a list of strings or a list of lists of strings that
        denote courses.

        See tunings.add_tuning for examples.
        """
        self.instrument = instrument
        self.tuning = []

        # convert to Note
        for x in tuning:
            if type(x) == list:
                self.tuning.append([Note(n) for n in x])
            else:
                self.tuning.append(Note(x))
        self.description = description

    def count_strings(self):
        """Return the number of strings."""
        return len(self.tuning)

    def count_courses(self):
        """Return the average number of courses per string."""
        c = 0
        for x in self.tuning:
            if type(x) == list:
                c += len(x)
            else:
                c += 1
        return float(c) / len(self.tuning)

    def find_frets(self, note, maxfret=24):
        """Return a list with for each string the fret on which the note is
        played or None if it can't be played on that particular string.

        The maxfret parameter is the highest fret that can be played; note
        should either be a string or a Note object.

        Example:
        >>> t = tunings.StringTuning('test', 'test', ['A-3', 'E-4'])
        >>> t.find_frets(Note('C-4')
        [3, None]
        >>> t.find_frets(Note('A-4')
        [12, 5]
        """
        result = []
        if type(note) == str:
            note = Note(note)
        for x in self.tuning:
            if type(x) == list:
                base = x[0]
            else:
                base = x
            diff = base.measure(note)
            if 0 <= diff <= maxfret:
                result.append(diff)
            else:
                result.append(None)
        return result

    def find_fingering(self, notes, max_distance=4, not_strings=[]):
        """Return a list [(string, fret)] of possible fingerings for
        'notes'.

        The notes parameter should be a list of strings or Notes or a
        NoteContainer; max_distance denotes the maximum distance between
        frets; not_strings can be used to disclude certain strings and is
        used internally to recurse.

        Example:
        >>> t = tunings.StringTuning('test', 'test', ['A-3', 'E-4', 'A-5'])
        >>> t.find_fingering(['E-4', 'B-4'])
        [[(0, 7), (1, 7)], [(1, 0), (0, 14)]]
        """
        if notes is None:
            return []
        if len(notes) == 0:
            return []
        first = notes[0]
        notes = notes[1:]
        frets = self.find_frets(first)
        result = []
        for (string, fret) in enumerate(frets):
            if fret is not None and string not in not_strings:
                if len(notes) > 0:
                    # recursively find fingerings for
                    # remaining notes
                    r = self.find_fingering(notes, max_distance, not_strings
                             + [string])
                    if r != []:
                        for f in r:
                            result.append([(string, fret)] + f)
                else:
                    result.append([(string, fret)])

        # filter impossible fingerings and sort
        res = []
        for r in result:
            (min, max) = (1000, -1)
            frets = 0
            for (string, fret) in r:
                if fret > max:
                    max = fret
                if fret < min and fret != 0:
                    min = fret
                frets += fret
            if 0 <= max - min < max_distance or min == 1000 or max == -1:
                res.append((frets, r))
        return [r for (_, r) in sorted(res)]

    def find_chord_fingering(self, notes, max_distance=4, maxfret=18,
            max_fingers=4, return_best_as_NoteContainer=False):
        """Return a list of fret lists that are considered possible fingerings.

        This function only looks at and matches on the note _names_ so it
        does more than find_fingering.

        Example:
        >>> t = tunings.get_tuning('guitar', 'standard', 6, 1)
        >>> t.find_chord_fingering(NoteContainer().from_chord('Am'))
        [[0, 0, 2, 2, 1, 0], [0, 3, 2, 2, 1, 0], ......]
        """
        def follow(string, next, name, prev=-1):
            """Follow the fret 'next' on 'string'; build result on the way."""
            if string >= len(self.tuning) - 1:
                return [[(next, name)]]
            result = []
            cur = res[string][next]
            if cur != []:
                for y in cur[1]:
                    for sub in follow(string + 1, y[0], y[1]):
                        if prev < 0:
                            result.append([(next, name)] + sub)
                        else:
                            if sub[0][0] == 0 or abs(sub[0][0] - prev)\
                                 < max_distance:
                                result.append([(next, name)] + sub)
            for s in follow(string + 1, maxfret + 1, None, next):
                result.append([(next, name)] + s)
            return [[(next, name)]] if result == [] else result

        def make_lookup_table():
            """Prepare the lookup table.

            table[string][fret] = (name, dest_frets)
            """
            res = [[[] for x in xrange(maxfret + 2)] for x in
                   xrange(len(self.tuning) - 1)]
            for x in xrange(0, len(self.tuning) - 1):
                addedNone = -1
                next = fretdict[x + 1]
                for (fret, name) in fretdict[x]:
                    for (f2, n2) in next:
                        if n2 != name and (f2 == 0 or abs(fret - f2)
                                 < max_distance):
                            if res[x][fret] != []:
                                res[x][fret][1].append((f2, n2))
                            else:
                                res[x][fret] = (name, [(f2, n2)])
                        if addedNone < x:
                            if res[x][maxfret + 1] != []:
                                res[x][maxfret + 1][1].append((f2, n2))
                            else:
                                res[x][maxfret + 1] = (None, [(f2, n2)])
                    addedNone = x
            return res

        # Convert to NoteContainer if necessary
        n = notes
        if notes != [] and type(notes) == list and type(notes[0]) == str:
            n = NoteContainer(notes)

        # Check number of note names.
        notenames = [x.name for x in n]
        if len(notenames) == 0 or len(notenames) > len(self.tuning):
            return []

        # Make string-fret dictionary
        fretdict = []
        for x in xrange(0, len(self.tuning)):
            fretdict.append(self.find_note_names(notes, x, maxfret))

        # Build table
        res = make_lookup_table()

        # Build result using table
        result = []

        # For each fret on the first string
        for (i, y) in enumerate(res[0]):
            if y != []:
                (yname, next) = (y[0], y[1])

                # For each destination fret in y
                for (fret, name) in next:

                    # For each followed result
                    for s in follow(1, fret, name):
                        subresult = [(i, yname)] + s

                        # Get boundaries
                        (mi, ma, names) = (1000, -1000, [])
                        for (f, n) in subresult:
                            if n is not None:
                                if f != 0 and f <= mi:
                                    mi = f
                                if f != 0 and f >= ma:
                                    ma = f
                                names.append(n)

                        # Enforce boundaries
                        if abs(ma - mi) < max_distance:
                            # Check if all note
                            # names are present
                            covered = True
                            for n in notenames:
                                if n not in names:
                                    covered = False

                            # Add to result
                            if covered and names != []:
                                result.append([y[0] if y[1]
                                         is not None else y[1] for y in
                                        subresult])

        # Return semi-sorted list
        s = sorted(result, key=lambda x: sum([t if t is not None else 1000
                   for (i, t) in enumerate(x)]))
        s = filter(lambda a: fingers_needed(a) <= max_fingers, s)
        if not return_best_as_NoteContainer:
            return s
        else:
            rnotes = self.frets_to_NoteContainer(s[0])
            for (i, x) in enumerate(rnotes):
                if x.string < len(self.tuning) - 1:
                    if res[x.string][x.fret] != []:
                        rnotes[i].name = res[x.string][x.fret][0]
            return rnotes

    def frets_to_NoteContainer(self, fingering):
        """Convert a list such as returned by find_fret to a NoteContainer."""

        res = []
        for (string, fret) in enumerate(fingering):
            if fret is not None:
                res.append(self.get_Note(string, fret))
        return NoteContainer(res)

    def find_note_names(self, notelist, string=0, maxfret=24):
        """Return a list [(fret, notename)] in ascending order.

        Notelist should be a list of Notes, note-strings or a NoteContainer.

        Example:
        >>> t = tunings.StringTuning('test', 'test', ['A-3', 'A-4'])
        >>> t.find_note_names(['A', 'C', 'E'], 0, 12)
        [(0, 'E'), (5, 'A'), (8, 'C'), (12, 'E')]
        """
        n = notelist
        if notelist != [] and type(notelist[0]) == str:
            n = NoteContainer(notelist)
        result = []
        names = [x.name for x in n]
        int_notes = [notes.note_to_int(x) for x in names]

        # Base of the string
        s = int(self.tuning[string]) % 12
        for x in xrange(0, maxfret + 1):
            if (s + x) % 12 in int_notes:
                result.append((x, names[int_notes.index((s + x) % 12)]))
        return result

    def get_Note(self, string=0, fret=0, maxfret=24):
        """Return the Note on 'string', 'fret'.

        Throw a RangeError if either the fret or string is unplayable.

        Examples:
        >>> t = tunings.StringTuning('test', 'test', ['A-3', 'A-4'])
        >>> t,get_Note(0, 0)
        'A-3'
        >>> t.get_Note(0, 1)
        'A#-3'
        >>> t.get_Note(1, 0)
        'A-4'
        """
        if 0 <= string < self.count_strings():
            if 0 <= fret <= maxfret:
                s = self.tuning[string]
                if type(s) == list:
                    s = s[0]
                n = Note(int(s) + fret)
                n.string = string
                n.fret = fret
                return n
            else:
                raise RangeError("Fret '%d' on string '%d' is out of range"
                        % (string, fret))
        else:
            raise RangeError("String '%d' out of range" % string)


def fingers_needed(fingering):
    """Return the number of fingers needed to play the given fingering."""
    split = False # True if an open string must be played, thereby making any
                  # subsequent strings impossible to bar with the index finger
    indexfinger = False # True if the index finger was already accounted for
                        # in the count
    minimum = min(finger for finger in fingering if finger) # the index finger
                                                            # plays the lowest
                                                            # finger position
    result = 0
    for finger in reversed(fingering):
        if finger == 0: # an open string is played
            split = True # subsequent strings are impossible to bar with the
                         # index finger
        else:
            if not split and finger == minimum: # if an open string hasn't been
                                                # played and this is a job for
                                                # the index finger:
                if not indexfinger: # if the index finger hasn't been accounted
                                    # for:
                    result += 1
                    indexfinger = True # index finger has now been accounted for
            else:
                result += 1
    return result

# The index
_known = {}

def add_tuning(instrument, description, tuning):
    """Add a new tuning to the index.

    The instrument and description parameters should be strings; tuning
    should be a list of strings or a list of lists to denote courses.

    Example:
    >>> std_strings = ['E-2', 'A-2', 'D-3', 'G-3', 'B-3', 'E-4']
    >>> tuning.add_tuning('Guitar', 'standard', std_strings)
    >>> tw_strings = [['E-2', 'E-3'], ['A-2', 'A-3'], ...........]
    >>> tuning.add_tuning('Guitar', 'twelve string', tw_string)
    """
    t = StringTuning(instrument, description, tuning)
    if _known.has_key(str.upper(instrument)):
        _known[str.upper(instrument)][1][str.upper(description)] = t
    else:
        _known[str.upper(instrument)] = (instrument,
                {str.upper(description): t})

def get_tuning(instrument, description, nr_of_strings=None, nr_of_courses=None):
    """Get the first tuning that satisfies the constraints.

    The instrument and description arguments are treated like
    case-insensitive prefixes. So search for 'bass' is the same is
    'Bass Guitar'.

    Example:
    >>> tunings.get_tuning('guitar', 'standard')
    <tunings.StringTuning instance at 0x139ac20>
    """
    searchi = str.upper(instrument)
    searchd = str.upper(description)
    keys = _known.keys()
    for x in keys:
        if (searchi not in keys and x.find(searchi) == 0 or searchi in keys and
                x == searchi):
            for (desc, tun) in _known[x][1].iteritems():
                if desc.find(searchd) == 0:
                    if nr_of_strings is None and nr_of_courses is None:
                        return tun
                    elif nr_of_strings is not None and nr_of_courses is None:
                        if tun.count_strings() == nr_of_strings:
                            return tun
                    elif nr_of_strings is None and nr_of_courses is not None:
                        if tun.count_courses() == nr_of_courses:
                            return tun
                    else:
                        if tun.count_courses() == nr_of_courses\
                             and tun.count_strings() == nr_of_strings:
                            return tun

def get_tunings(instrument=None, nr_of_strings=None, nr_of_courses=None):
    """Search tunings on instrument, strings, courses or a combination.

    The instrument is actually treated like a case-insensitive prefix. So
    asking for 'bass' yields the same tunings as 'Bass Guitar'; the string
    'ba' yields all the instruments starting with 'ba'.

    Example:
    >>> tunings.get_tunings(nr_of_string = 4)
    >>> tunings.get_tunings('bass')
    """
    search = ''
    if instrument is not None:
        search = str.upper(instrument)
    result = []
    keys = _known.keys()
    inkeys = search in keys
    for x in keys:
        if (instrument is None or not inkeys and x.find(search) == 0 or
                inkeys and search == x):
            if nr_of_strings is None and nr_of_courses is None:
                result += _known[x][1].values()
            elif nr_of_strings is not None and nr_of_courses is None:
                result += [y for y in _known[x][1].itervalues()
                           if y.count_strings() == nr_of_strings]
            elif nr_of_strings is None and nr_of_courses is not None:
                result += [y for y in _known[x][1].itervalues()
                           if y.count_courses() == nr_of_courses]
            else:
                result += [y for y in _known[x][1].itervalues()
                           if y.count_strings() == nr_of_strings
                            and y.count_courses() == nr_of_courses]
    return result

def get_instruments():
    """Return a sorted list of instruments that have string tunings defined
    for them."""
    return sorted([_known[upname][0] for upname in _known])

add_tuning('Baglamas (Greek)', 'Modal D standard tuning', [['D-4', 'D-5'],
           ['A-4', 'A-4'], ['D-5', 'D-5']])
add_tuning('Bajo quinto', 'Standard tuning.', [['A-2', 'A-1'], ['D-3', 'D-2'],
           ['G-2', 'G-2'], ['C-3', 'C-3'], ['F-3', 'F-3']])
add_tuning('Bajo Sexto', 'Standard tuning', [
    ['E-2', 'E-1'],
    ['A-2', 'A-1'],
    ['D-3', 'D-2'],
    ['G-2', 'G-2'],
    ['C-3', 'C-3'],
    ['F-3', 'F-3'],
    ])
add_tuning('Bandola Oriental', 'Standard tuning.', [['G-3', 'G-3'], ['D-4',
           'D-4'], ['A-4', 'A-4'], ['E-5', 'E-5']])
add_tuning('Banjo (bass)',
           'A cello banjo is sometimes called a "bass banjo",but there are true bass banjos as well'
           , ['E-1', 'A-1', 'D-2', 'G-2'])
add_tuning('Banjo (cello)', 'Standard tuning. Same as cello and mandocello',
           ['C-2', 'G-2', 'D-3', 'A-3'])
add_tuning('Banjo (tenor)', 'Standard tenor jazz tuning', ['C-3', 'G-3', 'D-4',
           'A-4'])
add_tuning('Banjo (tenor)', 'Irish tenor tuning', ['G-2', 'D-3', 'A-3', 'E-4'])
add_tuning('Banjo (5-string)', 'Open G tuning', ['G-4', 'D-3', 'G-3', 'B-3',
           'D-4'])
add_tuning('Baritone guitar', 'Standard 5th lower tuning', [
    'A-1',
    'D-2',
    'G-2',
    'C-3',
    'E-3',
    'A-3',
    ])
add_tuning('Baritone guitar', 'Octave lower tuning', [
    'E-1',
    'A-1',
    'D-2',
    'G-2',
    'B-2',
    'E-3',
    ])
add_tuning('Bass guitar', 'Standard 4-string tuning', ['E-1', 'A-1', 'D-2',
           'G-2'])
add_tuning('Bass guitar', 'Standard 5-string tuning', ['B-0', 'E-1', 'A-1',
           'D-2', 'G-2'])
add_tuning('Bass guitar', 'Alternate 5-string tuning', ['E-1', 'A-1', 'D-2',
           'G-2', 'C-3'])
add_tuning('Bass guitar', 'Standard 6-string tuning', [
    'B-0',
    'E-1',
    'A-1',
    'D-2',
    'G-2',
    'C-3',
    ])
add_tuning('Cello', 'Standard tuning', ['C-2', 'G-2', 'D-3', 'A-3'])
add_tuning('Cello', '"5th Suite" tuning', ['C-2', 'G-2', 'D-3', 'G-3'])
add_tuning('Cello banjo', 'Standard tuning', ['C-2', 'G-2', 'D-3', 'A-3'])
add_tuning('Charango', 'Standard C6 tuning. 3rd course is an octave pair.',
           [['G-4', 'G-4'], ['C-4', 'C-4'], ['E-5', 'E-4'], ['A-4', 'A-4'],
           ['E-5', 'E-5']])
add_tuning('Charangon', 'F6 tuning', [['C-4', 'C-4'], ['F-4', 'F-4'], ['A-5',
           'A-4'], ['D-5', 'D-5'], ['A-5', 'A-5']])
add_tuning('Charangon', 'G6 tuning', [['D-4', 'D-4'], ['G-4', 'G-4'], ['B-5',
           'B-4'], ['E-5', 'E-5'], ['B-5', 'B-5']])
add_tuning('Cuatro', 'Standard tuning', [['B-3', 'B-2'], ['E-4', 'E-3'], ['A-3'
           , 'A-3'], ['D-4', 'D-4'], ['G-4', 'G-4']])
add_tuning('Double bass', 'Orchestral tuning', ['E-1', 'A-1', 'D-2', 'G-2'])
add_tuning('Dulcimer',
           'Ionian Tuning (The traditional dulcimer is fretted diatonically whole, whole, half, whole, whole, half, whole. )'
           , ['A-3', 'A-3', 'D-3'])
add_tuning('Dulcimer', 'Mixolydian Tuning', ['D-4', 'A-3', 'D-3'])
add_tuning('Dulcimer', 'Dorian Tuning', ['G-3', 'A-3', 'D-3'])
add_tuning('Dulcimer', 'Aeolian Tuning', ['C-4', 'A-3', 'D-3'])
add_tuning('Fiddle', 'Standard tuning', ['G-3', 'D-4', 'A-4', 'E-5'])
add_tuning('Fiddle', 'Cajun tuning', ['F-3', 'C-4', 'G-4', 'F-5'])
add_tuning('Fiddle', 'Open G tuning', ['G-3', 'D-4', 'G-4', 'B-4'])
add_tuning('Fiddle', 'Sawmill tuning', ['G-3', 'D-4', 'G-4', 'D-5'])
add_tuning('Fiddle', '"Gee-dad"', ['G-3', 'D-4', 'A-4', 'D-5'])
add_tuning('Fiddle', 'Open D tuning', ['D-3', 'D-4', 'A-4', 'D-5'])
add_tuning('Fiddle', 'Old-timey D tuning', ['A-3', 'D-4', 'A-4', 'E-5'])
add_tuning('Fiddle', 'Cross Tuning, High bass, high counter', ['A-3', 'E-4',
           'A-4', 'E-5'])
add_tuning('Gadulka', '3 playing strings, with up to 10 sympathetic strings.',
           ['A-3', 'E-3', 'A-4'])
add_tuning('Greek Bouzouki', 'Standard F6 tuning', [['C-3', 'C-4'], ['F-3',
           'F-4'], ['A-3', 'A-3'], ['D-4', 'D-4']])
add_tuning('Greek Bouzouki', 'Standard F6 tuning', [['D-3', 'D-4'], ['A-3',
           'A-3'], ['D-4', 'D-4']])
add_tuning('Guitar', 'Standard tuning', [
    'E-2',
    'A-2',
    'D-3',
    'G-3',
    'B-3',
    'E-4',
    ])
add_tuning('Guitar', '*DADGAD* Dsus4 tuning', [
    'D-2',
    'A-2',
    'D-3',
    'G-3',
    'A-3',
    'D-4',
    ])
add_tuning('Guitar', 'Double drop D tuning', [
    'D-2',
    'A-2',
    'D-3',
    'G-3',
    'B-3',
    'D-4',
    ])
add_tuning('Guitar', 'Drop D tuning', [
    'D-2',
    'A-2',
    'D-3',
    'G-3',
    'B-3',
    'E-4',
    ])
add_tuning('Guitar', 'Open C major tuning', [
    'C-2',
    'G-2',
    'C-3',
    'G-3',
    'C-3',
    'E-4',
    ])
add_tuning('Guitar', 'Open E minor tuning', [
    'E-2',
    'B-2',
    'E-3',
    'G-3',
    'B-3',
    'E-4',
    ])
add_tuning('Guitar', 'Open G major tuning', [
    'D-2',
    'G-2',
    'D-3',
    'G-3',
    'B-3',
    'D-4',
    ])
add_tuning('Guitar',
           'Standard tuning. Some players tune the second course G string to unison to minimize breakage.'
           , [
    ['E-2', 'E-3'],
    ['A-2', 'A-3'],
    ['D-3', 'D-4'],
    ['G-3', 'G-4'],
    ['B-3', 'B-3'],
    ['E-4', 'E-4'],
    ])
add_tuning('Guitar Banjo', 'Standard guitar tuning', [
    'E-2',
    'A-2',
    'D-3',
    'G-3',
    'B-3',
    'E-4',
    ])
add_tuning("Guitarrón", 'Standard tuning', [
    'A-1',
    'D-2',
    'G-2',
    'C-3',
    'E-3',
    'A-2',
    ])
add_tuning('Huapanguera', '', ['G-2', ['D-3', 'D-4'], ['G-3', 'G-3'], ['B-3',
           'B-3'], 'E-3'])
add_tuning('Irish bouzouki', 'Irish tuning (octaves)', [['G-3', 'G-2'], ['D-4',
           'D-3'], ['A-3', 'A-3'], ['D-4', 'D-4']])
add_tuning('Irish bouzouki', 'Irish tuning (unison pairs)', [['G-2', 'G-2'],
           ['D-3', 'D-3'], ['A-3', 'A-3'], ['D-4', 'D-4']])
add_tuning('Irish bouzouki', '"Mandolin" tuning (octaves)', [['G-3', 'G-2'],
           ['D-4', 'D-3'], ['A-3', 'A-3'], ['E-4', 'E-4']])
add_tuning('Irish bouzouki', '"Mandolin" tuning (unison pairs)', [['G-2', 'G-2'
           ], ['D-3', 'D-3'], ['A-3', 'A-3'], ['E-4', 'E-4']])
add_tuning('Irish bouzouki', 'Modal D tuning (octaves)', [['A-3', 'A-2'], ['D-4'
           , 'D-3'], ['A-3', 'A-3'], ['D-4', 'D-4']])
add_tuning('Irish bouzouki', 'Modal D tuning (unison pairs)', [['A-2', 'A-2'],
           ['D-3', 'D-3'], ['A-3', 'A-3'], ['D-4', 'D-4']])
add_tuning('Mandobass', 'Standard tuning', ['E-1', 'A-1', 'D-2', 'G-2'])
add_tuning('Mandola',
           'Standard tuning. Pitched a 5th below mandolin tuning.  Known in Europe as the tenor mandola.'
           , [['C-3', 'C-3'], ['G-3', 'G-3'], ['D-4', 'D-4'], ['A-4', 'A-4']])
add_tuning('Mandocello', 'Standard tuning. Pitched an octave below the mandola.'
           , [['C-2', 'C-2'], ['G-2', 'G-2'], ['D-3', 'D-3'], ['A-3', 'A-3']])
add_tuning('Mandolin', 'Standard tuning', [['G-3', 'G-3'], ['D-4', 'D-4'],
           ['A-4', 'A-4'], ['E-5', 'E-5']])
add_tuning('Mandolin (piccolo)', 'Standard tuning', [['C-4', 'C-4'], ['G-4',
           'G-4'], ['D-5', 'D-5'], ['A-5', 'A-5']])
add_tuning('Mandolin (Octave)',
           'Standard tuning. Known in Europe as the octave mandola.  Pitched an octave below the mandolin.'
           , [['G-2', 'G-2'], ['D-3', 'D-3'], ['A-3', 'A-3'], ['E-4', 'E-4']])
add_tuning('Mejorana', 'Standard tuning', ['D-4', 'A-4', 'A-3', 'B-3', 'E-4'])
add_tuning('Mejorana', 'Alternative tuning', ['D-4', 'G-4', 'G-3', 'B-3', 'E-3'
           ])
add_tuning('Octave Guitar', 'see *Soprano guitar*', [
    'E-3',
    'A-4',
    'D-4',
    'G-4',
    'B-4',
    'E-5',
    ])
add_tuning('Requinto', 'Standard tuning', [
    'A-2',
    'D-3',
    'G-3',
    'C-4',
    'E-4',
    'A-4',
    ])
add_tuning('Ronroco', 'Standard C6 tuning (tuned an octave below the charango).'
           , [['G-3', 'G-3'], ['C-3', 'C-3'], ['E-4', 'E-3'], ['A-3', 'A-3'],
           ['E-4', 'E-4']])
add_tuning('Soprano guitar', 'Standard tuning', [
    'E-3',
    'A-4',
    'D-4',
    'G-4',
    'B-4',
    'E-5',
    ])
add_tuning('Taro patch',
           'Standard C6 tuning. The taro patch is a double-string ukulele.',
           [['G-3', 'G-4'], ['C-3', 'C-4'], ['E-4', 'E-4'], ['A-4', 'A-4']])
add_tuning('Tenor guitar', 'Standard tuning.', ['C-3', 'G-3', 'D-4', 'A-4'])
add_tuning('Tiple', 'Standard Colombian G6 tuning.', [['D-4', 'D-3', 'D-4'],
           ['G-4', 'G-3', 'G-4'], ['B-3', 'B-3', 'B-3'], ['E-4', 'E-4', 'E-4']])
add_tuning('Tres', 'Standard C major tuning', [['G-4', 'G-3'], ['C-4', 'C-4'],
           ['E-4', 'E-3']])
add_tuning('Ukulele', 'Standard C6 tuning for soprano, concert and tenor.',
           ['G-4', 'C-4', 'E-4', 'A-4'])
add_tuning('Viola', 'Standard tuning. Pitched a 5th below the violin.', ['C-3',
           'G-3', 'D-4', 'A-4'])
add_tuning('Violin', 'Standard tuning', ['G-3', 'D-4', 'A-4', 'E-5'])
add_tuning('Violin', 'Cajun tuning to accompany accordion', ['F-3', 'C-4', 'G-4'
           , 'D-5'])
add_tuning('Walaycho', 'F6 tuning', [['C-4', 'C-4'], ['F-4', 'F-4'], ['A-5',
           'A-4'], ['D-5', 'D-5'], ['A-5', 'A-5']])
add_tuning('Walaycho', 'G6 tuning', [['D-4', 'D-4'], ['G-4', 'G-4'], ['B-5',
           'B-4'], ['E-5', 'E-5'], ['B-5', 'B-5']])
