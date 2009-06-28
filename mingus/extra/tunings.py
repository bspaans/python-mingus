# -*- coding: utf-8 -*-

from mingus.containers.Note import Note

class StringTuning:

        def __init__(self, instrument, tuning, description):
                self.instrument = instrument
                self.tuning = []

                for x in tuning:
                        if type(x) == list:
                                self.tuning += [Note(n) for n in x]
                        else:
                                self.tuning.append(Note(x))

                self.description = description

        def count_strings(self):
                return len(self.tuning)

        def count_courses(self):
                c = 0
                for x in self.tuning:
                        if type(x) == list:
                                c += len(x)
                        else:
                                c += 1
                return float(c) / len(self.tuning)
               

        def find_frets(self, note):
                result = []

                if type(note) == str:
                        note = Note(note)

                for x in self.tuning:
                        if type(x) == list:
                                base = x[0]
                        else:
                                base = x
                        diff = base.measure(note)
                        if 0 > diff > maxfret:
                                result.append(diff)
                        else:
                                result.append(None)

_known = {}

def add_tuning(instrument, description, tuning):
        t = StringTuning(instrument, tuning, description)
        if _known.has_key(str.upper(instrument)):
                _known[str.upper(instrument)][1][str.upper(description)] = t
        else:
                _known[str.upper(instrument)] = (instrument, {str.upper(description): t})

def get_tuning(instrument, description, nr_of_strings = None, nr_of_courses = None):
        searchi = str.upper(instrument)
        searchd = str.upper(description)

        for x in _known.iterkeys():
                if x.find(searchi) == 0:
                        for desc, tun in _known[x][1].iteritems():
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
                                                if tun.count_courses() == nr_of_courses and \
                                                   tun.count_strings() == nr_of_strings:
                                                        return tun



def get_tunings(instrument = None, nr_of_strings = None, nr_of_courses = None):
        """Allows you to search on instrument, strings, courses or a combination."""

        if instrument is not None:
                search = str.upper(instrument)

        result = []
        for x in _known.iterkeys():
                if instrument is None or x.find(search) == 0:

                        if nr_of_strings is None and nr_of_courses is None:
                                result += _known[x][1].values()

                        elif nr_of_strings is not None and nr_of_courses is None:
                                result += [ y for y in _known[x][1].itervalues() if 
                                           y.count_strings() == nr_of_strings]
                        elif nr_of_strings is None and nr_of_courses is not None:
                                result += [ y for y in _known[x][1].itervalues() if 
                                           y.count_courses() == nr_of_courses]
                        else:
                                result += [ y for y in _known[x][1].itervalues() if 
                                           y.count_strings() == nr_of_strings and \
                                      y.count_courses() == nr_of_courses]
        return result

def get_instruments():
        return sorted([ _known[upname][0] for upname in _known ])

add_tuning("Baglamas (Greek)", "Modal D standard tuning", 
                   [['D-4', 'D-5'], ['A-4', 'A-4'], ['D-5', 'D-5']])

add_tuning("Bajo quinto", "Standard tuning.", 
                   [['A-2', 'A-1'], ['D-3', 'D-2'], ['G-2', 'G-2'], 
                    ['C-3', 'C-3'], ['F-3', 'F-3']])

add_tuning("Bajo Sexto", "Standard tuning", 
                   [['E-2', 'E-1'], ['A-2', 'A-1'], ['D-3', 'D-2'], 
                    ['G-2', 'G-2'], ['C-3', 'C-3'], ['F-3', 'F-3']])

add_tuning("Bandola Oriental", "Standard tuning.", 
                   [['G-3', 'G-3'], ['D-4', 'D-4'], ['A-4', 'A-4'], 
                    ['E-5', 'E-5']])

add_tuning("banjo (bass)", "A cello banjo is sometimes called a \"bass banjo\","\
                   "but there are true bass banjos as well", 
                   ['E-1', 'A-1', 'D-2', 'G-2'])

add_tuning("banjo (cello)", "Standard tuning. Same as cello and mandocello", 
                   ['C-2', 'G-2', 'D-3', 'A-3'])

add_tuning("Banjo (tenor)", "Standard tenor jazz tuning", 
                   ['C-3', 'G-3', 'D-4', 'A-4'])

