Tutorial 4 - Instruments
========================

We have grouped Notes in NoteContainers and NoteContainers in Bars, but before we can add Bars to Tracks, we need an Instrument class.



>>> from mingus.containers.instrument import Instrument, Piano, Guitar




----


Working with Instruments
------------------------

The Instrument module is currently very basic (plans on expanding it exist), but it stores all the things the rest of mingus might need. 



>>> i = Instrument()
>>> i.name
'Instrument'
>>> i.range
('C-0', 'C-8')
>>> i.clef
'bass and treble'



The easiest way to use the Instrument class is probably to subclass it (see the Piano and Guiter classes), but you can also use the `set_range` function and `name` and `clef` attributes directly.



>>> i = Instrument()
>>> i.setrange(("C", "E"))
>>> i.name = "Keyboard - five keys"
>>> i.clef = "treble"




----


Range Checking
--------------

Because we have set a range, we can check whether or not a note is within the range of the instrument.



>>> g = Guitar()
>>> p = Piano()
>>> g.note_in_range("E")
True
>>> g.note_in_range("E-2")
False
>>> p.note_in_range("E-2")
True



To test multiple notes at once we can either use `notes_in_range` or `can_play_notes`. They both do the same thing and the alias is here for semantic reasons only.



>>> g = Guitar()
>>> g.can_play_notes(["A", "C", "E"])
True
>>> g.can_play_notes(["A-2", "C-2", "E-2"])
False




----


Midi Instruments
----------------

Another, special subclass of Instrument is the MidiInstrument, which is used throughout the `mingus.midi` module. This instrument has an extra `midi_instr` attribute which you can set to an integer (0..127) to denote the MIDI instrument patch that should be used when playing notes. A list of instrument names is provided as `names` attribute.



>>> from mingus.containers.Instrument import MidiInstrument
>>> i = MidiInstrument()
>>> i.midi_instr = 14





----


You can learn more about `mingus.containers.Instrument <refMingusContainersInstrument>`_ in the reference section

  * `Tutorial 1 - The Note Class <tutorialNoteModule>`_
  * `Tutorial 2 - NoteContainers <tutorialNoteContainerModule>`_
  * `Tutorial 3 - Bars <tutorialBarModule>`_
  * Tutorial 4 - Instruments
  * `Tutorial 5 - Tracks <tutorialTrackModule>`_
  * :doc:`Back to Index </index>`
