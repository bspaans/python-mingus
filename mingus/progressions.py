from .scales import Diatonic, Scale
from .notes import Note, NotesSequence
from . import chords
import re

_PROG_MATCHER = re.compile("^([IV]*)(.*)$")
_PROG_LOOKUP = {"I": 0, "II": 1, "III": 2, "IV": 3, "V": 4, "VI": 5, "VII": 6}


class Progression(object):
    def __init__(self, using_scale=None):
        self.set_scale(using_scale)

    def set_scale(self, scale):
        if scale is None:
            scale = Diatonic("C4")
        elif type(scale) is str:
            scale = Diatonic(scale)
        elif isinstance(scale, Note):
            scale = Diatonic(scale)
        if not isinstance(scale, Scale):
            raise Exception("Expecting a Scale object")
        self._scale = scale
        self._triads = scale.triads()
        self._sevenths = scale.sevenths()

    def get_scale(self):
        return self._scale

    def I(self):
        return self.first()

    def II(self):
        return self.second()

    def III(self):
        return self.third()

    def IV(self):
        return self.fourth()

    def V(self):
        return self.fifth()

    def VI(self):
        return self.sixth()

    def VII(self):
        return self.seventh()

    def I7(self):
        return self.first_seventh()

    def II7(self):
        return self.second_seventh()

    def III7(self):
        return self.third_seventh()

    def IV7(self):
        return self.fourth_seventh()

    def V7(self):
        return self.fifth_seventh()

    def VI7(self):
        return self.sixth_seventh()

    def VII7(self):
        return self.seventh_seventh()

    def first(self):
        return self.first_triad()

    def second(self):
        return self.second_triad()

    def third(self):
        return self.third_triad()

    def fourth(self):
        return self.fourth_triad()

    def fifth(self):
        return self.fifth_triad()

    def sixth(self):
        return self.sixth_triad()

    def seventh(self):
        return self.seventh_triad()

    def first_triad(self):
        return self._triads[0]

    def second_triad(self):
        return self._triads[1]

    def third_triad(self):
        return self._triads[2]

    def fourth_triad(self):
        return self._triads[3]

    def fifth_triad(self):
        return self._triads[4]

    def sixth_triad(self):
        return self._triads[5]

    def seventh_triad(self):
        return self._triads[6]

    def first_seventh(self):
        return self._sevenths[0]

    def second_seventh(self):
        return self._sevenths[1]

    def third_seventh(self):
        return self._sevenths[2]

    def fourth_seventh(self):
        return self._sevenths[3]

    def fifth_seventh(self):
        return self._sevenths[4]

    def sixth_seventh(self):
        return self._sevenths[5]

    def seventh_seventh(self):
        return self._sevenths[6]

    def __call__(self, shorthand):
        return self.from_string(shorthand)

    def from_string(self, shorthand):
        m = _PROG_MATCHER.match(shorthand)
        if m is None:
            raise Exception("Invalid format: " + shorthand)

        prog, extension = m.group(1), m.group(2)

        if prog not in _PROG_LOOKUP:
            raise Exception("Invalid progressions %s in %s" % (prog, shorthand))

        prog = _PROG_LOOKUP[prog]

        if extension == "7":
            return self._sevenths[prog]
        elif extension == "":
            return self._triads[prog]

        extension = chords.Chords.normalize_shorthand_extension(extension)
        if extension in chords.SHORTHAND:
            return chords.SHORTHAND[extension](self._triads[prog].lowest_note())
        else:
            raise Exception("Unknown shorthand extension: " + extension)

    def from_string_list(self, str_list):
        return NotesSequence(list(map(self.from_string, str_list)))
