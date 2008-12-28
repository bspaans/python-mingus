
"""

================================================================================

	mingus - Music theory Python package, MusicXML
	Copyright (C) 2008, Bart Spaans

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


def write_Note(file, note):
	try:
		f = open(file, "w")
	except:
		raise IOError, "Couldn't open '%s' for writing" % file

	doc = Document()
	score_partwise = doc.createElement("score-partwise")
	score_partwise.setAttribute("version", "2.0")
	doc.append_child(score_partwise)

	part_list = doc.createElement("part-list")
	score_partwise.append_child(part_list)

	score_part = doc.createElement("score-part")
	score_part.setAttribute("id", "P1")
	part_list.append_child(score_part)

	part_name = doc.createElement("part-name")
	score_part.append_child(part_name)



	