add_tuning("Banjo (tenor)", "Irish tenor tuning", 
                   ['G-2', 'D-3', 'A-3', 'E-4'])

add_tuning("Banjo (5-string)", "Open G tuning", 
                   ['G-4', 'D-3', 'G-3', 'B-3', 'D-4'])

add_tuning("Baritone guitar", "Standard 5th lower tuning", 
                   ['A-1', 'D-2', 'G-2', 'C-3', 'E-3', 'A-3'])

add_tuning("Baritone guitar", "Octave lower tuning", 
                   ['E-1', 'A-1', 'D-2', 'G-2', 'B-2', 'E-3'])

add_tuning("Bass guitar", "Standard 4-string tuning", 
                   ['E-1', 'A-1', 'D-2', 'G-2'])

add_tuning("Bass guitar", "Standard 5-string tuning", 
                   ['B-0', 'E-1', 'A-1', 'D-2', 'G-2'])

add_tuning("Bass guitar", "Alternate 5-string tuning", 
                   ['E-1', 'A-1', 'D-2', 'G-2', 'C-3'])

add_tuning("Bass guitar", "Standard 6-string tuning", 
                   ['B-0', 'E-1', 'A-1', 'D-2', 'G-2', 'C-3'])

add_tuning("Cello", "Standard tuning", ['C-2', 'G-2', 'D-3', 'A-3'])

add_tuning("Cello", "\"5th Suite\" tuning", ['C-2', 'G-2', 'D-3', 'G-3'])

add_tuning("Cello banjo", "Standard tuning", 
                   ['C-2', 'G-2', 'D-3', 'A-3'])

add_tuning("Charango", "Standard C6 tuning. 3rd course is an octave pair.", 
                   [['G-4', 'G-4'], ['C-4', 'C-4'], ['E-5', 'E-4'], 
                    ['A-4', 'A-4'], ['E-5', 'E-5']])

add_tuning("Charangon", "F6 tuning", 
                   [['C-4', 'C-4'], ['F-4', 'F-4'], ['A-5', 'A-4'], 
                    ['D-5', 'D-5'], ['A-5', 'A-5']])

add_tuning("Charangon", "G6 tuning", 
                   [['D-4', 'D-4'], ['G-4', 'G-4'], ['B-5', 'B-4'], 
                    ['E-5', 'E-5'], ['B-5', 'B-5']])

add_tuning("Cuatro", "Standard tuning", 
                   [['B-3', 'B-2'], ['E-4', 'E-3'], ['A-3', 'A-3'], 
                    ['D-4', 'D-4'], ['G-4', 'G-4']])

add_tuning("Double bass", "Orchestral tuning", 
                   ['E-1', 'A-1', 'D-2', 'G-2'])

add_tuning("Dulcimer", "Ionian Tuning (The traditional dulcimer is "\
                   "fretted diatonically whole, whole, half, whole, whole, half, whole. )", 
                   ['A-3', 'A-3', 'D-3'])

add_tuning("Dulcimer", "Mixolydian Tuning", ['D-4', 'A-3', 'D-3'])

add_tuning("Dulcimer", "Dorian Tuning", ['G-3', 'A-3', 'D-3'])

add_tuning("Dulcimer", "Aeolian Tuning", ['C-4', 'A-3', 'D-3'])

add_tuning("Fiddle", "Standard tuning", ['G-3', 'D-4', 'A-4', 'E-5'])

add_tuning("Fiddle", "Cajun tuning", ['F-3', 'C-4', 'G-4', 'F-5'])

add_tuning("Fiddle", "Open G tuning", ['G-3', 'D-4', 'G-4', 'B-4'])

add_tuning("Fiddle", "Sawmill tuning", ['G-3', 'D-4', 'G-4', 'D-5'])

add_tuning("Fiddle", "\"Gee-dad\"", ['G-3', 'D-4', 'A-4', 'D-5'])

add_tuning("Fiddle", "Open D tuning", ['D-3', 'D-4', 'A-4', 'D-5'])

add_tuning("Fiddle", "Old-timey D tuning", ['A-3', 'D-4', 'A-4', 'E-5'])

