import json

# noinspection PyUnresolvedReferences
from mingus.containers import PercussionNote, Note

# noinspection PyUnresolvedReferences
from mingus.containers import MidiInstrument

# noinspection PyUnresolvedReferences
from mingus.containers.midi_percussion import MidiPercussion


class MingusJSONEncoder(json.JSONEncoder):

    def default(self, obj):
        try:
            return obj.to_json()
        except:
            return super().default(obj)


def encode(obj, *args, **kwargs):
    return MingusJSONEncoder(*args, **kwargs).encode(obj)


def dumps(obj, *args, **kwargs):
    return encode(obj, *args, **kwargs)


def dump(obj, fp, *args, **kwargs):
    json_str = dumps(obj, *args, **kwargs)
    fp.write(json_str)


class MingusJSONDecoder(json.JSONDecoder):

    def __init__(self, *args, **kwargs):
        json.JSONDecoder.__init__(self, object_hook=self.object_hook, *args, **kwargs)

    def object_hook(self, obj):

        # handle your custom classes
        if isinstance(obj, dict):
            class_name = obj.get('class_name')
            if class_name:
                params = obj
                params.pop('class_name', None)
                obj = eval(f'{class_name}(**params)')
                return obj

        # handling the resolution of nested objects
        if isinstance(obj, dict):
            for key in list(obj):
                obj[key] = self.object_hook(obj[key])
            return obj

        if isinstance(obj, list):
            for i in range(0, len(obj)):
                obj[i] = self.object_hook(obj[i])
            return obj

        return obj


def decode(json_str):
    return MingusJSONDecoder().decode(json_str)


def loads(json_str):
    return decode(json_str)


def load(fp):
    json_str = fp.read()
    return loads(json_str)
