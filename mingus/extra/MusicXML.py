#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

================================================================================

    mingus - Music theory Python package, MusicXML
    Copyright (C) 2008-2009, Bart Spaans, Javier Palanca

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

    This module can convert mingus.containers to MusicXML files.
    The MusicXML format represents common Western musical notation from
    the 17th century onwards. It lets you distribute interactive sheet
    music online, and to use sheet music files with a wide variety of
    musical applications. The MusicXML format is open for use by anyone
    under a royalty-free license, and is supported by over 100 applications.

    http://www.musicxml.org/xml.html

================================================================================
"""

import xml
from xml.dom.minidom import Document
from mingus.core import notes
from mingus.core.diatonic import basic_keys
from mingus.containers.Instrument import MidiInstrument
from mingus.containers.Composition import Composition
from mingus.containers.Track import Track
from mingus.core import value
import datetime


def _gcd(a=None, b=None, terms=None):
    """Return greatest common divisor using Euclid's Algorithm."""

    if terms:
        return reduce(lambda a, b: _gcd(a, b), terms)
    else:
        while b:
            (a, b) = (b, a % b)
        return a


def _lcm(a=None, b=None, terms=None):
    """Return lowest common multiple."""

    if terms:
        return reduce(lambda a, b: _lcm(a, b), terms)
    else:
        return (a * b) / _gcd(a, b)


def _note2musicxml(note):
    doc = Document()
    note_node = doc.createElement('note')
    if note == None:

        # note is a rest

        rest = doc.createElement('rest')
        note_node.appendChild(rest)
    else:

        # add pitch info

        pitch = doc.createElement('pitch')
        step = doc.createElement('step')
        step.appendChild(doc.createTextNode(note.name[:1]))
        pitch.appendChild(step)
        octave = doc.createElement('octave')
        octave.appendChild(doc.createTextNode(str(note.octave)))
        pitch.appendChild(octave)

        # check for alterations

        count = 0
        for i in note.name[1:]:
            if i == 'b':
                count -= 1
            elif i == '#':
                count += 1
        if count != 0:
            alter = doc.createElement('alter')
            alter.appendChild(doc.createTextNode(str(count)))
            pitch.appendChild(alter)
        note_node.appendChild(pitch)
    return note_node


def _bar2musicxml(bar):
    doc = Document()
    bar_node = doc.createElement('measure')

    # bar attributes

    attributes = doc.createElement('attributes')

    # calculate divisions by using the LCM

    l = list()
    for nc in bar:
        l.append(int(value.determine(nc[1])[0]))
    lcm = _lcm(terms=l) * 4
    divisions = doc.createElement('divisions')
    divisions.appendChild(doc.createTextNode(str(lcm)))
    attributes.appendChild(divisions)
    if bar.key.name in basic_keys:
        key = doc.createElement('key')
        fifths = doc.createElement('fifths')

        # now we are going to guess which is the key of the bar

        index = basic_keys.index(bar.key.name)
        if index > 13:
            index -= 12
        fifths.appendChild(doc.createTextNode(str(index - 6)))
        mode = doc.createElement('mode')
        mode.appendChild(doc.createTextNode('major'))  # does mingus support
                                                       # more modes?
        key.appendChild(fifths)
        key.appendChild(mode)
        attributes.appendChild(key)
    time = doc.createElement('time')
    beats = doc.createElement('beats')
    beattype = doc.createElement('beat-type')
    beats.appendChild(doc.createTextNode(str(bar.meter[0])))
    beattype.appendChild(doc.createTextNode(str(bar.meter[1])))
    time.appendChild(beats)
    time.appendChild(beattype)
    attributes.appendChild(time)
    bar_node.appendChild(attributes)
    chord = doc.createElement('chord')
    for nc in bar:
        time = value.determine(nc[1])
        beat = time[0]
        note_cont = nc[2]
        is_chord = False
        if note_cont:

            # is a note_container with 2 or more notes a chord?

            if len(note_cont) > 1:
                is_chord = True
        else:
            note_cont = [None]
        for n in note_cont:
            note = _note2musicxml(n)
            if is_chord:
                note.appendChild(chord)

            # convert the duration of the note

            duration = doc.createElement('duration')
            duration.appendChild(doc.createTextNode(str(int(lcm * (4.0
                                  / beat)))))
            note.appendChild(duration)

        # check for dots

            dot = doc.createElement('dot')
            for i in range(0, time[1]):
                note.appendChild(dot)
            if beat in value.musicxml.keys():
                type_node = doc.createElement('type')
                type_node.appendChild(doc.createTextNode(value.musicxml[beat]))
                note.appendChild(type_node)

        # check for non-standard ratio

            if time[2] != 1 and time[3] != 1:
                modification = doc.createElement('time-modification')
                actual = doc.createElement('actual-notes')
                actual.appendChild(doc.createTextNode(str(time[2])))
                normal = doc.createElement('normal-notes')
                normal.appendChild(doc.createTextNode(str(time[3])))
                modification.appendChild(actual)
                modification.appendChild(normal)
                note.appendChild(modification)
            bar_node.appendChild(note)
    return bar_node


