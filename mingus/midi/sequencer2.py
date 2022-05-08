import logging

import sortedcontainers

from mingus.containers import PercussionNote
import mingus.tools.mingus_json as mingus_json


logging.basicConfig(level=logging.INFO)


def calculate_bar_start_time(bpm: float, beats_per_bar: int, bar_number: int) -> int:
    """
    Since tracks can have different bpm and beats_per_bar, it's easiest t

    :param bpm:
    :param beats_per_bar:
    :param bar_number: the first bar is bar_number 1
    :return: time in milliseconds
    """
    beat = (bar_number - 1) * beats_per_bar
    minutes = beat / bpm
    t = round(minutes * 60_000)
    return t


def calculate_bar_end_time(bpm: float, beats_per_bar: int, bar_number: int) -> int:
    """
    :param bpm:
    :param beats_per_bar:
    :param bar_number: the first bar is bar_number 1
    :return: time in milliseconds
    """
    t = calculate_bar_start_time(bpm, beats_per_bar, bar_number + 1)
    return t


class Sequencer:
    """
    This sequencer creates a "score" that is a dict with time in milliseconds as keys and list of
    events as the values.

    To build the score, just go through all the tracks, bars, notes, etc... and add keys and events.
    Then when playing the score, first sort by keys.

    We use sortedcontainers containers to make that fast for the case where there are thousands of events.
    """
    def __init__(self, score=None):
        super().__init__()
        # Keys will be in milliseconds since the start. Values will be lists of stuff to do.
        self.score = score or {}
        self.instruments = []

    # noinspection PyPep8Naming
    def play_Track(self, track, channel=1, bpm=120.0):
        """Play a Track object."""
        start_time = 0
        for bar in track.bars:
            bpm = bar.bpm or bpm
            start_time += bar.play(start_time, bpm, channel, self.score)

        for snippet in track.snippets:
            snippet.put_into_score(self.score, channel, bpm)

        for event in track.events:
            event.put_into_score(self.score, channel, bpm)

    # noinspection PyPep8Naming
    def play_Tracks(self, tracks, channels, bpm=None):
        """Play a list of Tracks."""
        # Set the instruments. Previously, if an instrument number could not be found, it was set to 1. That can
        # be confusing to users, so just crash if it cannot be found.
        for track_num, track in enumerate(tracks):
            if track.instrument is not None:
                self.instruments.append((channels[track_num], track.instrument))

        # Because of possible changes in bpm, render each track separately
        for track, channel in zip(tracks, channels):
            bpm = bpm or track.bpm
            self.play_Track(track, channel, bpm=bpm)

    # noinspection PyPep8Naming
    def play_Composition(self, composition, channels=None, bpm=120):
        if channels is None:
            channels = [x + 1 for x in range(len(composition.tracks))]
        return self.play_Tracks(composition.tracks, channels, bpm)

    def play_score(self, synth, stop_func=None, start_time=0, end_time=50_000_000):
        """

        :param synth:
        :param stop_func: a function that returns True if the score should stop playing. We tried
            using a global variable for this, that ended up passing around the variable value, not the
            reference.
        :param start_time: in milliseconds. It might seem easier to pass in the start beat, but tracks can have
            different bpm or meter, etc... So time in milliseconds is more universal. There are helper functions
            at the top of this module to calculate time from bpm, ...
        :param end_time: in milliseconds
        :return: None
        """
        score = sortedcontainers.SortedDict(self.score)

        for channel, instrument in self.instruments:
            synth.set_instrument(channel, instrument.number, instrument.bank)
            logging.info(f'Instrument: {instrument.number}  Channel: {channel}')
        logging.info('--------------\n')

        the_time = 0
        for event_start_time, events in score.items():
            if stop_func and stop_func():
                break

            if event_start_time > end_time:
                break

            # Sleep until the next event
            dt = event_start_time - the_time
            if dt > 0 and event_start_time >= start_time:
                synth.sleep(dt / 1000.0)
            the_time = event_start_time

            for event in events:
                if event['func'] == 'start_note' and event_start_time >= start_time:
                    if isinstance(event['note'], PercussionNote):
                        synth.play_percussion_note(event['note'], event['channel'], event['velocity'])
                    else:
                        synth.play_note(event['note'], event['channel'], event['velocity'])

                    logging.info('Start: {} Note: {note}  Velocity: {velocity}  Channel: {channel}'.
                                 format(the_time, **event))

                elif event['func'] == 'end_note':
                    if isinstance(event['note'], PercussionNote):
                        synth.stop_percussion_note(event['note'], event['channel'])
                    else:
                        synth.stop_note(event['note'], event['channel'])
                    logging.info('Stop: {} Note: {note}  Channel: {channel}'.format(the_time, **event))

                elif event['func'] == 'control_change':
                    synth.control_change(event['channel'], event['control'].value, event['value'])
                    logging.info('Control change: Channel: {channel}  Control: {control}  Value: {value}'.
                                 format(the_time, **event))

            logging.info('--------------\n')
        synth.sleep(2)  # prevent cutoff at the end

    def save_tracks(self, path, tracks, channels, bpm):
        self.play_Tracks(tracks, channels, bpm=bpm)
        score = sortedcontainers.SortedDict(self.score)

        to_save = {
            'instruments': self.instruments,
            'score': dict(score)
        }

        with open(path, 'w') as fp:
            mingus_json.dump(to_save, fp, indent=4)

    def load_tracks(self, path):
        with open(path, 'r') as fp:
            data = mingus_json.load(fp)

        self.instruments = data['instruments']
        self.score = {int(k): v for k, v in data['score'].items()}
