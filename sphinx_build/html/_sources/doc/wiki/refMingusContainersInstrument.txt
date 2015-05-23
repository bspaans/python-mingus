.. module:: mingus.containers.instrument

============================
mingus.containers.instrument
============================


.. class:: Guitar


   .. method:: __init__(self)


   .. method:: __repr__(self)

      Return a string representing the object.


   .. method:: can_play_notes(self, notes)


   .. attribute:: clef

      Attribute of type: str
      ``'Treble'``

   .. attribute:: name

      Attribute of type: str
      ``'Guitar'``

   .. method:: note_in_range(self, note)

      Test whether note is in the range of this Instrument.
      
      Return True if so, False otherwise.


   .. method:: notes_in_range(self, notes)

      An alias for can_play_notes.


   .. attribute:: range

      Attribute of type: tuple
      ``('E-3', 'E-7')``

   .. method:: set_range(self, range)

      Set the range of the instrument.
      
      A range is a tuple of two Notes or note strings.


   .. attribute:: tuning

      Attribute of type: NoneType
      ``None``

.. class:: Instrument


   .. method:: __init__(self)


   .. method:: __repr__(self)

      Return a string representing the object.


   .. method:: can_play_notes(self, notes)

      Test if the notes lie within the range of the instrument.
      
      Return True if so, False otherwise.


   .. attribute:: clef

      Attribute of type: str
      ``'bass and treble'``

   .. attribute:: name

      Attribute of type: str
      ``'Instrument'``

   .. method:: note_in_range(self, note)

      Test whether note is in the range of this Instrument.
      
      Return True if so, False otherwise.


   .. method:: notes_in_range(self, notes)

      An alias for can_play_notes.


   .. attribute:: range

      Attribute of type: tuple
      ``('C-0', 'C-8')``

   .. method:: set_range(self, range)

      Set the range of the instrument.
      
      A range is a tuple of two Notes or note strings.


   .. attribute:: tuning

      Attribute of type: NoneType
      ``None``

.. class:: MidiInstrument


   .. method:: __init__(self, name=)


   .. method:: __repr__(self)

      Return a string representing the object.


   .. method:: can_play_notes(self, notes)

      Test if the notes lie within the range of the instrument.
      
      Return True if so, False otherwise.


   .. attribute:: clef

      Attribute of type: str
      ``'bass and treble'``

   .. attribute:: instrument_nr

      Attribute of type: int
      ``1``

   .. attribute:: name

      Attribute of type: str
      ``''``

   .. attribute:: names

      Attribute of type: list
      ``['Acoustic Grand Piano', 'Bright Acoustic Piano', 'Electric Grand Piano', 'Honky-tonk Piano', 'Electric Piano 1', 'Electric Piano 2', 'Harpsichord', 'Clavi', 'Celesta', 'Glockenspiel', 'Music Box', 'Vibraphone', 'Marimba', 'Xylophone', 'Tubular Bells', 'Dulcimer', 'Drawbar Organ', 'Percussive Organ', 'Rock Organ', 'Church Organ', 'Reed Organ', 'Accordion', 'Harmonica', 'Tango Accordion', 'Acoustic Guitar (nylon)', 'Acoustic Guitar (steel)', 'Electric Guitar (jazz)', 'Electric Guitar (clean)', 'Electric Guitar (muted)', 'Overdriven Guitar', 'Distortion Guitar', 'Guitar harmonics', 'Acoustic Bass', 'Electric Bass (finger)', 'Electric Bass (pick)', 'Fretless Bass', 'Slap Bass 1', 'Slap Bass 2', 'Synth Bass 1', 'Synth Bass 2', 'Violin', 'Viola', 'Cello', 'Contrabass', 'Tremolo Strings', 'Pizzicato Strings', 'Orchestral Harp', 'Timpani', 'String Ensemble 1', 'String Ensemble 2', 'SynthStrings 1', 'SynthStrings 2', 'Choir Aahs', 'Voice Oohs', 'Synth Voice', 'Orchestra Hit', 'Trumpet', 'Trombone', 'Tuba', 'Muted Trumpet', 'French Horn', 'Brass Section', 'SynthBrass 1', 'SynthBrass 2', 'Soprano Sax', 'Alto Sax', 'Tenor Sax', 'Baritone Sax', 'Oboe', 'English Horn', 'Bassoon', 'Clarinet', 'Piccolo', 'Flute', 'Recorder', 'Pan Flute', 'Blown Bottle', 'Shakuhachi', 'Whistle', 'Ocarina', 'Lead1 (square)', 'Lead2 (sawtooth)', 'Lead3 (calliope)', 'Lead4 (chiff)', 'Lead5 (charang)', 'Lead6 (voice)', 'Lead7 (fifths)', 'Lead8 (bass + lead)', 'Pad1 (new age)', 'Pad2 (warm)', 'Pad3 (polysynth)', 'Pad4 (choir)', 'Pad5 (bowed)', 'Pad6 (metallic)', 'Pad7 (halo)', 'Pad8 (sweep)', 'FX1 (rain)', 'FX2 (soundtrack)', 'FX 3 (crystal)', 'FX 4 (atmosphere)', 'FX 5 (brightness)', 'FX 6 (goblins)', 'FX 7 (echoes)', 'FX 8 (sci-fi)', 'Sitar', 'Banjo', 'Shamisen', 'Koto', 'Kalimba', 'Bag pipe', 'Fiddle', 'Shanai', 'Tinkle Bell', 'Agogo', 'Steel Drums', 'Woodblock', 'Taiko Drum', 'Melodic Tom', 'Synth Drum', 'Reverse Cymbal', 'Guitar Fret Noise', 'Breath Noise', 'Seashore', 'Bird Tweet', 'Telephone Ring', 'Helicopter', 'Applause', 'Gunshot']``

   .. method:: note_in_range(self, note)

      Test whether note is in the range of this Instrument.
      
      Return True if so, False otherwise.


   .. method:: notes_in_range(self, notes)

      An alias for can_play_notes.


   .. attribute:: range

      Attribute of type: tuple
      ``('C-0', 'B-8')``

   .. method:: set_range(self, range)

      Set the range of the instrument.
      
      A range is a tuple of two Notes or note strings.


   .. attribute:: tuning

      Attribute of type: NoneType
      ``None``

.. class:: Piano


   .. method:: __init__(self)


   .. method:: __repr__(self)

      Return a string representing the object.


   .. method:: can_play_notes(self, notes)

      Test if the notes lie within the range of the instrument.
      
      Return True if so, False otherwise.


   .. attribute:: clef

      Attribute of type: str
      ``'bass and treble'``

   .. attribute:: name

      Attribute of type: str
      ``'Piano'``

   .. method:: note_in_range(self, note)

      Test whether note is in the range of this Instrument.
      
      Return True if so, False otherwise.


   .. method:: notes_in_range(self, notes)

      An alias for can_play_notes.


   .. attribute:: range

      Attribute of type: tuple
      ``('F-0', 'B-8')``

   .. method:: set_range(self, range)

      Set the range of the instrument.
      
      A range is a tuple of two Notes or note strings.


   .. attribute:: tuning

      Attribute of type: NoneType
      ``None``
----



:doc:`Back to Index</index>`
