#!/usr/bin/python
# -*- coding: utf-8 -*-

#    mingus - Music theory Python package, lilypond module.
#    Copyright (C) 2008-2009, Bart Spaans
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

"""Functions to generate files in the LilyPond format.

This allows you to create sheet music from some of the objects in
mingus.containers.
"""
from mingus.containers import Note

from mingus.core.keys import Key
from mingus.containers.mt_exceptions import (NoteFormatError,
        UnexpectedObjectError)
import mingus.core.value as value
import os
import subprocess

def from_Note(note, process_octaves=True, standalone=True):
    """Get a Note object and return the LilyPond equivalent in a string.

    If process_octaves is set to False, all data regarding octaves will be
    ignored. If standalone is True, the result can be used by functions
    like to_png and will produce a valid output. The argument is mostly here
    to let from_NoteContainer make use of this function.
    """
    # Throw exception
    if not hasattr(note, 'name'):
        return False

    # Lower the case of the name
    result = note.name[0].lower()

    # Convert #'s and b's to 'is' and 'es' suffixes
    for accidental in note.name[1:]:
        if accidental == '#':
            result += 'is'
        elif accidental == 'b':
            result += 'es'

    # Place ' and , for octaves
    if process_octaves:
        oct = note.octave
        if oct >= 4:
            while oct > 3:
                result += "'"
                oct -= 1
        elif oct < 3:
            while oct < 3:
                result += ','
                oct += 1
    if standalone:
        return '{ %s }' % result
    else:
        return result

def from_NoteContainer(nc, duration=None, standalone=True):
    """Get a NoteContainer object and return the LilyPond equivalent in a
    string.

    The second argument determining the duration of the NoteContainer is
    optional. When the standalone argument is True the result of this
    function can be used directly by functions like to_png. It is mostly
    here to be used by from_Bar.
    """
    # Throw exception
    if nc is not None and not hasattr(nc, 'notes'):
        return False

    # Return rests for None or empty lists
    if nc is None or len(nc.notes) == 0:
        result = 'r'
    elif len(nc.notes) == 1:

    # Return a single note if the list contains only one note
        result = from_Note(nc.notes[0], standalone=False)
    else:
        # Return the notes grouped in '<' and '>'
        result = '<'
        for notes in nc.notes:
            result += from_Note(notes, standalone=False) + ' '
        result = result[:-1] + '>'

    # Add the duration
    if duration != None:
        parsed_value = value.determine(duration)

        # Special case: check for longa and breve in the duration (issue #37)
        dur = parsed_value[0]
        if dur == value.longa:
            result += '\\longa'
        elif dur == value.breve:
            result += '\\breve'
        else:
            result += str(int(parsed_value[0]))
        for i in range(parsed_value[1]):
            result += '.'
    if not standalone:
        return result
    else:
        return '{ %s }' % result

def from_Bar(bar, showkey=True, showtime=True):
    """Get a Bar object and return the LilyPond equivalent in a string.

    The showkey and showtime parameters can be set to determine whether the
    key and the time should be shown.
    """
    # Throw exception
    if not hasattr(bar, 'bar'):
        return False

    # Process the key
    if showkey:
        key_note = Note(bar.key.key[0].upper() + bar.key.key[1:])
        key = '\\key %s \\%s ' % (from_Note(key_note, False, standalone=False), bar.key.mode)
        result = key
    else:
        result = ''

    # Handle the NoteContainers
    latest_ratio = (1, 1)
    ratio_has_changed = False
    for bar_entry in bar.bar:
        parsed_value = value.determine(bar_entry[1])
        ratio = parsed_value[2:]
        if ratio == latest_ratio:
            result += from_NoteContainer(bar_entry[2], bar_entry[1],
                    standalone=False) + ' '
        else:
            if ratio_has_changed:
                result += '}'
            result += '\\times %d/%d {' % (ratio[1], ratio[0])
            result += from_NoteContainer(bar_entry[2], bar_entry[1],
                    standalone=False) + ' '
            latest_ratio = ratio
            ratio_has_changed = True
    if ratio_has_changed:
        result += '}'

    # Process the time
    if showtime:
        return '{ \\time %d/%d %s}' % (bar.meter[0], bar.meter[1], result)
    else:
        return '{ %s}' % result

def from_Track(track):
    """Process a Track object and return the LilyPond equivalent in a string."""
    # Throw exception
    if not hasattr(track, 'bars'):
        return False
    lastkey = Key('C')
    lasttime = (4, 4)

    # Handle the Bars:
    result = ''
    for bar in track.bars:
        if lastkey != bar.key:
            showkey = True
        else:
            showkey = False
        if lasttime != bar.meter:
            showtime = True
        else:
            showtime = False
        result += from_Bar(bar, showkey, showtime) + ' '
        lastkey = bar.key
        lasttime = bar.meter
    return '{ %s}' % result

def from_Composition(composition):
    """Return the LilyPond equivalent of a Composition in a string."""
    # warning Throw exception
    if not hasattr(composition, 'tracks'):
        return False
    result = '\\header { title = "%s" composer = "%s" opus = "%s" } '\
         % (composition.title, composition.author, composition.subtitle)
    for track in composition.tracks:
        result += from_Track(track) + ' '
    return result[:-1]

def from_Suite(suite):
    pass

def to_png(ly_string, filename):
    """Save a string in LilyPond format to a PNG.

    LilyPond in the $PATH is needed.
    """
    return save_string_and_execute_LilyPond(ly_string, filename, '-fpng')

def to_pdf(ly_string, filename):
    """Save a string in LilyPond format to a PDF.

    LilyPond in the $PATH is needed.
    """
    return save_string_and_execute_LilyPond(ly_string, filename, '-fpdf')

def save_string_and_execute_LilyPond(ly_string, filename, command):
    """A helper function for to_png and to_pdf. Should not be used directly."""
    ly_string = '\\version "2.10.33"\n' + ly_string
    if filename[-4:] in ['.pdf', '.png']:
        filename = filename[:-4]
    try:
        f = open(filename + '.ly', 'w')
        f.write(ly_string)
        f.close()
    except:
        return False
    command = 'lilypond %s -o "%s" "%s.ly"' % (command, filename, filename)
    print 'Executing: %s' % command
    p = subprocess.Popen(command, shell=True).wait()
    os.remove(filename + '.ly')
    return True
