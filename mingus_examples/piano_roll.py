from collections import defaultdict
import tkinter as tk
from pathlib import Path

from mingus.midi.sequencer2 import Sequencer
from mingus.containers.midi_percussion import percussion_index_to_name


def process_score(score):
    """
    Not sure how we are going to handle this. So for now use this function to find instruments and times.
    """
    tracks = defaultdict(list)
    names = {}
    for start_time, events in score.items():
        for event in events:
            name = names.setdefault(event['note'].name, percussion_index_to_name(int(event['note'].name)))
            tracks[name].append(start_time)
    return tracks


class Drawer:
    def __init__(self, tracks, canvas, width, height, bpm, time_signature, quantization):
        self.tracks = tracks
        self.canvas = canvas
        self.width = width
        self.height = height
        self.bpm = bpm
        self.beats_per_millisecond = bpm * (1.0 / 60000.0)
        self.time_signature = time_signature
        self.quantization = quantization

        self.n_bars = 4
        self.top_padding = 20.0
        self.label_width = 120.0
        self.bar_width = (self.width - self.label_width) / self.n_bars

        self.colors = {
            "major_grid_line": "red",
            "minor_grid_line": "blue",
            "text": "black"
        }

        self.row_height = min((self.height - self.top_padding) / len(self.tracks), 20.0)

    def draw_grid(self):

        # Draw minor grid ------------------------------------------------------------------------------------------
        cell_width = (self.bar_width / self.time_signature[0]) / (self.quantization / self.time_signature[1])
        bottom_y = self.top_padding + (self.row_height * len(self.tracks))

        x = self.label_width
        for _ in range(self.n_bars * self.time_signature[0] * round(self.quantization / self.time_signature[1])):
            self.canvas.create_line(x, self.top_padding, x, bottom_y, fill=self.colors["minor_grid_line"])
            x += cell_width

        # Major grid ---------------------------------------------------------------------------------------------
        y = self.top_padding
        for _ in self.tracks:
            self.canvas.create_line(0, y, self.width - 1, y, fill=self.colors["major_grid_line"])
            y += self.row_height
        self.canvas.create_line(0, y, self.width - 1, y, fill=self.colors["major_grid_line"])

        x = self.label_width
        for bar_num in range(self.n_bars):
            self.canvas.create_line(x, 0, x, bottom_y, fill=self.colors["major_grid_line"])
            self.canvas.create_text(x, self.top_padding / 2.0, text=str(bar_num + 1), fill=self.colors["text"])
            x += self.bar_width
        self.canvas.create_line(x, 0, x, bottom_y, fill=self.colors["major_grid_line"])

    def time_to_x(self, t_milliseconds):
        beat = self.beats_per_millisecond * t_milliseconds
        x = self.bar_width * beat / self.time_signature[0]
        return x

    def draw_notes(self):
        y = self.top_padding + 1
        for name, times in self.tracks.items():
            self.canvas.create_text(5.0, y + self.row_height / 2.0, text=name, fill=self.colors["text"], anchor=tk.W)
            for time in times:
                x = self.time_to_x(time) + self.label_width
                self.canvas.create_rectangle(x + 1, y, x + 10, y + self.row_height - 1, fill="green")
            y += self.row_height

    def draw_all(self):
        self.draw_grid()
        self.draw_notes()


class PianoRoll:
    def __init__(self):
        score_path = Path.home() / 'python_mingus' / 'scores' / 'blues.json'
        sequencer = Sequencer()
        sequencer.load_tracks(score_path)
        self.tracks = process_score(sequencer.score)

        bpm = 120.0
        time_signature = (4, 4)
        quantization = 8
        canvas_width = 1000
        canvas_height = 200

        self.root = tk.Tk()
        self.root.title("Piano Roll")
        self.root.geometry(f"{canvas_width + 50}x{canvas_height + 20}")

        canvas = tk.Canvas(self.root, width=canvas_width, height=canvas_height, bg="white")
        canvas.pack()

        drawer = Drawer(self.tracks, canvas, canvas_width, canvas_height, bpm, time_signature, quantization)
        drawer.draw_all()

        self.root.mainloop()


if __name__ == '__main__':
    PianoRoll()
