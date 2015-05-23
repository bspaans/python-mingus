.. module:: mingus.midi.midi_track

======================
mingus.midi.midi_track
======================

Methods for working with MIDI data as bytes.

The MIDI file format specification I used can be found here:
http://www.sonicspot.com/guide/midifiles.html



.. class:: MidiTrack


   .. method:: __init__(self, start_bpm=120)


   .. attribute:: bpm

      Attribute of type: int
      ``120``

   .. attribute:: change_instrument

      Attribute of type: bool
      ``False``

   .. method:: controller_event(self, channel, contr_nr, contr_val)

      Return the bytes for a MIDI controller event.


   .. attribute:: delay

      Attribute of type: int
      ``0``

   .. attribute:: delta_time

      Attribute of type: str
      ``'\x00'``

   .. method:: end_of_track(self)

      Return the bytes for an end of track meta event.


   .. method:: get_midi_data(self)

      Return the MIDI data in bytes for this track.
      
      Include header, track_data and the end of track meta event.


   .. method:: header(self)

      Return the bytes for the header of track.
      
      The header contains the length of the track_data, so you'll have to
      call this function when you're done adding data (when you're not
      using get_midi_data).


   .. attribute:: instrument

      Attribute of type: int
      ``1``

   .. method:: int_to_varbyte(self, value)

      Convert an integer into a variable length byte.
      
      How it works: the bytes are stored in big-endian (significant bit
      first), the highest bit of the byte (mask 0x80) is set when there
      are more bytes following. The remaining 7 bits (mask 0x7F) are used
      to store the value.


   .. method:: key_signature_event(self, key=C)

      Return the bytes for a key signature event.


   .. method:: midi_event(self, event_type, channel, param1, param2=None)

      Convert and return the paraters as a MIDI event in bytes.


   .. method:: note_off(self, channel, note, velocity)

      Return bytes for a 'note off' event.


   .. method:: note_on(self, channel, note, velocity)

      Return bytes for a 'note_on' event.


   .. method:: play_Bar(self, bar)

      Convert a Bar object to MIDI events and write them to the
      track_data.


   .. method:: play_Note(self, note)

      Convert a Note object to a midi event and adds it to the
      track_data.
      
      To set the channel on which to play this note, set Note.channel, the
      same goes for Note.velocity.


   .. method:: play_NoteContainer(self, notecontainer)

      Convert a mingus.containers.NoteContainer to the equivalent MIDI
      events and add it to the track_data.
      
      Note.channel and Note.velocity can be set as well.


   .. method:: play_Track(self, track)

      Convert a Track object to MIDI events and write them to the
      track_data.


   .. method:: program_change_event(self, channel, instr)

      Return the bytes for a program change controller event.


   .. method:: reset(self)

      Reset track_data and delta_time.


   .. method:: select_bank(self, channel, bank)

      Return the MIDI event for a select bank controller event.


   .. method:: set_deltatime(self, delta_time)

      Set the delta_time.
      
      Can be an integer or a variable length byte.


   .. method:: set_instrument(self, channel, instr, bank=1)

      Add a program change and bank select event to the track_data.


   .. method:: set_key(self, key=C)

      Add a key signature event to the track_data.


   .. method:: set_meter(self, meter=(4, 4))

      Add a time signature event for meter to track_data.


   .. method:: set_tempo(self, bpm)

      Convert the bpm to a midi event and write it to the track_data.


   .. method:: set_tempo_event(self, bpm)

      Calculate the microseconds per quarter note.


   .. method:: set_track_name(self, name)

      Add a meta event for the track.


   .. method:: stop_Note(self, note)

      Add a note_off event for note to event_track.


   .. method:: stop_NoteContainer(self, notecontainer)

      Add note_off events for each note in the NoteContainer to the
      track_data.


   .. method:: time_signature_event(self, meter=(4, 4))

      Return a time signature event for meter.


   .. attribute:: track_data

      Attribute of type: str
      ``''``

   .. method:: track_name_event(self, name)

      Return the bytes for a track name meta event.


