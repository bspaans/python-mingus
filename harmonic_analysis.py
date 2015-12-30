from argparse import ArgumentParser
from mingus.core import chords
from mingus.core.keys import keys as all_keys, get_notes, is_valid_key
from mingus.core.intervals import (interval, minor_fifth as tritone, minor_third, perfect_fourth, major_fifth,
                                   minor_seventh)
from mingus.core.scales import _Scale, Blues
from mingus.core.harmony import (CIRCLE_OF_5THS, MODE_CHORD_TYPE, MODE_CHORD_FUNCTIONS,
                                 analyze_7th_chord as analyze_chord)
from mingus.containers.bar import Bar
from mingus.core.progressions import twelve_bar_blues_chord_progression
from mingus.core.notes import reduce_accidentals
from mingus.extra.lilypond import from_Bar, to_png

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

def tritone_substitution(chord):
    chord_notes = chords.from_shorthand(chord)
    new_note = reduce_accidentals(tritone(chord_notes[0]))
    new_chord = new_note + '7'
    new_notes = chords.from_shorthand(new_chord)
    return new_chord, new_notes

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

def group(lst, n):
    """
    http://code.activestate.com/recipes/303060-group-a-list-into-sequential-n-tuples/
    """
    for i in range(0, len(lst), n):
        val = lst[i:i+n]
        if len(val) == n:
            yield tuple(val)

def twelve_bar_blues(key):
    return list(group(twelve_bar_blues_chord_progression(key), 4))

BLUES_INTERVAL = [
    minor_third,
    perfect_fourth,
    tritone,
    major_fifth,
    minor_seventh
]

def blues_scale(key):
    yield key
    for interval_fn in BLUES_INTERVAL:
        yield reduce_accidentals(interval_fn(key))

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
    '12_bar_blues',
    'blues_scale',
    '12_bar_blues_printout'
]

if __name__ == '__main__':
    p = ArgumentParser()
    p.add_argument('-a', '--action', help='The action to take',
                   choices=ACTIONS,
                   default='harmonic_function')
    p.add_argument('-c', '--chords', dest='chords', help='The chords', nargs='*')
    p.add_argument('-f', '--file-name', dest='filename', help='The name of a file for relevant actions', nargs='?')
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

    elif args.action == 'blues_scale':
        print("{} blues scale: {}".format(args.key, ', '.join(blues_scale(args.key))))

    elif args.action == '12_bar_blues_printout':
        from mingus.containers.note import QuarterNoteFactory as Q
        from mingus.core.chords import WholNoteChordFactory as WNC
        blues_scale = Blues(args.key)
        bar = Bar()
        bar.extend(Q(list(blues_scale.generate(4*12, undulating=True, starting_octave=4))))
        bar.set_chord_notes([WNC(chord) for chord in twelve_bar_blues_chord_progression(args.key)])
        result = from_Bar(bar)
        print(result)
        to_png(result, args.filename)
