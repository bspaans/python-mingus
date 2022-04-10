from functools import partial
from time import sleep

import tkinter as tk

import midi_percussion as mp
import pyfluidsynth
from mingus.midi.get_soundfont_path import get_soundfont_path


# noinspection PyUnusedLocal
class PlayPercussion:
    def __init__(self, instrument_number=50, setup_synth=True):
        """

        :param instrument_number:
        :type instrument_number: int
        :param setup_synth: synth setup can take several seconds. Set this to False to delay setup until it is needed
        :type setup_synth: bool
        """
        if setup_synth:
            self.setup_synth()
        else:
            self.synth = None
            self.sound_font = 'not loaded'

        self.window = tk.Tk()
        self.window.title("Percusion Browser")
        padding = {
            'padx': 10,
            'pady': 10
        }

        instrument_number = 1
        row = 0
        for row in range(16):
            for column in range(8):
                name = mp.percussion_index_to_name(instrument_number)
                tk.Button(
                    self.window,
                    text=f"{instrument_number} - {name}",
                    command=partial(self.play, instrument_number)
                ).grid(row=row, column=column, sticky=tk.NSEW)

                instrument_number += 1

        row += 1
        tk.Button(self.window, text="Quit", command=self.quit).grid(row=row, column=0, **padding)

        self.window.mainloop()

    def setup_synth(self):
        self.sound_font = get_soundfont_path()
        self.synth = pyfluidsynth.Synth(gain=1.0)
        self.sfid = self.synth.sfload(self.sound_font)
        self.synth.start()

    def quit(self):
        self.window.withdraw()
        self.window.destroy()

    def play(self, instrument_number):
        if self.synth is None:
            self.setup_synth()

        channel = 1
        bank = 128
        preset = 1  # seem like it can be any integer
        self.synth.program_select(channel, self.sfid, bank, preset)

        velocity = 100
        for _ in range(3):
            self.synth.noteon(channel, instrument_number, velocity)
            sleep(0.5)


play = PlayPercussion(setup_synth=False)
