from argparse import ArgumentParser
from mingus.core import chords
from mingus.core.keys import keys as all_keys, get_notes, is_valid_key
from mingus.core.intervals import interval, minor_fifth as tritone
from mingus.core.scales import _Scale
from mingus.core.notes import reduce_accidentals
from mingus.core.progressions import determine

def determine_scale(notes):
    """ Same as determine, but returns the scale object itself """
    notes = set(notes)
    res = []

    for key in all_keys:
        for scale in _Scale.__subclasses__():
            if scale.type == 'major':
                if (notes <= set(scale(key[0]).ascending()) or
                        notes <= set(scale(key[0]).descending())):
                    res.append(scale(key[0]))
            elif scale.type == 'minor':
                if (notes <= set(scale(get_notes(key[1])[0]).ascending()) or
                        notes <= set(scale(get_notes(key[1])[0]).descending())):
                    res.append(scale(get_notes(key[1])[0]))
    return res

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

MODES_4_CHORD_TYPE = {
    'M7': ['I', 'IV'],
    'm7': ['ii', 'iii', 'vi'],
    '7': ['V'],
    'm7b5': 'vii'
}

def tritone_substitution(chord):
    chord_notes = chords.from_shorthand(chord)
    new_note = reduce_accidentals(tritone(chord_notes[0]))
    new_chord = new_note + '7'
    new_notes = chords.from_shorthand(new_chord)
    return new_chord, new_notes

def analyze_chord(chord):
    chord_notes = chords.from_shorthand(chord)
    chord_type_full = chords.determine_seventh(chord_notes)[0]
    chord_type_short = chords.determine_seventh(chord_notes, shorthand=True)[0]
    type_key = 'M7' if chord_type_short[-2:] == 'M7' else (
        'm7' if chord_type_short[-2:] == 'm7' else ('m7b5' if chord_type_short[-2:] == 'm7b5' else '7')
    )
    # possible_chord_types = MODES_4_CHORD_TYPE[type_key]
    chord_modes = []
    for key in CIRCLE_OF_5THS:
        harmonic_func = determine(chord_notes, key, shorthand=True)[0]
        harmonic_func_full = determine(chord_notes, key, shorthand=False)[0]
        assert harmonic_func[-1] == '7'
        chord_degree = harmonic_func[:-1]
        if chord_degree in MODE_CHORD_TYPE:
            func_chord_type = MODE_CHORD_TYPE[chord_degree]
            if func_chord_type == type_key:
                chord_modes.append((chord_degree, key, harmonic_func_full))
    return chord_notes, chord_type_full, chord_modes

def determine_key_and_function(chord):
    chord_notes, chord_type_full, results = analyze_chord(chord)
    # chord_meaning = chords.chord_shorthand_meaning[type_key],
    if len(results) == 1:
        for chord_degree, key, harmonic_func_full in results:
            print("{} (comprising {}) is a {} chord ({}) of the key of {}".format(chord_type_full,
                                                                                  ', '.join(chord_notes),
                                                                                  chord_degree,
                                                                                  harmonic_func_full,
                                                                                  key))
    else:
        print("{} (comprising {}) can be one of: ".format(chord_type_full, ', '.join(chord_notes)))
        for chord_degree, key, harmonic_func_full in results:
            print("\t a {} chord ({}) of the key of {}".format(chord_degree, harmonic_func_full, key))

def create_seventh_name(note):
    return chords.determine_seventh(chords.seventh(note, note), shorthand=True)[0]

def twelve_bar_blues(key):
    key_notes = get_notes(key)
    aChord = create_seventh_name(key)
    bChord = create_seventh_name(key_notes[3])
    cChord = chords.determine_seventh(MODE_CHORD_FUNCTIONS[1](key), shorthand=True)[0]
    dChord = chords.determine_seventh(MODE_CHORD_FUNCTIONS[4](key), shorthand=True)[0]
    return [
        [aChord, bChord, aChord, aChord],
        [bChord, bChord, aChord, aChord],
        [cChord, dChord, aChord, aChord]
    ]

def reharmonize_v_to_ii_v(chord):
    chord_notes, chord_type_full, chord_modes = analyze_chord(chord)
    assert len(chord_modes) == 1
    chord_degree, key, harmonic_func_full = chord_modes[0]
    ii_chord_type_short = chords.determine_seventh(chords.ii7(key), shorthand=True)[0]
    return [ii_chord_type_short, chord]

ACTIONS = [
    'harmonic_function',
    'tritone_substitution',
    'reharmonize_v_to_ii_v',
    'ii_v_tritone_substitution',
    'chord_modes',
    '12_bar_blues'
]

if __name__ == '__main__':
    p = ArgumentParser()
    p.add_argument('-a', '--action', help='The action to take',
                   choices=ACTIONS,
                   default='harmonic_function')
    p.add_argument('-c', '--chords', dest='chords', help='The chords', nargs='*')
    p.add_argument('-k', '--key', help='The chords', nargs='?')
    args = p.parse_args()
    if args.action == 'harmonic_function':
        for chord in args.chords:
            determine_key_and_function(chord)

    elif args.action == 'tritone_substitution':
        for chord in args.chords:
            new_chord, new_notes = tritone_substitution(chord)
            print("The tritone substitution of {} is {} ({})".format(chord, new_chord, ', '.join(new_notes)))

    elif args.action == 'reharmonize_v_to_ii_v':
        for chord in args.chords:
            ii_chord_type_short, chord = reharmonize_v_to_ii_v(chord)
            print("II-V ({}, {})".format(ii_chord_type_short, chord))

    elif args.action == 'ii_v_tritone_substitution':
        for chord in args.chords:
            chord_notes = chords.from_shorthand(chord)
            new_note = reduce_accidentals(tritone(chord_notes[0]))
            new_chord = new_note + '7'

            ii_chord_type_short, chord = reharmonize_v_to_ii_v(new_chord)
            print("{} {}".format(ii_chord_type_short, new_chord))

    elif args.action == 'chord_modes':
        chords = [chords.determine_seventh(mode_func(args.key), shorthand=True)[0]
                  for mode_func in MODE_CHORD_FUNCTIONS]
        print(', '.join(chords))

    elif args.action == '12_bar_blues':
        for four_bars in twelve_bar_blues(args.key):
            print('\t'.join(four_bars))
