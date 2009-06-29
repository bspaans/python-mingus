"""

================================================================================

	mingus - Music theory Python package, tablature module
	Copyright (C) 2009, Bart Spaans

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

================================================================================

        The tablature module provides the necessary functions to convert
        mingus.containers to pretty ASCII tablature. 

================================================================================
"""

import mingus.extra.tunings as tunings
import os


default_tuning = tunings.get_tuning("Guitar", "Standard", 6, 1)


def begin_track(tuning, padding = 2):
        """Helper function that builds the first few characters of every bar."""

        # find longest shorthand tuning base
        names = [ x.to_shorthand() for x in tuning.tuning ]
        basesize = len(max(names)) + 3

        # Build result
        res = []
        for x in names:
                r = " %s" % x
                spaces = basesize - len(r)
                r += " " * spaces + "||" + "-" * padding
                res.append(r)
        return res



def add_headers(width = 80, title = 'Untitled', subtitle = '', author = '', email = '', 
                description = '', tunings = []):
        """Creates a nice header in the form of a list of strings using the information \
that has been filled in. All arguments except `width` and `tunings` should be strings. \
`width` should be an integer and `tunings` a list of tunings representing the instruments."""
        result = [""]

        title = str.upper(title)
        result += [str.center("  ".join(title), width)]

        if subtitle != "":
                result += ["", str.center(str.title(subtitle), width)]
        if author != "" or email != "":
                result += ["", ""]
                if email != "":
                        result += [str.center("Written by: %s <%s>" % (author, email), width)]
                else:
                        result += [str.center("Written by: %s" % (author), width)]

        if description != '':
                result += ["", ""]
                words = description.split()
                lines = []
                line = []
                last = 0
                for word in words:
                        if len(word) + last < width - 10:
                                line.append(word)
                                last += len(word) + 1
                        else:
                                lines.append(line)
                                line = [word]
                                last = len(word) + 1
                lines.append(line)
                for line in lines:
                        result += [str.center(" ".join(line), width)]

        if tunings != []:
                result += ["", "", str.center("Instruments", width)]
                for i, tuning in enumerate(tunings):
                        result += ["", str.center("%d. %s" % (i + 1, tuning.instrument), width),
                                   str.center( tuning.description, width)]


        result += ["", ""]
        return result


def from_Note(note, width = 80, tuning = None):
        """Returns a string made out of ascii tablature representing a \
Note object or note string. `tuning` should be a StringTuning object or None \
for the default tuning."""
        if tuning is None:
                tuning = default_tuning
        result = begin_track(tuning)

        min = 1000
        s, f = -1, -1

        # Do an attribute check
        if hasattr(note, "string") and hasattr(note, "fret"):
                n = tuning.get_Note(note.string, note.fret)
                if n is not None and int(n) == int(note):
                        s, f = note.string, note.fret
                        min = 0


        # Find smallest fret (or use the attributes)
        if min == 1000:
                for string, fret in enumerate(tuning.find_frets(note)):
                        if fret is not None:
                                if fret < min:
                                        min = fret
                                        s, f = string, fret


        l = len(result[0])
        w = max(4, (width - l - 1))

        # Build ASCII
        if min != 1000:
                fret = str(f)
                for i in range(len(result)):
                        d = len(fret)
                        if i != s:
                                result[i] += "-" * w + "|"
                        else:
                                d = w - len(fret)
                                result[i] += "-" * (d / 2) + fret

                                d = w - (d / 2) - len(fret)
                                result[i] += "-" * d + "|"
                                
        else:
                #warning no fret found
                pass
        result.reverse()
        return (os.linesep).join(result)


