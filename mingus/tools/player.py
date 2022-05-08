import json
import importlib
import time
import tkinter as tk
from functools import partial
from pathlib import Path
from threading import Thread
from tkinter import ttk
from tkinter.filedialog import askopenfile, asksaveasfile
from typing import Optional

import midi_percussion as mp

import mingus.tools.mingus_json as mingus_json
from mingus.midi.fluid_synth2 import FluidSynthPlayer
from mingus.midi.get_soundfont_path import get_soundfont_path
from mingus.midi.sequencer2 import Sequencer


# A global variable for communicating with the click track thread
player_track_done = False


def load_tracks(module_name):
    module = importlib.import_module(module_name)
    importlib.reload(module)
    # noinspection PyUnresolvedReferences
    tracks, channels = module.play_in_player(n_times=1)
    return tracks, channels


def stop_func():
    global player_track_done
    return player_track_done


class Play(Thread):
    def __init__(self, synth, module_name):
        super().__init__()
        self.synth = synth
        self.tracks, self.channels = load_tracks(module_name)

    def run(self):
        self.synth.play_tracks(self.tracks, self.channels, stop_func=stop_func)
        print('player_done')


class Player:
    """
    Reloading the synth is too slow. This keeps the synth running and loads .py file as needed and plays them
    """
    def __init__(self):
        soundfont_path = get_soundfont_path()
        self.synth = FluidSynthPlayer(soundfont_path, gain=1.0)
        print("Loading soundfont...")
        self.synth.load_sound_font()
        print("done")

        self.module_name = 'mingus_examples.blues'

        self.main = tk.Tk()
        # Buttons -------------------------------------------------------------------------------------------------
        tk.Button(self.main, text="Play", command=self.play).pack()
        tk.Button(self.main, text="Stop", command=self.stop_playback).pack()
        tk.Button(self.main, text="Quit", command=self.quit).pack()

        self.main.mainloop()

    def quit(self):
        self.main.withdraw()
        self.main.destroy()

    def play(self):
        global player_track_done
        player_track_done = False

        play = Play(self.synth, self.module_name)
        play.start()

    @staticmethod
    def stop_playback():
        global player_track_done
        player_track_done = True


if __name__ == "__main__":
    Player()
