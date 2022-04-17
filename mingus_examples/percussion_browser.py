from functools import partial
from time import sleep

import tkinter as tk

import mingus.containers.midi_percussion as mp
import mingus.midi.pyfluidsynth as pyfluidsynth
from mingus.midi.get_soundfont_path import get_soundfont_path


class PlayPercussion:
    def __init__(self, setup_synth=True):
        """
        Presents a grid of buttons to playing each instrument

        :param setup_synth: synth setup can take several seconds. Set this to False to delay setup until it is needed
        """
        self.window = tk.Tk()
        self.window.title("Percusion Browser")
        self.padding = {
            'padx': 10,
            'pady': 10
        }

        # Messages ----------------------------------------------------------------------------------------------
        self.messages_frame = tk.Frame(self.window)
        messages = tk.Text(self.messages_frame, height=2)
        messages.pack(fill=tk.BOTH, expand=tk.YES, padx=2, pady=5)
        messages.insert(tk.END, 'Loading sound font. Please wait...')

        # Instruments -------------------------------------------------------------------------------------------
        self.instrument_frame = tk.Frame(self.window)
        instrument_number = 1
        for row in range(16):
            for column in range(8):
                name = mp.percussion_index_to_name(instrument_number)
                tk.Button(
                    self.instrument_frame,
                    text=f"{instrument_number} - {name}",
                    command=partial(self.play, instrument_number)
                ).grid(row=row, column=column, sticky=tk.NSEW)

                instrument_number += 1

        # Buttons -------------------------------------------------------------------------------------------------
        self.button_frame = tk.Frame(self.window)
        tk.Button(self.button_frame, text="Quit", command=self.quit).pack()

        if setup_synth:
            self.messages_frame.pack(fill=tk.BOTH, expand=tk.YES, **self.padding)
            self.window.after(500, self.setup_synth)
        else:
            self.instrument_frame.pack(fill=tk.BOTH, expand=tk.YES, **self.padding)
            self.button_frame.pack(fill=tk.BOTH, expand=tk.YES, **self.padding)
            self.sound_font = 'not loaded'
            self.synth = None
            self.sfid = None

        self.window.mainloop()

    def setup_synth(self):
        self.sound_font = get_soundfont_path()
        self.synth = pyfluidsynth.Synth(gain=1.0)
        self.sfid = self.synth.sfload(self.sound_font)
        self.synth.start()

        # Update GUI
        self.messages_frame.pack_forget()
        self.button_frame.pack_forget()
        self.instrument_frame.pack(fill=tk.BOTH, expand=tk.YES)
        self.button_frame.pack(fill=tk.BOTH, expand=tk.YES)

    def quit(self):
        self.window.withdraw()
        self.window.destroy()

    def play(self, instrument_number):
        if self.synth is None:
            self.button_frame.pack_forget()
            self.instrument_frame.pack_forget()
            self.messages_frame.pack(fill=tk.BOTH, expand=tk.YES, **self.padding)
            self.window.update()
            sleep(0.5)
            self.setup_synth()

        channel = 1
        bank = 128
        preset = 1  # seem like it can be any integer
        self.synth.program_select(channel, self.sfid, bank, preset)

        velocity = 100
        self.synth.noteon(channel, instrument_number, velocity)


if __name__ == '__main__':
    PlayPercussion(setup_synth=True)
