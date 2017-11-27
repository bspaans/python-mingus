#!/usr/bin/python
# -*- coding: utf-8 -*-

#    mingus - Music theory Python package, fft module.
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

"""Find the frequencies in raw audio data by using fast Fourier transformations
(supplied by numpy).

This module can also convert the found frequencies to Note objects.
"""

import wave
import struct
import numpy
from mingus.containers.note import Note
from numpy.fft import fft as _fft
import operator

# Making a frequency-amplitude table   Adapted some ideas and source from:
# http://xoomer.virgilio.it/sam_psy/psych/sound_proc/sound_proc_python.html
#
# The log function turns out to be really, really slow, which adds up quickly.
# So before we do any performance critical calculations we set up a cache of all
# the frequencies we need to look up.

_log_cache = []
for x in xrange(129):
    _log_cache.append(Note().from_int(x).to_hertz())
_last_asked = None

def _find_log_index(f):
    """Look up the index of the frequency f in the frequency table.

    Return the nearest index.
    """
    global _last_asked, _log_cache
    (begin, end) = (0, 128)

    # Most calls are sequential, this keeps track of the last value asked for so
    # that we need to search much, much less.
    if _last_asked is not None:
        (lastn, lastval) = _last_asked
        if f >= lastval:
            if f <= _log_cache[lastn]:
                _last_asked = (lastn, f)
                return lastn
            elif f <= _log_cache[lastn + 1]:
                _last_asked = (lastn + 1, f)
                return lastn + 1
            begin = lastn

    # Do some range checking
    if f > _log_cache[127] or f <= 0:
        return 128

    # Binary search related algorithm to find the index
    while begin != end:
        n = (begin + end) // 2
        c = _log_cache[n]
        cp = _log_cache[n - 1] if n != 0 else 0
        if cp < f <= c:
            _last_asked = (n, f)
            return n
        if f < c:
            end = n
        else:
            begin = n
    _last_asked = (begin, f)
    return begin

def find_frequencies(data, freq=44100, bits=16):
    """Convert audio data into a frequency-amplitude table using fast fourier
    transformation.

    Return a list of tuples (frequency, amplitude).

    Data should only contain one channel of audio.
    """
    # Fast fourier transform
    n = len(data)
    p = _fft(data)
    uniquePts = numpy.ceil((n + 1) / 2.0)

    # Scale by the length (n) and square the value to get the amplitude
    p = [(abs(x) / float(n)) ** 2 * 2 for x in p[0:uniquePts]]
    p[0] = p[0] / 2
    if n % 2 == 0:
        p[-1] = p[-1] / 2

    # Generate the frequencies and zip with the amplitudes
    s = freq / float(n)
    freqArray = numpy.arange(0, uniquePts * s, s)
    return zip(freqArray, p)

def find_notes(freqTable, maxNote=100):
    """Convert the (frequencies, amplitude) list to a (Note, amplitude) list."""
    res = [0] * 129
    n = Note()
    for (freq, ampl) in freqTable:
        if freq > 0 and ampl > 0:
            f = _find_log_index(freq)
            if f < maxNote:
                res[f] += ampl
            else:
                res[128] += ampl
    return [(Note().from_int(x) if x < 128 else None, n) for (x, n) in
            enumerate(res)]

def data_from_file(file):
    """Return (first channel data, sample frequency, sample width) from a .wav
    file."""
    fp = wave.open(file, 'r')
    data = fp.readframes(fp.getnframes())
    channels = fp.getnchannels()
    freq = fp.getframerate()
    bits = fp.getsampwidth()

    # Unpack bytes -- warning currently only tested with 16 bit wavefiles. 32
    # bit not supported.
    data = struct.unpack(('%sh' % fp.getnframes()) * channels, data)

    # Only use first channel
    channel1 = []
    n = 0
    for d in data:
        if n % channels == 0:
            channel1.append(d)
        n += 1
    fp.close()
    return (channel1, freq, bits)

def find_Note(data, freq, bits):
    """Get the frequencies, feed them to find_notes and the return the Note
    with the highest amplitude."""
    data = find_frequencies(data, freq, bits)
    return sorted(find_notes(data), key=operator.itemgetter(1))[-1][0]

def analyze_chunks(data, freq, bits, chunksize=512):
    """Cut the one channel data in chunks and analyzes them separately.

    Making the chunksize a power of two works fastest.
    """
    res = []
    while data != []:
        f = find_frequencies(data[:chunksize], freq, bits)
        res.append(sorted(find_notes(f), key=operator.itemgetter(1))[-1][0])
        data = data[chunksize:]
    return res

def find_melody(file='440_480_clean.wav', chunksize=512):
    """Cut the sample into chunks and analyze each chunk.

    Return a list [(Note, chunks)] where chunks is the number of chunks
    where that note is the most dominant.

    If two consequent chunks turn out to return the same Note they are
    grouped together.

    This is an experimental function.
    """
    (data, freq, bits) = data_from_file(file)
    res = []
    for d in analyze_chunks(data, freq, bits, chunksize):
        if res != []:
            if res[-1][0] == d:
                val = res[-1][1]
                res[-1] = (d, val + 1)
            else:
                res.append((d, 1))
        else:
            res.append((d, 1))
    return [(x, freq) for (x, freq) in res]

