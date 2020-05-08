from mingus.core import chords
from mingus.core.progressions import determine

CIRCLE_OF_5THS = ['C', 'G', 'D', 'A', 'E', 'B', 'Gb', 'Db', 'Ab', 'Eb', 'Bb', 'F']

MODE_CHORD_FUNCTIONS = [chords.I7, chords.ii7, chords.iii7, chords.IV7, chords.V7, chords.vi7, chords.VII7]

MODE_CHORD_TYPE = {
    'I': 'M7',
    'ii': 'm7',
    'iii': 'm7',
    'IV': 'M7',
    'V': '7',
    'vi': 'm7',
    'vii': 'm7b5'
}

def analyze_7th_chord(chord):
    """

    :param chord:
    :return: chord_notes, chord_type_full, chord_modes

    Example:
    >>> chord_notes, chord_type_full, results = analyze_chord("G7")
    >>> for chord_degree, key, harmonic_func_full in results:
    ...     print("{} (comprising {}) is a {} chord ({}) of the key of {}".format(chord_type_full,', '.join(chord_notes),
    ...                                                                           chord_degree, harmonic_func_full,
    ...                                                                           key))
    G dominant seventh (comprising G, B, D, F) is a V chord (dominant seventh) of the key of C

    """
    chord_notes = chords.from_shorthand(chord)
    chord_type_full = chords.determine_seventh(chord_notes)[0]
    chord_type_short = chords.determine_seventh(chord_notes, shorthand=True)[0]
    type_key = 'M7' if chord_type_short[-2:] == 'M7' else (
        'm7' if chord_type_short[-2:] == 'm7' else ('m7b5' if chord_type_short[-2:] == 'm7b5' else '7')
    )

    chord_modes = []
    for key in CIRCLE_OF_5THS:
        harmonic_func = determine(chord_notes, key, shorthand=True)[0]
        harmonic_func_full = determine(chord_notes, key, shorthand=False)[0]
        chord_degree = harmonic_func[:-1]
        if chord_degree in MODE_CHORD_TYPE:
            func_chord_type = MODE_CHORD_TYPE[chord_degree]
            if func_chord_type == type_key:
                chord_modes.append((chord_degree, key, harmonic_func_full))
    return chord_notes, chord_type_full, chord_modes

if __name__ == '__main__':
    import doctest
    doctest.testmod()