def from_NoteContainer(notes, width = 80, tuning = None):
        """Returns a string made out of ASCII tablature representing a \
NoteContainer object or list of note strings / Note objects. `tuning` \
should be a StringTuning object or None for the default tuning."""

        if tuning is None:
                tuning = default_tuning


        result = begin_track(tuning)
        l = len(result[0])
        w = max(4, (width - l - 1))
        

        fingerings = tuning.find_fingering(notes)

        if fingerings != []:

                # Do an attribute check
                f = []
                attr = []

                for note in notes:
                        if hasattr(note, "string") and hasattr(note, "fret"):
                                n = tuning.get_Note(note.string, note.fret)
                                if n is not None and int(n) == int(note):
                                        f += ((note.string, note.fret))
                                        attr.append(int(note))

                # See if there are any possible fingerings with the 
                # attributes that are set.
                fres = []
                if f != []:
                        for x in fingerings:
                                found = True
                                for pos in f:
                                        if pos not in x:
                                                found = False
                                if found:
                                        fres.append(x)
                # Use best fingering.
                if fres != []:
                        f = fres[0]

                # Use default fingering if attributes don't make sense
                else:
                        f = fingerings[0]

                # Build {string: fret} result
                res = {}
                for string, fret in f:
                        res[string] = str(fret)
                maxfret = max(res.values())

                # Produce ASCII
                for i in range(len(result)):
                        if i not in res.keys():
                                result[i] += "-" * w + "|"
                        else:
                                d = w - len(res[i])
                                result[i] += "-" * (d / 2) + res[i]

                                d = w - (d / 2) - len(res[i])
                                result[i] += "-" * d + "|"


        else:
                #warning no fingerings
                pass

        result.reverse()
        return (os.linesep).join(result)


def from_Bar(bar, width = 40, tuning = None, collapse = True):
        """Converts a mingus.containers.Bar object to ASCII tablature. \
`tuning` should be a StringTuning object or None for the default tuning. \
If `collapse` is False this will return a list of lines, if its True all \
lines will be concatenated with a newline symbol."""

        if tuning is None:
                tuning = default_tuning

        # Size of a quarter note
        qsize = _get_qsize(tuning, width)

        result = begin_track(tuning, max(2, qsize / 2))
        
        # Add bar
        for entry in bar.bar:
                beat, duration, notes = entry
                fingering = tuning.find_fingering(notes)
                if fingering != [] or notes is None:

                        # Do an attribute check
                        f = []
                        attr = []

                        for note in notes:
                                if hasattr(note, "string") and hasattr(note, "fret"):
                                        n = tuning.get_Note(note.string, note.fret)
                                        if n is not None and int(n) == int(note):
                                                f.append((note.string, note.fret))
                                                attr.append(int(note))

                        # See if there are any possible fingerings with the 
                        # attributes that are set.
                        fres = []
                        if f != []:
                                for x in fingering:
                                        found = True
                                        for pos in f:
                                                if pos not in x:
                                                        found = False
                                        if found:
                                                fres.append(x)
                        
                        # Use best fingering.
                        maxlen = 0
                        if fres != []:
                                f = fres[0]

                        # Use default fingering if attributes don't make sense
                        else:
                                if notes is None:
                                        f = []
                                        maxlen = 1
                                else:
                                        f = fingering[0]

                        # Make {string: fret} dictionary and find highest fret
                        d = {}
                        for string, fret in f:
                                d[string] = str(fret)
                                if len(str(fret)) > maxlen:
                                        maxlen = len(str(fret))

                        # Add to result
                        for i in range(len(result)):
                                dur = int(1.0 / duration * qsize * 4) - maxlen
                                if i not in d.keys():
                                        result[i] += "-" * maxlen + "-" * dur
                                else:
                                        result[i] += ("%" + str(maxlen) + "s") % d[i] + "-" * dur
                else:
                        #warning no fingerings
                        pass

        # Padding at the end
        l = len(result[i]) + 1
        for i in range(len(result)):
                result[i] += (width - l) * "-" + "|"

        result.reverse()

        # Mark quarter notes
        pad = (" " * int(1.0 / bar.meter[1] * qsize * 4 - 1))
        r =  (" " * (result[0].find("||") + 2 + max(2, qsize /2 ))) + (("*" + pad ) * bar.meter[0])
        r += " " * (len(result[0]) - len(r))

        if not collapse:
                return [r] + result
        else:
                return (os.linesep).join([r] + result)

