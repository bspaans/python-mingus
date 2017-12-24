#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
sys.path += ['../']
from mingus.midi import fluidsynth
from mingus.containers import *
import unittest
import time
from mingus.midi.sequencer_observer import SequencerObserver

class test_fluidsynth(unittest.TestCase):

    def setUp(self):
        fluidsynth.init('/home/bspaans/workspace/fluidsynth/ChoriumRevA.SF2',
                        file='test.wav')
        fluidsynth.set_instrument(0, 0)
        s = SequencerObserver()
        fluidsynth.midi.attach(s)

    def test_bar_velocity(self):
        b = Bar()
        n = Note('C')
        n.velocity = 0
        m = Note('C')
        m.velocity = 40
        o = Note('C')
        o.velocity = 80
        p = Note('C')
        p.velocity = 120
        b + n
        b + m
        b + o
        b + p
        self.assertTrue(fluidsynth.play_Bar(b), 0)

    def test_main_volume(self):
        for x in range(0, 128, 20):
            fluidsynth.midi.main_volume(1, x)
            fluidsynth.midi.main_volume(2, x)
            fluidsynth.play_NoteContainer(NoteContainer(['C', 'E', 'G']), 0)
            time.sleep(0.25)

    def test_control_change(self):
        for x in range(0, 128, 20):
            fluidsynth.midi.control_change(1, 13, x)
            fluidsynth.play_NoteContainer(NoteContainer(['C', 'E', 'G']), 0)
            time.sleep(0.25)

    def test_playnote(self):
        self.assertTrue(fluidsynth.play_Note(Note('C')))
        time.sleep(0.25)
        fluidsynth.stop_Note(Note('C'))

    def test_playnotecontainer(self):
        self.assertTrue(fluidsynth.play_NoteContainer(NoteContainer(['C', 'E', 'G'
                     ]), 0))
        time.sleep(0.25)
        fluidsynth.stop_NoteContainer(NoteContainer(['C', 'E', 'G']), 0)
        self.assertTrue(fluidsynth.play_NoteContainer(NoteContainer(['E', 'G',
                     Note('C', 6)]), 0))
        time.sleep(0.25)
        fluidsynth.stop_NoteContainer(NoteContainer(['E', 'G', Note('C', 6)]),
                                      0)

    def test_playbar(self):
        b = Bar()
        b + Note('C')
        b + Note('E')
        b + Note('G')
        self.assertTrue(fluidsynth.play_Bar(b), 0)

    def test_playbars(self):
        b = Bar()
        b + Note('C')
        b + Note('E')
        b + Note('G')
        c = Bar()
        c + Note('Eb')
        c + 'Gb'
        c + 'B'
        c + Note('C', 5)
        self.assertTrue(fluidsynth.play_Bars([b, c], [1, 2]), 0)

    def test_changing_bpm_bar(self):
        b = Bar()
        n = NoteContainer(['C', 'E', 'G'])
        n.bpm = 150
        b + NoteContainer(['A', 'C', 'E'])
        b + Note('E')
        b + n
        b + Note('Eb')
        self.assertTrue(fluidsynth.play_Bar(b, 0, 120))

    def test_changing_bpm_bars(self):
        b = Bar()
        n = NoteContainer(['C', 'E', 'G'])
        n.bpm = 150
        b + NoteContainer(['A', 'C', 'E'])
        b + Note('E')
        b + n
        b + Note('Eb')
        self.assertTrue(fluidsynth.play_Bars([b, b], [1, 2], 120))

    def test_changing_bpm_track(self):
        b = Bar()
        n = NoteContainer(['C', 'E', 'G'])
        n.bpm = 150
        b + NoteContainer(['A', 'C', 'E'])
        b + Note('E')
        b + n
        b + Note('Eb')
        t = Track()
        t + b
        t + b
        self.assertTrue(fluidsynth.play_Track(t), 0)

    def test_track(self):
        b = Bar()
        b + Note('C')
        b + Note('E')
        b + Note('A')
        b + 'E'
        t = Track()
        t + b
        t + b
        self.assertTrue(fluidsynth.play_Track(t), 0)

    def test_tracks(self):
        b = Bar()
        b + Note('C')
        b + Note('E')
        b + Note('A')
        b + 'E'
        c = Bar()
        c + Note('Eb')
        c + 'Gb'
        c + 'B'
        c + Note('C', 5)
        t = Track()
        t + b
        t + c
        t2 = Track()
        t2 + b
        t2 + b
        self.assertTrue(fluidsynth.play_Tracks([t, t2], [0, 1]))

    def test_composition(self):
        m = MidiInstrument('Vibraphone')
        b = Bar()
        b + Note('C')
        b + Note('E')
        b + Note('A')
        b + 'E'
        c = Bar()
        c + Note('G')
        c + 'C'
        c + 'E'
        c + Note('C', 5)
        t = Track()
        t + b
        t + c
        t2 = Track()
        t2 + b
        t2 + b
        t2.instrument = m
        c = Composition()
        c + t
        c + t2
        self.assertTrue(fluidsynth.play_Composition(c))


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(test_fluidsynth)

