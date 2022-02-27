"""Centralize this in case we want to enhance it in the future."""
import os


def get_soundfont_path():
    soundfont_path = os.getenv('MINGUS_SOUNDFONT')
    assert soundfont_path, 'Please put the path to a soundfont file in the environment variable: MINGUS_SOUNDFONT'
    return soundfont_path
