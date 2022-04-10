# -*- coding: utf-8 -*-
import logging

import sortedcontainers

from mingus.containers import PercussionNote
from mingus.containers.midi_snippet import MidiPercussionSnippet


logging.basicConfig(level=logging.INFO)


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
            if isinstance(snippet, MidiPercussionSnippet):
                snippet.put_into_score(channel, self.score, bpm)

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

    def play_score(self, synth):
        score = sortedcontainers.SortedDict(self.score)

        for channel, instrument in self.instruments:
            synth.set_instrument(channel, instrument.number, instrument.bank)
            logging.info(f'Instrument: {instrument.number}  Channel: {channel}')
        logging.info('--------------\n')

        the_time = 0
        for start_time, events in score.items():
            dt = start_time - the_time
            if dt > 0:
                synth.sleep(dt / 1000.0)
            the_time = start_time
            for event in events:
                if event['func'] == 'start_note':
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
            logging.info('--------------\n')

    def save_tracks(self, path, tracks, channels, bpm):
        self.play_Tracks(tracks, channels, bpm=bpm)
        score = sortedcontainers.SortedDict(self.score)

        print('x')

        # for channel, instrument in self.instruments:
        #     synth.set_instrument(channel, instrument.number, instrument.bank)
        #     logging.info(f'Instrument: {instrument.number}  Channel: {channel}')
        # logging.info('--------------\n')
        #
        # the_time = 0
        # for start_time, events in score.items():
        #     dt = start_time - the_time
        #     if dt > 0:
        #         synth.sleep(dt / 1000.0)
        #     the_time = start_time
        #     for event in events:
        #         if event['func'] == 'start_note':
        #             if isinstance(event['note'], PercussionNote):
        #                 synth.play_percussion_note(event['note'], event['channel'], event['velocity'])
        #             else:
        #                 synth.play_note(event['note'], event['channel'], event['velocity'])
        #
        #             logging.info('Start: {} Note: {note}  Velocity: {velocity}  Channel: {channel}'.
        #                          format(the_time, **event))
        #         elif event['func'] == 'end_note':
        #             if isinstance(event['note'], PercussionNote):
        #                 synth.stop_percussion_note(event['note'], event['channel'])
        #             else:
        #                 synth.stop_note(event['note'], event['channel'])
        #
        #             logging.info('Stop: {} Note: {note}  Channel: {channel}'.format(the_time, **event))
        #     logging.info('--------------\n')
