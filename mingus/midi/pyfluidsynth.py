#!/usr/bin/python
# -*- coding: utf-8 -*-

#    pyFluidSynth
#
#    Python bindings for FluidSynth
#
#    Copyright 2008-2009, Nathan Whitehead <nwhitehe@gmail.com>
#    Currently maintained by Bart Spaans <onderstekop@gmail.com>
#    Released under the LGPL

"""Python bindings for FluidSynth.

FluidSynth is a software synthesizer for generating music.  It works like a
MIDI synthesizer.

You load patches, set parameters, then send NOTEON and NOTEOFF events to
play notes.

Instruments are defined in SoundFonts, generally files with the extension
SF2.

FluidSynth can either be used to play audio itself, or you can call a
function that returns chunks of audio data and output the data to the
soundcard yourself.

FluidSynth works on all major platforms, so pyFluidSynth should also.
"""

import time
from ctypes import *
from ctypes.util import find_library

lib = find_library('fluidsynth') or find_library('libfluidsynth')\
     or find_library('libfluidsynth-1')
if lib is None:
    raise ImportError, "Couldn't find the FluidSynth library."

_fl = CDLL(lib)

def cfunc(name, result, *args):
    """Build and apply a ctypes prototype complete with parameter flags."""
    atypes = []
    aflags = []
    for arg in args:
        atypes.append(arg[1])
        aflags.append((arg[2], arg[0]) + arg[3:])
    return CFUNCTYPE(result, *atypes)((name, _fl), tuple(aflags))

api_version = '1.2'

new_fluid_settings = cfunc('new_fluid_settings', c_void_p)
new_fluid_synth = cfunc('new_fluid_synth', c_void_p, ('settings', c_void_p, 1))
new_fluid_audio_driver = cfunc('new_fluid_audio_driver', c_void_p, ('settings',
                               c_void_p, 1), ('synth', c_void_p, 1))
fluid_settings_setstr = cfunc('fluid_settings_setstr', c_int, ('settings',
                              c_void_p, 1), ('name', c_char_p, 1), ('str',
                              c_char_p, 1))
fluid_settings_setnum = cfunc('fluid_settings_setnum', c_int, ('settings',
                              c_void_p, 1), ('name', c_char_p, 1), ('val',
                              c_double, 1))
fluid_settings_setint = cfunc('fluid_settings_setint', c_int, ('settings',
                              c_void_p, 1), ('name', c_char_p, 1), ('val',
                              c_int, 1))
delete_fluid_audio_driver = cfunc('delete_fluid_audio_driver', None, ('driver',
                                  c_void_p, 1))
delete_fluid_synth = cfunc('delete_fluid_synth', None, ('synth', c_void_p, 1))
delete_fluid_settings = cfunc('delete_fluid_settings', None, ('settings',
                              c_void_p, 1))
fluid_synth_sfload = cfunc('fluid_synth_sfload', c_int, ('synth', c_void_p, 1),
                           ('filename', c_char_p, 1), ('update_midi_presets',
                           c_int, 1))
fluid_synth_sfunload = cfunc('fluid_synth_sfunload', c_int, ('synth', c_void_p,
                             1), ('sfid', c_int, 1), ('update_midi_presets',
                             c_int, 1))
fluid_synth_program_select = cfunc(
    'fluid_synth_program_select',
    c_int,
    ('synth', c_void_p, 1),
    ('chan', c_int, 1),
    ('sfid', c_int, 1),
    ('bank', c_int, 1),
    ('preset', c_int, 1),
    )
fluid_synth_noteon = cfunc(
    'fluid_synth_noteon',
    c_int,
    ('synth', c_void_p, 1),
    ('chan', c_int, 1),
    ('key', c_int, 1),
    ('vel', c_int, 1),
    )
fluid_synth_noteoff = cfunc('fluid_synth_noteoff', c_int, ('synth', c_void_p,
                            1), ('chan', c_int, 1), ('key', c_int, 1))
fluid_synth_pitch_bend = cfunc('fluid_synth_pitch_bend', c_int, ('synth',
                               c_void_p, 1), ('chan', c_int, 1), ('val', c_int,
                               1))
fluid_synth_cc = cfunc(
    'fluid_synth_cc',
    c_int,
    ('synth', c_void_p, 1),
    ('chan', c_int, 1),
    ('ctrl', c_int, 1),
    ('val', c_int, 1),
    )
fluid_synth_program_change = cfunc('fluid_synth_program_change', c_int, ('synth'
                                   , c_void_p, 1), ('chan', c_int, 1), ('prg',
                                   c_int, 1))
fluid_synth_bank_select = cfunc('fluid_synth_bank_select', c_int, ('synth',
                                c_void_p, 1), ('chan', c_int, 1), ('bank',
                                c_int, 1))
fluid_synth_sfont_select = cfunc('fluid_synth_sfont_select', c_int, ('synth',
                                 c_void_p, 1), ('chan', c_int, 1), ('sfid',
                                 c_int, 1))
fluid_synth_program_reset = cfunc('fluid_synth_program_reset', c_int, ('synth',
                                  c_void_p, 1))
fluid_synth_system_reset = cfunc('fluid_synth_system_reset', c_int, ('synth',
                                 c_void_p, 1))
fluid_synth_write_s16 = cfunc(
    'fluid_synth_write_s16',
    c_void_p,
    ('synth', c_void_p, 1),
    ('len', c_int, 1),
    ('lbuf', c_void_p, 1),
    ('loff', c_int, 1),
    ('lincr', c_int, 1),
    ('rbuf', c_void_p, 1),
    ('roff', c_int, 1),
    ('rincr', c_int, 1),
    )