add_tuning("Fiddle", "Cross Tuning, High bass, high counter", 
                   ['A-3', 'E-4', 'A-4', 'E-5'])

add_tuning("Gadulka", "3 playing strings, with up to 10 sympathetic strings.", 
                   ['A-3', 'E-3', 'A-4'])

add_tuning("Greek Bouzouki", "Standard F6 tuning", 
                   [['C-3', 'C-4'], ['F-3', 'F-4'], ['A-3', 'A-3'], ['D-4', 'D-4']])

add_tuning("Greek Bouzouki", "Standard F6 tuning", 
                   [['D-3', 'D-4'], ['A-3', 'A-3'], ['D-4', 'D-4']])

add_tuning("Guitar", "Standard tuning", 
                   ['E-2', 'A-2', 'D-3', 'G-3', 'B-3', 'E-4'])

add_tuning("Guitar", "*DADGAD* Dsus4 tuning", 
                   ['D-2', 'A-2', 'D-3', 'G-3', 'A-3', 'D-4'])

add_tuning("Guitar", "Double drop D tuning", 
                   ['D-2', 'A-2', 'D-3', 'G-3', 'B-3', 'D-4'])

add_tuning("Guitar", "Drop D tuning", 
                   ['D-2', 'A-2', 'D-3', 'G-3', 'B-3', 'E-4'])

add_tuning("Guitar", "Open C major tuning", 
                   ['C-2', 'G-2', 'C-3', 'G-3', 'C-3', 'E-4'])

add_tuning("Guitar", "Open E minor tuning", 
                   ['E-2', 'B-2', 'E-3', 'G-3', 'B-3', 'E-4'])

add_tuning("Guitar", "Open G major tuning", 
                   ['D-2', 'G-2', 'D-3', 'G-3', 'B-3', 'D-4'])

add_tuning("Guitar", "Standard tuning. Some players tune the second "\
                   "course G string to unison to minimize breakage.", 
                   [['E-2', 'E-3'], ['A-2', 'A-3'], ['D-3', 'D-4'], 
                    ['G-3', 'G-4'], ['B-3', 'B-3'], ['E-4', 'E-4']])

add_tuning("Guitar Banjo", "Standard guitar tuning", 
                   ['E-2', 'A-2', 'D-3', 'G-3', 'B-3', 'E-4'])

add_tuning("Guitarrón", "Standard tuning", 
                   ['A-1', 'D-2', 'G-2', 'C-3', 'E-3', 'A-2'])

add_tuning("Huapanguera", "", 
                   ['G-2', ['D-3', 'D-4'], ['G-3', 'G-3'], 
                    ['B-3', 'B-3'], 'E-3'])

add_tuning("Irish bouzouki", "Irish tuning (octaves)", 
                   [['G-3', 'G-2'], ['D-4', 'D-3'], 
                    ['A-3', 'A-3'], ['D-4', 'D-4']])

add_tuning("Irish bouzouki", "Irish tuning (unison pairs)", 
                   [['G-2', 'G-2'], ['D-3', 'D-3'], 
                    ['A-3', 'A-3'], ['D-4', 'D-4']])

add_tuning("Irish bouzouki", "\"Mandolin\" tuning (octaves)", 
                   [['G-3', 'G-2'], ['D-4', 'D-3'],
                    ['A-3', 'A-3'], ['E-4', 'E-4']])

add_tuning("Irish bouzouki", "\"Mandolin\" tuning (unison pairs)", 
                   [['G-2', 'G-2'], ['D-3', 'D-3'],
                    ['A-3', 'A-3'], ['E-4', 'E-4']])

add_tuning("Irish bouzouki", "Modal D tuning (octaves)", 
                   [['A-3', 'A-2'], ['D-4', 'D-3'],
                    ['A-3', 'A-3'], ['D-4', 'D-4']])

add_tuning("Irish bouzouki", "Modal D tuning (unison pairs)", 
                   [['A-2', 'A-2'], ['D-3', 'D-3'],
                    ['A-3', 'A-3'], ['D-4', 'D-4']])

add_tuning("Mandobass", "Standard tuning",
                   ['E-1', 'A-1', 'D-2', 'G-2'])

