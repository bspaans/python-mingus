======================
mingus.midi.midi_track
======================

Methods for working with MIDI data as bytes.

The MIDI file format specification I used can be found here:
http://www.sonicspot.com/guide/midifiles.html



----

.. attribute:: BALANCE

   Attribute of type: int (8)

----

.. attribute:: BANK_SELECT

   Attribute of type: int (0)

----

.. attribute:: BREATH_CONTROLLER

   Attribute of type: int (2)

----

.. attribute:: CHANNEL_AFTERTOUCH

   Attribute of type: int (13)

----

.. attribute:: CONTROLLER

   Attribute of type: int (11)

----

.. attribute:: COPYRIGHT_NOTICE

   Attribute of type: str ('\x02')

----

.. attribute:: CUE_POINT

   Attribute of type: str ('\x07')

----

.. attribute:: DATA_ENTRY_MSB

   Attribute of type: int (6)

----

.. attribute:: EFFECT_CONTROL_1

   Attribute of type: int (12)

----

.. attribute:: EFFECT_CONTROL_2

   Attribute of type: int (13)

----

.. attribute:: END_OF_TRACK

   Attribute of type: str ('/')

----

.. attribute:: EXPRESSION_CONTROLLER

   Attribute of type: int (11)

----

.. attribute:: FILE_HEADER

   Attribute of type: str ('MThd')

----

.. attribute:: FOOT_CONTROLLER

   Attribute of type: int (4)

----

.. attribute:: INSTRUMENT_NAME

   Attribute of type: str ('\x04')

----

.. attribute:: KEY_SIGNATURE

   Attribute of type: str ('Y')

----

.. attribute:: LYRICS

   Attribute of type: str ('\x05')

----

.. attribute:: MAIN_VOLUME

   Attribute of type: int (7)

----

.. attribute:: MARKER

   Attribute of type: str ('\x06')

----

.. attribute:: META_EVENT

   Attribute of type: str ('\xff')

----

.. attribute:: MIDI_CHANNEL_PREFIX

   Attribute of type: str (' ')

----

.. attribute:: MODULATION

   Attribute of type: int (1)

----

.. attribute:: NOTE_AFTERTOUCH

   Attribute of type: int (10)

----

.. attribute:: NOTE_OFF

   Attribute of type: int (8)

----

.. attribute:: NOTE_ON

   Attribute of type: int (9)

----

.. attribute:: PAN

   Attribute of type: int (10)

----

.. attribute:: PITCH_BEND

   Attribute of type: int (14)

----

.. attribute:: PORTAMENTO_TIME

   Attribute of type: int (5)

----

.. attribute:: PROGRAM_CHANGE

   Attribute of type: int (12)

----

.. attribute:: SEQUENCE_NUMBER

   Attribute of type: str ('\x00')

----

.. attribute:: SET_TEMPO

   Attribute of type: str ('Q')

----

.. attribute:: SMPTE_OFFSET

   Attribute of type: str ('T')

----

.. attribute:: TEXT_EVENT

   Attribute of type: str ('\x01')

----

.. attribute:: TIME_SIGNATURE

   Attribute of type: str ('X')

----

.. attribute:: TRACK_HEADER

   Attribute of type: str ('MTrk')

----

.. attribute:: TRACK_NAME

   Attribute of type: str ('\x03')

----

.. attribute:: major_keys

   Attribute of type: list (['Cb', 'Gb', 'Db', 'Ab', 'Eb', 'Bb', 'F', 'C', 'G', 'D', 'A', 'E', 'B', 'F#', 'C#'])

----

.. attribute:: minor_keys

   Attribute of type: list (['ab', 'eb', 'bb', 'f', 'c', 'g', 'd', 'a', 'e', 'b', 'f#', 'c#', 'g#', 'd#', 'a#'])
:doc:`Back to Index</index>`