----

.. data:: BALANCE

      Attribute of type: int
      ``8``

----

.. data:: BANK_SELECT

      Attribute of type: int
      ``0``

----

.. data:: BREATH_CONTROLLER

      Attribute of type: int
      ``2``

----

.. data:: CHANNEL_AFTERTOUCH

      Attribute of type: int
      ``13``

----

.. data:: CONTROLLER

      Attribute of type: int
      ``11``

----

.. data:: COPYRIGHT_NOTICE

      Attribute of type: str
      ``'\x02'``

----

.. data:: CUE_POINT

      Attribute of type: str
      ``'\x07'``

----

.. data:: DATA_ENTRY_MSB

      Attribute of type: int
      ``6``

----

.. data:: EFFECT_CONTROL_1

      Attribute of type: int
      ``12``

----

.. data:: EFFECT_CONTROL_2

      Attribute of type: int
      ``13``

----

.. data:: END_OF_TRACK

      Attribute of type: str
      ``'/'``

----

.. data:: EXPRESSION_CONTROLLER

      Attribute of type: int
      ``11``

----

.. data:: FILE_HEADER

      Attribute of type: str
      ``'MThd'``

----

.. data:: FOOT_CONTROLLER

      Attribute of type: int
      ``4``

----

.. data:: INSTRUMENT_NAME

      Attribute of type: str
      ``'\x04'``

----

.. data:: KEY_SIGNATURE

      Attribute of type: str
      ``'Y'``

----

.. data:: LYRICS

      Attribute of type: str
      ``'\x05'``

----

.. data:: MAIN_VOLUME

      Attribute of type: int
      ``7``

----

.. data:: MARKER

      Attribute of type: str
      ``'\x06'``

----

.. data:: META_EVENT

      Attribute of type: str
      ``'\xff'``

----

.. data:: MIDI_CHANNEL_PREFIX

      Attribute of type: str
      ``' '``

----

.. data:: MODULATION

      Attribute of type: int
      ``1``

----

.. data:: NOTE_AFTERTOUCH

      Attribute of type: int
      ``10``

----

.. data:: NOTE_OFF

      Attribute of type: int
      ``8``

----

.. data:: NOTE_ON

      Attribute of type: int
      ``9``

----

.. data:: PAN

      Attribute of type: int
      ``10``

----

.. data:: PITCH_BEND

      Attribute of type: int
      ``14``

----

.. data:: PORTAMENTO_TIME

      Attribute of type: int
      ``5``

----

.. data:: PROGRAM_CHANGE

      Attribute of type: int
      ``12``

----

.. data:: SEQUENCE_NUMBER

      Attribute of type: str
      ``'\x00'``

----

.. data:: SET_TEMPO

      Attribute of type: str
      ``'Q'``

----

.. data:: SMPTE_OFFSET

      Attribute of type: str
      ``'T'``

----

.. data:: TEXT_EVENT

      Attribute of type: str
      ``'\x01'``

----

.. data:: TIME_SIGNATURE

      Attribute of type: str
      ``'X'``

----

.. data:: TRACK_HEADER

      Attribute of type: str
      ``'MTrk'``

----

.. data:: TRACK_NAME

      Attribute of type: str
      ``'\x03'``

----

.. data:: major_keys

      Attribute of type: list
      ``['Cb', 'Gb', 'Db', 'Ab', 'Eb', 'Bb', 'F', 'C', 'G', 'D', 'A', 'E', 'B', 'F#', 'C#']``

----

.. data:: minor_keys

      Attribute of type: list
      ``['ab', 'eb', 'bb', 'f', 'c', 'g', 'd', 'a', 'e', 'b', 'f#', 'c#', 'g#', 'd#', 'a#']``
----



:doc:`Back to Index</index>`