add_tuning("Mandola", "Standard tuning. Pitched a 5th below mandolin "\
                   "tuning.  Known in Europe as the tenor mandola.", 
                   [['C-3', 'C-3'], ['G-3', 'G-3'], 
                    ['D-4', 'D-4'], ['A-4', 'A-4']])

add_tuning("Mandocello", "Standard tuning. Pitched an octave below the mandola.", 
                   [['C-2', 'C-2'], ['G-2', 'G-2'], 
                    ['D-3', 'D-3'], ['A-3', 'A-3']])

add_tuning("Mandolin", "Standard tuning", 
                   [['G-3', 'G-3'], ['D-4', 'D-4'], 
                    ['A-4', 'A-4'], ['E-5', 'E-5']])

add_tuning("Mandolin (piccolo)", "Standard tuning", 
                   [['C-4', 'C-4'], ['G-4', 'G-4'],
                    ['D-5', 'D-5'], ['A-5', 'A-5']])

add_tuning("Mandolin (Octave)", "Standard tuning. Known in Europe as the octave mandola. "\
                   " Pitched an octave below the mandolin.", 
                   [['G-2', 'G-2'], ['D-3', 'D-3'],
                    ['A-3', 'A-3'], ['E-4', 'E-4']])

add_tuning("Mejorana", "Standard tuning", 
                   ['D-4', 'A-4', 'A-3', 'B-3', 'E-4'])

add_tuning("Mejorana", "Alternative tuning", 
                   ['D-4', 'G-4', 'G-3', 'B-3', 'E-3'])

add_tuning("Octave Guitar", "see *Soprano guitar*", 
                   ['E-3', 'A-4', 'D-4', 'G-4', 'B-4', 'E-5'])

add_tuning("Requinto", "Standard tuning", 
                   ['A-2', 'D-3', 'G-3', 'C-4', 'E-4', 'A-4'])

add_tuning("Ronroco", "Standard C6 tuning (tuned an octave below the charango).", 
                   [['G-3', 'G-3'], ['C-3', 'C-3'], ['E-4', 'E-3'], 
                    ['A-3', 'A-3'], ['E-4', 'E-4']])

add_tuning("Soprano guitar", "Standard tuning", 
                   ['E-3', 'A-4', 'D-4', 'G-4', 'B-4', 'E-5'])

add_tuning("Taro patch", "Standard C6 tuning. The taro patch is a double-string ukulele.", 
                   [['G-3', 'G-4'], ['C-3', 'C-4'], 
                    ['E-4', 'E-4'], ['A-4', 'A-4']])

add_tuning("Tenor guitar", "Standard tuning.", 
                   ['C-3', 'G-3', 'D-4', 'A-4'])

add_tuning("Tiple", "Standard Colombian G6 tuning.", 
                   [['D-4', 'D-3', 'D-4'], ['G-4', 'G-3', 'G-4'], 
                    ['B-3', 'B-3', 'B-3'], ['E-4', 'E-4', 'E-4']])

add_tuning("Tres", "Standard C major tuning", 
                   [['G-4', 'G-3'], ['C-4', 'C-4'], ['E-4', 'E-3']])

add_tuning("Ukulele", "Standard C6 tuning for soprano, concert and tenor.", 
                   ['G-4', 'C-4', 'E-4', 'A-4'])

add_tuning("Viola", "Standard tuning. Pitched a 5th below the violin.", 
                   ['C-3', 'G-3', 'D-4', 'A-4'])

add_tuning("Violin", "Standard tuning", ['G-3', 'D-4', 'A-4', 'E-5'])

add_tuning("Violin", "Cajun tuning to accompany accordion", 
                   ['F-3', 'C-4', 'G-4', 'D-5'])

add_tuning("Walaycho", "F6 tuning", 
                   [['C-4', 'C-4'], ['F-4', 'F-4'], ['A-5', 'A-4'], 
                    ['D-5', 'D-5'], ['A-5', 'A-5']])

add_tuning("Walaycho", "G6 tuning", 
                   [['D-4', 'D-4'], ['G-4', 'G-4'], ['B-5', 'B-4'],
                    ['E-5', 'E-5'], ['B-5', 'B-5']])









print get_instruments()
