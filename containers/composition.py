#!/usr/bin/python
# -*- coding: utf-8 -*-

#    mingus - Music theory Python package, composition module.
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

from .mt_exceptions import UnexpectedObjectError

class Composition(object):

    """A composition object.

    The Composition class is a datastructure for working with Tracks.

    Composition can be stored together in Suites.
    """

    title = 'Untitled'
    subtitle = ''
    author = ''
    email = ''
    description = ''
    tracks = []
    selected_tracks = []

    def __init__(self):
        self.empty()

    def empty(self):
        """Remove all the tracks from this class."""
        self.tracks = []

    def reset(self):
        """Reset the information in this class.

        Remove the track and composer information.
        """
        self.empty()
        self.set_title()
        self.set_author()

    def add_track(self, track):
        """Add a track to the composition.

        Raise an UnexpectedObjectError if the argument is not a
        mingus.containers.Track object.
        """
        if not hasattr(track, 'bars'):
            raise UnexpectedObjectError("Unexpected object '%s', "
                    "expecting a mingus.containers.Track object" % track)
        self.tracks.append(track)
        self.selected_tracks = [len(self.tracks) - 1]

    def add_note(self, note):
        """Add a note to the selected tracks.

        Everything container.Track supports in __add__ is accepted.
        """
        for n in self.selected_tracks:
            self.tracks[n] + note

    def set_title(self, title='Untitled', subtitle=''):
        """Set the title and subtitle of the piece."""
        self.title = title
        self.subtitle = subtitle

    def set_author(self, author='', email=''):
        """Set the title and author of the piece."""
        self.author = author
        self.email = email

    def __add__(self, value):
        """Enable the '+' operator for Compositions.

        Notes, note strings, NoteContainers, Bars and Tracks are accepted.
        """
        if hasattr(value, 'bars'):
            return self.add_track(value)
        else:
            return self.add_note(value)

    def __getitem__(self, index):
        """Enable the '[]' notation."""
        return self.tracks[index]

    def __setitem__(self, index, value):
        """Enable the '[] =' notation."""
        self.tracks[index] = value

    def __len__(self):
        """Enable the len() function."""
        return len(self.tracks)

    def __repr__(self):
        """Return a string representing the class."""
        result = ''
        for x in self.tracks:
            result += str(x)
        return result

