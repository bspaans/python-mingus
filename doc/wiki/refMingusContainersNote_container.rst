.. module:: mingus.containers.note_container

================================
mingus.containers.note_container
================================


.. class:: NoteContainer


   .. method:: __add__(self, notes)

      Enable the use of the '+' operator on NoteContainers.
      
      Example:
      
      >>> n = NoteContainer(['C', 'E', 'G'])
      >>> n + 'B'
      ['C-4', 'E-4', 'G-4', 'B-4']


   .. method:: __eq__(self, other)

      Enable the '==' operator for NoteContainer instances.


   .. method:: __getitem__(self, item)

      Enable the use of the container as a simple array.
      
      Example:
      
      >>> n = NoteContainer(['C', 'E', 'G'])
      >>> n[0]
      'C-4'


   .. method:: __init__(self, notes=[])


   .. method:: __len__(self)

      Return the number of notes in the container.


   .. method:: __repr__(self)

      Return a nice and clean string representing the note container.


   .. method:: __setitem__(self, item, value)

      Enable the use of the [] notation on NoteContainers.
      
      This function accepts Notes and notes as string.
      
      Example:
      
      >>> n = NoteContainer(['C', 'E', 'G'])
      >>> n[0] = 'B'
      >>> n
      ['B-4', 'E-4', 'G-4']


   .. method:: __sub__(self, notes)

      Enable the use of the '-' operator on NoteContainers.
      
      Example:
      
      >>> n = NoteContainer(['C', 'E', 'G'])
      >>> n - 'E'
      ['C-4', 'G-4']


   .. method:: _consonance_test(self, testfunc, param=None)

      Private function used for testing consonance/dissonance.


   .. method:: add_note(self, note, octave=None, dynamics={})

      Add a note to the container and sorts the notes from low to high.
      
      The note can either be a string, in which case you could also use
      the octave and dynamics arguments, or a Note object.


   .. method:: add_notes(self, notes)

      Feed notes to self.add_note.
      
      The notes can either be an other NoteContainer, a list of Note
      objects or strings or a list of lists formatted like this:
      
      >>> notes = [['C', 5], ['E', 5], ['G', 6]]
      
      or even:
      >>> notes = [['C', 5, {'volume': 20}], ['E', 6, {'volume': 20}]]


   .. method:: augment(self)

      Augment all the notes in the NoteContainer.


   .. method:: determine(self, shorthand=False)

      Determine the type of chord or interval currently in the
      container.


   .. method:: diminish(self)

      Diminish all the notes in the NoteContainer.


   .. method:: empty(self)

      Empty the container.


   .. method:: from_chord(self, shorthand)

      Shortcut to from_chord_shorthand.


   .. method:: from_chord_shorthand(self, shorthand)

      Empty the container and add the notes in the shorthand.
      
      See mingus.core.chords.from_shorthand for an up to date list of
      recognized format.
      
      Example:
      
      >>> NoteContainer().from_chord_shorthand('Am')
      ['A-4', 'C-5', 'E-5']


   .. method:: from_interval(self, startnote, shorthand, up=True)

      Shortcut to from_interval_shorthand.


   .. method:: from_interval_shorthand(self, startnote, shorthand, up=True)

      Empty the container and add the note described in the startnote and
      shorthand.
      
      See core.intervals for the recognized format.
      
      Examples:
      
      >>> nc = NoteContainer()
      >>> nc.from_interval_shorthand('C', '5')
      ['C-4', 'G-4']
      >>> nc.from_interval_shorthand('C', '5', False)
      ['F-3', 'C-4']


   .. method:: from_progression(self, shorthand, key=C)

      Shortcut to from_progression_shorthand.


   .. method:: from_progression_shorthand(self, shorthand, key=C)

      Empty the container and add the notes described in the progressions
      shorthand (eg. 'IIm6', 'V7', etc).
      
      See mingus.core.progressions for all the recognized format.
      
      Example:
      
      >>> NoteContainer().from_progression_shorthand('VI')
      ['A-4', 'C-5', 'E-5']


   .. method:: get_note_names(self)

      Return a list with all the note names in the current container.
      
      Every name will only be mentioned once.


   .. method:: is_consonant(self, include_fourths=True)

      Test whether the notes are consonants.
      
      See the core.intervals module for a longer description on
      consonance.


   .. method:: is_dissonant(self, include_fourths=False)

      Test whether the notes are dissonants.
      
      See the core.intervals module for a longer description.


   .. method:: is_imperfect_consonant(self)

      Test whether the notes are imperfect consonants.
      
      See the core.intervals module for a longer description on
      consonance.


   .. method:: is_perfect_consonant(self, include_fourths=True)

      Test whether the notes are perfect consonants.
      
      See the core.intervals module for a longer description on
      consonance.


   .. attribute:: notes

      Attribute of type: list
      ``[]``

   .. method:: remove_duplicate_notes(self)

      Remove duplicate and enharmonic notes from the container.


   .. method:: remove_note(self, note, octave=-1)

      Remove note from container.
      
      The note can either be a Note object or a string representing the
      note's name. If no specific octave is given, the note gets removed
      in every octave.


   .. method:: remove_notes(self, notes)

      Remove notes from the containers.
      
      This function accepts a list of Note objects or notes as strings and
      also single strings or Note objects.


   .. method:: sort(self)

      Sort the notes in the container from low to high.


   .. method:: transpose(self, interval, up=True)

      Transpose all the notes in the container up or down the given
      interval.

----



:doc:`Back to Index</index>`
