#!/usr/bin/env python

from scales import Diatonic
import re

_PROG_MATCHER = re.compile("^([IV]*)(7?)$")
_PROG_LOOKUP = {
    "I": 0,
    "II": 1,
    "III": 2,
    "IV": 3,
    "V": 4,
    "VI": 5,
    "VII": 6
}

class Progression(object):
    def __init__(self, using_scale = None):
        self.set_scale(using_scale)

    def set_scale(self, scale):
        if scale is None:
            scale = Diatonic('C4')
        self._scale = scale
        self._triads = scale.triads()
        self._sevenths = scale.sevenths()

    def first(self):
        return self.first_triad()

    def first_triad(self):
        return self._triads[0]

    def second(self):
        return self.second_triad()

    def second_triad(self):
        return self._triads[1]

    def third(self):
        return self.third_triad()

    def third_triad(self):
        return self._triads[2]

    def fourth(self):
        return self.fourth_triad()

    def fourth_triad(self):
        return self._triads[3]

    def fifth(self):
        return self.fifth_triad()

    def fifth_triad(self):
        return self._triads[4]

    def sixth(self):
        return self.sixth_triad()

    def sixth_triad(self):
        return self._triads[5]

    def seventh(self):
        return self.seventh_triad()

    def seventh_triad(self):
        return self._triads[6]

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

        if extension == '7':
            return self._sevenths[prog]
        return self._triads[prog]