def _track2musicxml(track):
    doc = Document()
    clef = None
    track_node = doc.createElement('part')
    track_node.setAttribute('id', str(id(track)))
    if track.instrument:  # try to guess the clef of the instrument
        if 'treble' in track.instrument.clef.lower():
            clef = ('G', '2')
        elif 'bass' in track.instrument.clef.lower():
            clef = ('F', '4')
        elif 'french' in track.instrument.clef.lower():
            clef = ('G', '1')
        elif 'baritone' in track.instrument.clef.lower():
            clef = ('F', '3')
        elif 'subbass' in track.instrument.clef.lower():
            clef = ('F', '5')
        elif 'alto' in track.instrument.clef.lower():
            clef = ('C', '3')
        elif 'tenor' in track.instrument.clef.lower():
            clef = ('C', '4')
        elif 'mezzo-soprano' in track.instrument.clef.lower():
            clef = ('C', '2')
        elif 'soprano' in track.instrument.clef.lower():
            clef = ('C', '1')
    counter = 1
    for b in track.bars:
        bar = _bar2musicxml(b)
        bar.setAttribute('number', str(counter))
        if clef:
            attrs = bar.getElementsByTagName('attributes')
            for attr in attrs:
                clef_node = doc.createElement('clef')
                sign = doc.createElement('sign')
                line = doc.createElement('line')
                sign.appendChild(doc.createTextNode(clef[0]))
                line.appendChild(doc.createTextNode(clef[1]))
                clef_node.appendChild(sign)
                clef_node.appendChild(line)
                attr.appendChild(clef_node)
        track_node.appendChild(bar)
        counter += 1
    return track_node


def _composition2musicxml(comp):
    doc = Document()
    score = doc.createElement('score-partwise')
    score.setAttribute('version', '2.0')

    # set title information

    if comp.title:
        title = doc.createElement('movement-title')
        title.appendChild(doc.createTextNode(str(comp.title)))
        score.appendChild(title)
    identification = doc.createElement('identification')

    # set author information

    if comp.author:
        author = doc.createElement('creator')
        author.setAttribute('type', 'composer')
        author.appendChild(doc.createTextNode(str(comp.author)))
        identification.appendChild(author)

    # set additional info

    encoding = doc.createElement('encoding')
    software = doc.createElement('software')
    software.appendChild(doc.createTextNode('mingus'))
    encoding.appendChild(software)
    enc_date = doc.createElement('encoding-date')
    enc_date.appendChild(doc.createTextNode(str(datetime.date.today())))
    encoding.appendChild(enc_date)
    identification.appendChild(encoding)
    score.appendChild(identification)

    # add tracks

    part_list = doc.createElement('part-list')
    score.appendChild(part_list)
    for t in comp:
        track = _track2musicxml(t)
        score_part = doc.createElement('score-part')
        track.setAttribute('id', str(id(t)))
        score_part.setAttribute('id', str(id(t)))
        part_name = doc.createElement('part-name')
        part_name.appendChild(doc.createTextNode(t.name))
        score_part.appendChild(part_name)
        if t.instrument:

            # add instrument info

            score_inst = doc.createElement('score-instrument')
            score_inst.setAttribute('id', str(id(t.instrument)))
            name = doc.createElement('instrument-name')
            name.appendChild(doc.createTextNode(str(t.instrument.name)))
            score_inst.appendChild(name)
            score_part.appendChild(score_inst)

            # add midi instruments

            if isinstance(t.instrument, MidiInstrument):
                midi = doc.createElement('midi-instrument')
                midi.setAttribute('id', str(id(t.instrument)))
                channel = doc.createElement('midi-channel')
                channel.appendChild(doc.createTextNode(str(1)))  # what about the midi
                                                                 # channels?
                program = doc.createElement('midi-program')
                program.appendChild(doc.createTextNode(str(t.instrument.instrument_nr)))
                midi.appendChild(channel)
                midi.appendChild(program)
                score_part.appendChild(midi)
        part_list.appendChild(score_part)
        track.setAttribute('id', str(id(t)))
        score.appendChild(track)
    return score


def from_Note(note):
    c = Composition()
    c.add_note(note)
    return _composition2musicxml(c).toprettyxml()


def from_Bar(bar):
    c = Composition()
    t = Track()
    t.add_bar(bar)
    c.add_track(t)
    return _composition2musicxml(c).toprettyxml()


def from_Track(track):
    c = Composition()
    c.add_track(track)
    return _composition2musicxml(c).toprettyxml()


def from_Composition(comp):
    return _composition2musicxml(comp).toprettyxml()


def write_Composition(composition, filename, zip=False):
    """Creates an xml file (or mxl if compressed) for a given composition"""

    text = from_Composition(composition)
    if not zip:
        f = open(filename + '.xml', 'w')
        f.write(text)
        f.close()
    else:
        import zipfile
        import os
        zf = zipfile.ZipFile(filename + '.mxl', mode='w',
                             compression=zipfile.ZIP_DEFLATED)
        zi = zipfile.ZipInfo('META-INF' + os.sep + 'container.xml')
        zi.external_attr = 0660 << 16L
        zf.writestr(zi,
                    "<?xml version='1.0' encoding='UTF-8'?><container><rootfiles><rootfile full-path='"
                     + filename + ".xml'/></rootfiles></container>")
        zi = zipfile.ZipInfo(filename + '.xml')
        zi.external_attr = 0660 << 16L
        zf.writestr(zi, text)
        zf.close()


