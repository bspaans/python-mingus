import os
from time import sleep

import tkinter as tk
from tkinter import ttk

import midi_percussion as mp
import pyfluidsynth


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
        self.window.title("Instrument Browser")
        padding = {
            'padx': 10,
            'pady': 10
        }

        self.message = tk.StringVar(value=f'Font: {self.sound_font}')

        row = 0
        ttk.Label(self.window, textvariable=self.message, anchor='w', justify='left').\
            grid(row=row, column=0, columnspan=2, sticky='EW', **padding)
        row += 1

        self.instrument_number = tk.IntVar(value=instrument_number)
        ttk.Label(self.window, text="Instrument").grid(row=row, column=0, sticky=tk.W, **padding)
        spin_box = tk.Spinbox(self.window, from_=1, to=128, increment=1, textvariable=self.instrument_number,
                              command=self.spinner)
        spin_box.bind("<Return>", self.spinner)
        spin_box.grid(row=row, column=1, sticky=tk.W, **padding)
        row += 1

        ttk.Label(self.window, text="Name").grid(row=row, column=0, sticky=tk.W, **padding)
        self.instrument_name = tk.StringVar(value=mp.percussion_index_to_name(instrument_number))
        ttk.Label(self.window, text="", textvariable=self.instrument_name).\
            grid(row=row, column=1, sticky=tk.W, **padding)
        row += 1

        tk.Button(self.window, text="Play", command=self.play).grid(row=row, column=0, **padding)
        tk.Button(self.window, text="Quit", command=self.quit).grid(row=row, column=1, **padding)

        self.window.mainloop()

    def setup_synth(self):
        self.sound_font = os.getenv('MINGUS_SOUNDFONT')
        assert self.sound_font, 'Please put the path to a soundfont file in the environment variable: MINGUS_SOUNDFONT'

        self.synth = pyfluidsynth.Synth(gain=1.0)
        self.sfid = self.synth.sfload(self.sound_font)
        self.synth.start()

    def quit(self):
        self.window.withdraw()
        self.window.destroy()
    
    def play(self):
        if self.synth is None:
            self.setup_synth()

        channel = 1
        bank = 128
        preset = 1  # seem like it can be any integer
        self.synth.program_select(channel, self.sfid, bank, preset)

        velocity = 100
        for _ in range(3):
            self.synth.noteon(channel, self.instrument_number.get(), velocity)
            sleep(0.5)

    def spinner(self, *args):
        number = self.instrument_number.get()
        self.instrument_name.set(mp.percussion_index_to_name(number))
        self.window.after(250, self.play)


play = PlayPercussion()