def from_Track(track, maxwidth = 80, tuning = None):
        """Converts a mingus.containers.Track object to an ASCII tablature string. \
`tuning` should be set to a StringTuning object or None to use the default."""

        result = []
        width = _get_width(maxwidth)

        lastlen = 0
        for bar in track:
                r = from_Bar(bar, width,  tuning, collapse = False)
                barstart = r[1].find("||") + 2

                if len(r[0]) + lastlen - barstart < maxwidth and result != []:
                        for i in range(1, len(r) + 1):
                                item = r[len(r) - i]
                                result[-i] += item[barstart:]
                else:
                        result += ["", ""] + r
                lastlen = len(result[-1])
        return (os.linesep).join(result)

def from_Composition(composition, maxwidth = 80, description = ''):
        """Converts a mingus.containers.Composition to an ASCII tablature string, \
and automatically adds an header based on the title, subtitle, author and e-mail \
attributes. An extra description of the piece can also be given."""


        result = add_headers(maxwidth, 
                             composition.title,
                             composition.subtitle, 
                             composition.author,
                             composition.email,
                             description,
                             #warning check instrument/track attributes for tunings
                             [default_tuning] * len(composition.tracks)
                            )

        # Some variables
        width = _get_width(maxwidth)
        barindex = 0
        bars = maxwidth / width
        lastlen = 0
        maxlen = max( [ len(x) for x in composition.tracks ])


        # Add Bars
        while barindex < maxlen:
                notfirst = False
                for tracks in composition:

                        #warning check tuning attribute
                        tuning = None 

                        ascii = []
                        for x in xrange(bars):
                                if barindex + x < len(tracks):

                                        bar = tracks[barindex + x]
                                        r = from_Bar(bar, width, tuning, collapse = False)
                                        barstart = r[1].find("||") + 2

                                        # Add extra '||' to quarter note marks to connect tracks.
                                        if notfirst:
                                                r[0] = r[0][:barstart - 2] + "||" +  r[0][barstart:]

                                        # Add bar to ascii
                                        if ascii != []:
                                                for i in range(1, len(r) + 1):
                                                        item = r[len(r) - i]
                                                        ascii[-i] += item[barstart:]
                                        else:
                                                ascii += r

                        # Add extra '||' to connect tracks
                        if notfirst:
                                pad = ascii[-1].find("||")
                                result += [" " * pad + "||", " " * pad + "||"]
                        else:
                                notfirst = True

                        # Finally, add ascii to result
                        result += ascii
                result += ["", "", ""]
                barindex += bars

        return (os.linesep).join(result)


def from_Suite(suite, maxwidth = 80, description = ''):
        """Converts a mingus.containers.Suite to an ASCII tablature string, \
complete with headers. A description is optional."""

        subtitle = str(len(suite.compositions)) + " Compositions" if suite.subtitle == '' else suite.subtitle
        result =  (os.linesep).join(add_headers(maxwidth, 
                             suite.title,
                             subtitle,
                             suite.author,
                             suite.email,
                             description,
                            ))
        hr = maxwidth * "=" 
        n = os.linesep
        result = n + hr + n + result + n + hr + n + n

        for comp in suite:
                c = from_Composition(comp, maxwidth)
                result += c + n + hr + n + n
        return result

def _get_qsize(tuning, width):
        """Helper function that returns a reasonable quarter note size \
for `tuning` and `width`."""
        names = [ x.to_shorthand() for x in tuning.tuning ]
        basesize = len(max(names)) + 3
        barsize = width - basesize - 2 - 1
        
        # x * 4 + 0.5x - barsize = 0
        # 4.5x = barsize
        # x = barsize / 4.5

        return int(barsize / 4.5)

def _get_width(maxwidth):
        """Helper function that returns the width of a single bar, when \
width of the page is given."""
        width = maxwidth / 3
        if maxwidth <= 60:
                width = maxwidth
        elif 60 < maxwidth <= 120:
                width = maxwidth / 2
        return width

