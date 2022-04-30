from typing import Optional


import mingus.tools.mingus_json as mingus_json


class RawSnippet(mingus_json.JsonMixin):
    """
    A RawSnippet packages a dict of events and an instrument for a Track.
    """
    def __init__(self, events: dict, start: float = 0.0, length_in_seconds: Optional[float] = None,
                 n_replications: int = 1):
        """
        :param events: keys are in milliseconds, values are lists of events
        :param start: in seconds
        :param length_in_seconds: Original length. Needed for repeats.
        :param n_replications:
        """
        self.events = events
        self.start = start  # in seconds
        self.length_in_seconds = length_in_seconds
        self.n_replications = n_replications
        assert not (n_replications > 1 and length_in_seconds is None), \
            f'If there are replications, then length_in_seconds cannot be None'

    def to_json(self):
        snippet_dict = super().to_json()
        for param in ("events", "start", "length_in_seconds", "n_replications"):
            snippet_dict[param] = getattr(self, param)
        return snippet_dict

    def put_into_score(self, score: dict, *args, **kwargs):
        length_in_msec = (self.length_in_seconds or 0.0) * 1000.0
        elapsed_time = self.start * 1000.0

        for j in range(self.n_replications):
            for event_time, event_list in self.events.items():
                key = round((elapsed_time + event_time + j * length_in_msec))  # The score dict key in milliseconds
                if key not in score:
                    score[key] = []
                score[key] += event_list
