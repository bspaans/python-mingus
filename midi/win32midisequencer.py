#    mingus - Music theory Python package, win32midisequencer module.
#    Copyright (C) 2008-2010, Bart Spaans, Ben Fisher
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

"""MIDI playback support for mingus in MS Windows.

This module will use the default MIDI output device, which can be chosen in
the control panel. No extra dlls or modules are needed; uses built-in ctypes
module.

Caution: this will throw Win32MidiException if there is no device, or device
can't be opened.
"""

import sys
# We should be able to import this module on non-win32 systems without 
# raising exceptions. So instead, raise in the init() method.
if sys.platform=='win32':
    import win32midi
    from win32midi import Win32MidiException
    
from datetime import datetime
from mingus.midi.sequencer import Sequencer
from mingus.containers.instrument import MidiInstrument

class Win32MidiSequencer(Sequencer):
    output = None
    midplayer = None

    def init(self):
        if sys.platform != 'win32':
            raise RuntimeError('Intended for use on win32 platform')
        self.midplayer = win32midi.Win32MidiPlayer()
        self.midplayer.openDevice()

    def __del__(self):
        self.midplayer.closeDevice()

    # Implement Sequencer's interface

    def play_event(self, note, channel, velocity):
        self.midplayer.rawNoteOn(note, channel, velocity)

    def stop_event(self, note, channel):
        self.midplayer.rawNoteOff(note, channel)

    def cc_event(self, channel, control, value):
        self.midplayer.controllerChange(control,value, channel)

    def instr_event(self, channel, instr, bank):
        #"bank" currently not supported
        self.midplayer.programChange(instr, channel)

