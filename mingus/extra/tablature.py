import mingus.extra.tunings as tunings
import mingus.core.value as value

def begin_track(tuning, padding = 2):
        names = [ x.to_shorthand() for x in tuning.tuning ]
        basesize = len(max(names)) + 3
        res = []
        for x in names:
                r = " %s" % x
                spaces = basesize - len(r)
                r += " " * spaces + "||" + "-" * padding
                res.append(r)
        return res




def from_Note(note, tuning = None):
        if tuning is None:
                tuning = tunings.get_tuning("Guitar", "Standard")

        result = begin_track(tuning)

        # Do an attribute check


        # otherwise:
        min = 1000
        s, f = -1, -1
        for string, fret in enumerate(tuning.find_frets(note)):
                if fret is not None:
                        if fret < min:
                                min = fret
                                s, f = string, fret

        if min != 1000:
                fret = str(f)
                for i in range(len(result)):
                        if i != s:
                                result[i] += "-" * len(fret) + "--|"
                        else:
                                result[i] += fret + "--|"
        else:
                #warning no fret found
                pass
        result.reverse()
        return result


def from_NoteContainer(notes, tuning = None):

        if tuning is None:
                tuning = tunings.get_tuning("Guitar", "Standard")


        result = begin_track(tuning)
        

        fingerings = tuning.find_fingering(notes)

        if fingerings != []:
                res = {}

                # Do an attribute check

                # otherwise
                f = fingerings[0]

                for string, fret in f:
                        res[string] = str(fret)
                maxfret = max(res.values())

                for i in range(len(result)):
                        if i not in res.keys():
                                result[i] += "-" * len(maxfret) + "--|"
                        else:
                                result[i] += ("%" + str(len(maxfret)) + "s") % res[i] + "--|"

        else:
                #warning no fingerings
                pass

        result.reverse()
        return result


def from_Bar(bar, width = 40, tuning = None):

        if tuning is None:
                tuning = tunings.get_tuning("Guitar", "Standard")


        qsize = _get_qsize(tuning, width)
        result = begin_track(tuning, max(2, qsize / 2))
        
        for entry in bar.bar:
                beat, duration, notes = entry
                base, dots, rat1, rat2 = value.determine(duration)
                fingering = tuning.find_fingering(notes)
                if fingering != [] or notes is None:
                        # Do an attribute check
                        
                        # Otherwise
                        maxlen = 0
                        if notes is None:
                                f = []
                                maxlen = 1
                        else:
                                f = fingering[0]
                        d = {}
                        for string, fret in f:
                                d[string] = str(fret)
                                if len(str(fret)) > maxlen:
                                        maxlen = len(str(fret))
                        for i in range(len(result)):
                                dur = int(1.0 / duration * qsize * 4) - maxlen
                                if i not in d.keys():
                                        result[i] += "-" * maxlen + "-" * dur
                                else:
                                        result[i] += ("%" + str(maxlen) + "s") % d[i] + "-" * dur
                else:
                        #warning no fingerings
                        pass
        l = len(result[i]) + 1
        for i in range(len(result)):
                result[i] += (width - l) * "-" + "|"

        result.reverse()
        return result

def from_Track(track, maxwidth = 80, tuning = None):
        result = []
        width = _get_width(maxwidth)

        lastlen = 0
        for bar in track:
                r = from_Bar(bar, width,  tuning)
                barstart = r[0].find("||") + 2

                if len(r[0]) + lastlen - barstart < maxwidth and result != []:
                        for i in range(1, len(r) + 1):
                                item = r[len(r) - i]
                                result[-i] += item[barstart:]
                else:
                        result += [""] + r
                lastlen = len(result[-1])
        return result

def from_Composition(composition, maxwidth = 80):
        result = []
        width = _get_width(maxwidth)
        barindex = 0
        bars = maxwidth / width

        lastlen = 0
        maxlen = max( [ len(x) for x in composition.tracks ])
        while barindex < maxlen:
                notfirst = False
                for tracks in composition:

                        #warning check tuning attribute
                        tuning = None 

                        ascii = []
                        for x in xrange(bars):
                                bar = tracks[barindex + x]
                                r = from_Bar(bar, width, tuning)
                                barstart = r[0].find("||") + 2
                                if ascii != []:
                                        for i in range(1, len(r) + 1):
                                                item = r[len(r) - i]
                                                ascii[-i] += item[barstart:]
                                else:
                                        ascii += r

                        if notfirst:
                                #warning should find proper width (spaces)
                                result += ["    ||"]
                        else:
                                notfirst = True
                        result += ascii
                result += [""]
                barindex += bars


        return result


def from_Suite(suite, maxwidth = 80):
        result = []

        for comp in suite:
                result += comp + ["", "", ""]
        return result

def _get_qsize(tuning, width):
        names = [ x.to_shorthand() for x in tuning.tuning ]
        basesize = len(max(names)) + 3
        barsize = width - basesize - 2 - 1
        
        # x * 4 + x / 2 - barsize = 0
        # x(4 + 0.5) - barsize= 0
        # 4.5x = barsize
        # x = barsize / 4.5

        return int(barsize / 4.5)

def _get_width(maxwidth):
        width = maxwidth / 3
        if maxwidth <= 60:
                width = maxwidth
        elif 60 < maxwidth <= 120:
                width = maxwidth / 2
        return width

