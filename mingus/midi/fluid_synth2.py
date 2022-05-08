# -*- coding: utf-8 -*-

#    mingus - Music theory Python package, fluidsynth module.
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

# noinspection HttpUrlsUsage
"""FluidSynth support for mingus.

FluidSynth is a software MIDI synthesizer which allows you to play the
containers in mingus.containers real-time. To work with this module, you'll
need fluidsynth and a nice instrument collection (look here:
http://www.hammersound.net, go to Sounds → Soundfont Library → Collections).

An alternative is the FreePats project. You can download a SoundFont from
https://freepats.zenvoid.org/SoundSets/general-midi.html. Note that you will
need to uncompress the .tar.xz archive to get the actual .sf2 file.
"""
import time
import wave

from mingus.midi import pyfluidsynth as fs
from mingus.midi.sequencer2 import Sequencer


class FluidSynthPlayer:
    def __init__(self, sound_font_path, driver=None, file=None, gain=0.2):
        super().__init__()
        self.fs = fs.Synth(gain=gain)
        self.sfid = None
        self.sound_font_path = sound_font_path
        if file is not None:
            self.start_recording(file)
        else:
            self.start_audio_output(driver)

    def __del__(self):
        self.fs.delete()

    def start_audio_output(self, driver=None):
        """Start the audio output.

        The optional driver argument can be any of 'alsa', 'oss', 'jack',
        'portaudio', 'sndmgr', 'coreaudio', 'Direct Sound', 'dsound',
        'pulseaudio'. Not all drivers will be available for every platform.
        """
        self.fs.start(driver)

    def start_recording(self, file="mingus_dump.wav"):
        """Initialize a new wave file for recording."""
        w = wave.open(file, "wb")
        w.setnchannels(2)
        w.setsampwidth(2)
        w.setframerate(44100)
        self.wav = w

    # Implement Sequencer's interface
    def play_event(self, note, channel, velocity):
        self.fs.noteon(channel, note, velocity)

    def stop_event(self, note, channel):
        self.fs.noteoff(channel, note)

    def load_sound_font(self):
        self.sfid = self.fs.sfload(self.sound_font_path)
        assert self.sfid != -1, f'Could not load soundfont: {self.sound_font_path}'

    def set_instrument(self, channel, instr, bank):
        # Delay loading sound font because it is slow
        if self.sfid is None:
            self.sfid = self.fs.sfload(self.sound_font_path)
            assert self.sfid != -1, f'Could not load soundfont: {self.sound_font_path}'
            self.fs.program_reset()
        self.fs.program_select(channel, self.sfid, bank, instr)

    def sleep(self, seconds):
        if hasattr(self, "wav"):
            samples = fs.raw_audio_string(self.fs.get_samples(int(seconds * 44100)))
            self.wav.writeframes(bytes(samples))
        else:
            time.sleep(seconds)

    def control_change(self, channel, control, value):
        """Send a control change message.

        See the MIDI specification for more information.
        """
        if control < 0 or control > 128:
            return False
        if value < 0 or value > 128:
            return False
        self.fs.cc(channel, control, value)
        return True

    def modulation(self, channel, value):
        """Set the modulation."""
        return self.control_change(channel, 1, value)

    def main_volume(self, channel, value):
        """Set the main volume."""
        return self.control_change(channel, 7, value)

    def pan(self, channel, value):
        """Set the panning."""
        return self.control_change(channel, 10, value)

    def play_note(self, note, channel, velocity):
        self.play_event(int(note) + 12, int(channel), int(velocity))

    def play_percussion_note(self, note, channel, velocity):
        self.play_event(int(note), int(channel), int(velocity))

    def stop_note(self, note, channel):
        self.stop_event(int(note) + 12, int(channel))

    def stop_percussion_note(self, note, channel):
        self.stop_event(int(note), int(channel))

    def play_tracks(self, tracks, channels, bpm=120.0, start_time=1, end_time=50_000_000, stop_func=None):
        sequencer = Sequencer()
        sequencer.play_Tracks(tracks, channels, bpm=bpm)
        sequencer.play_score(self, stop_func=stop_func, start_time=start_time, end_time=end_time)

    def stop_everything(self):
        """Stop all the notes on all channels."""
        for x in range(118):
            for c in range(16):
                self.stop_note(x, c)
