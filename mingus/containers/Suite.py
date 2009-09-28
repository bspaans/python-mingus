"""

================================================================================

	mingus - Music theory Python package, Suite module
	Copyright (C) 2008-2009, Bart Spaans

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

"""

from mt_exceptions import UnexpectedObjectError


class Suite:
	"""The	Suite class is a datastructure that stores \
[refMingusContainersComposition Composition] objects."""

	title = 'Untitled'
	subtitle = ''
	author = ''
	email = ''
        description = ''
	compositions = []

	def __init__(self):
		pass

	def add_composition(self, composition):
		"""Adds a [refMingusContainersComposition composition] to the suite. \
Raises an !UnexpectedObjectError when the supplied argument is \
not a [refMingusContainersComposition Composition] object. """

		if not ( hasattr ( composition, "tracks") ):
			raise UnexpectedObjectError,\
			"Object '%s' not expected. Expecting a "\
			"mingus.containers.Composition object." % composition
		self.compositions.append(composition)
                return self

	def set_author(self, author, email = ''):
		"""Sets the author of the suite"""
		self.author = author
		self.email = email

	def set_title(self, title, subtitle = ''):
		"""Sets the title and the subtitle of the suite"""
		self.title = title
		self.subtitle = subtitle

	def __len__(self):
		"""Overloads the len() function"""
		return len(self.compositions)

	def __getitem__(self, index):
		"""Overloads the [] notation"""
		return self.compositions[index]

	def __setitem__(self, index, value):
		"""Overloads the [] = notation"""
		if not ( hasattr ( value, "tracks") ):
			raise UnexpectedObjectError,\
			"Object '%s' is not expected. Expecting a "\
			"mingus.containers.Composition object." % value
		self.compositions[index] = value

        def __add__(self, composition):
                """Overloads the + operator for Compositions."""
                return self.add_composition(composition)