def fluid_synth_write_s16_stereo(synth, len):
    """Return generated samples in stereo 16-bit format.

    Return value is a Numpy array of samples.
    """
    import numpy
    buf = create_string_buffer(len * 4)
    fluid_synth_write_s16(synth, len, buf, 0, 2, buf, 1, 2)
    return numpy.fromstring(buf[:], dtype=numpy.int16)

class Synth:

    """Synth represents a FluidSynth synthesizer."""

    def __init__(self, gain=0.2, samplerate=44100):
        """Create a new synthesizer object to control sound generation.

        Optional keyword arguments:
          gain: scale factor for audio output, default is 0.2
                lower values are quieter, allow more simultaneous notes
          samplerate: output samplerate in Hz, default is 44100 Hz
        """
        st = new_fluid_settings()
        fluid_settings_setnum(st, 'synth.gain', gain)
        fluid_settings_setnum(st, 'synth.sample-rate', samplerate)

        # No reason to limit ourselves to 16 channels
        fluid_settings_setint(st, 'synth.midi-channels', 256)
        self.settings = st
        self.synth = new_fluid_synth(st)
        self.audio_driver = None

    def start(self, driver=None):
        """Start audio output driver in separate background thread.

        Call this function any time after creating the Synth object.
        If you don't call this function, use get_samples() to generate
        samples.

        Optional keyword argument:
          driver: which audio driver to use for output
                  Possible choices:
                    'alsa', 'oss', 'jack', 'portaudio'
                    'sndmgr', 'coreaudio', 'Direct Sound',
                    'dsound', 'pulseaudio'

        Not all drivers will be available for every platform, it depends on
        which drivers were compiled into FluidSynth for your platform.
        """
        if driver is not None:
            assert driver in [
                    'alsa',
                    'oss',
                    'jack',
                    'portaudio',
                    'sndmgr',
                    'coreaudio',
                    'Direct Sound',
                    'dsound',
                    'pulseaudio'
                    ]
            fluid_settings_setstr(self.settings, 'audio.driver', driver)
        self.audio_driver = new_fluid_audio_driver(self.settings, self.synth)

    def delete(self):
        if self.audio_driver is not None:
            delete_fluid_audio_driver(self.audio_driver)
        delete_fluid_synth(self.synth)
        delete_fluid_settings(self.settings)

    def sfload(self, filename, update_midi_preset=0):
        """Load SoundFont and return its IDi."""
        return fluid_synth_sfload(self.synth, filename, update_midi_preset)

    def sfunload(self, sfid, update_midi_preset=0):
        """Unload a SoundFont and free memory it used."""
        return fluid_synth_sfunload(self.synth, sfid, update_midi_preset)

    def program_select(self, chan, sfid, bank, preset):
        """Select a program."""
        return fluid_synth_program_select(self.synth, chan, sfid, bank, preset)

    def noteon(self, chan, key, vel):
        """Play a note."""
        if key < 0 or key > 128:
            return False
        if chan < 0:
            return False
        if vel < 0 or vel > 128:
            return False
        return fluid_synth_noteon(self.synth, chan, key, vel)

    def noteoff(self, chan, key):
        """Stop a note."""
        if key < 0 or key > 128:
            return False
        if chan < 0:
            return False
        return fluid_synth_noteoff(self.synth, chan, key)

    def pitch_bend(self, chan, val):
        """Adjust pitch of a playing channel by small amounts.

        A pitch bend value of 0 is no pitch change from default.
        A value of -2048 is 1 semitone down.
        A value of 2048 is 1 semitone up.
        Maximum values are -8192 to +8192 (transposing by 4 semitones).
        """
        return fluid_synth_pitch_bend(self.synth, chan, val + 8192)

    def cc(self, chan, ctrl, val):
        """Send control change value.

        The controls that are recognized are dependent on the
        SoundFont.  Values are always 0 to 127.  Typical controls
        include:
          1: vibrato
          7: volume
          10: pan (left to right)
          11: expression (soft to loud)
          64: sustain
          91: reverb
          93: chorus
        """
        return fluid_synth_cc(self.synth, chan, ctrl, val)

    def program_change(self, chan, prg):
        """Change the program."""
        return fluid_synth_program_change(self.synth, chan, prg)

    def bank_select(self, chan, bank):
        """Choose a bank."""
        return fluid_synth_bank_select(self.synth, chan, bank)

    def sfont_select(self, chan, sfid):
        """Choose a SoundFont."""
        return fluid_synth_sfont_select(self.synth, chan, sfid)

    def program_reset(self):
        """Reset the programs on all channels."""
        return fluid_synth_program_reset(self.synth)

    def system_reset(self):
        """Stop all notes and reset all programs."""
        return fluid_synth_system_reset(self.synth)

    def get_samples(self, len=1024):
        """Generate audio samples.

        The return value will be a NumPy array containing the given
        length of audio samples.  If the synth is set to stereo output
        (the default) the array will be size 2 * len.
        """
        return fluid_synth_write_s16_stereo(self.synth, len)


def raw_audio_string(data):
    """Return a string of bytes to send to soundcard.

    Input is a numpy array of samples. Default output format is 16-bit
    signed (other formats not currently supported).
    """
    import numpy
    return data.astype(numpy.int16).tostring()

