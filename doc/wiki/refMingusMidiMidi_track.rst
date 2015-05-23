======================
mingus.midi.midi_track
======================

Methods for working with MIDI data as bytes.

The MIDI file format specification I used can be found here:
http://www.sonicspot.com/guide/midifiles.html


Attributes
----------


----

.. attribute::BALANCE

  * *Type*: int
  * *Value*: `8`


----

.. attribute::BANK_SELECT

  * *Type*: int
  * *Value*: `0`


----

.. attribute::BREATH_CONTROLLER

  * *Type*: int
  * *Value*: `2`


----

.. attribute::CHANNEL_AFTERTOUCH

  * *Type*: int
  * *Value*: `13`


----

.. attribute::CONTROLLER

  * *Type*: int
  * *Value*: `11`


----

.. attribute::COPYRIGHT_NOTICE

  * *Type*: str
  * *Value*: `'\x02'`


----

.. attribute::CUE_POINT

  * *Type*: str
  * *Value*: `'\x07'`


----

.. attribute::DATA_ENTRY_MSB

  * *Type*: int
  * *Value*: `6`


----

.. attribute::EFFECT_CONTROL_1

  * *Type*: int
  * *Value*: `12`


----

.. attribute::EFFECT_CONTROL_2

  * *Type*: int
  * *Value*: `13`


----

.. attribute::END_OF_TRACK

  * *Type*: str
  * *Value*: `'/'`


----

.. attribute::EXPRESSION_CONTROLLER

  * *Type*: int
  * *Value*: `11`


----

.. attribute::FILE_HEADER

  * *Type*: str
  * *Value*: `'MThd'`


----

.. attribute::FOOT_CONTROLLER

  * *Type*: int
  * *Value*: `4`


----

.. attribute::INSTRUMENT_NAME

  * *Type*: str
  * *Value*: `'\x04'`


----

.. attribute::KEY_SIGNATURE

  * *Type*: str
  * *Value*: `'Y'`


----

.. attribute::LYRICS

  * *Type*: str
  * *Value*: `'\x05'`


----

.. attribute::MAIN_VOLUME

  * *Type*: int
  * *Value*: `7`


----

.. attribute::MARKER

  * *Type*: str
  * *Value*: `'\x06'`


----

.. attribute::META_EVENT

  * *Type*: str
  * *Value*: `'\xff'`


----

.. attribute::MIDI_CHANNEL_PREFIX

  * *Type*: str
  * *Value*: `' '`


----

.. attribute::MODULATION

  * *Type*: int
  * *Value*: `1`


----

.. attribute::NOTE_AFTERTOUCH

  * *Type*: int
  * *Value*: `10`


----

.. attribute::NOTE_OFF

  * *Type*: int
  * *Value*: `8`


----

.. attribute::NOTE_ON

  * *Type*: int
  * *Value*: `9`


----

.. attribute::PAN

  * *Type*: int
  * *Value*: `10`


----

.. attribute::PITCH_BEND

  * *Type*: int
  * *Value*: `14`


----

.. attribute::PORTAMENTO_TIME

  * *Type*: int
  * *Value*: `5`


----

.. attribute::PROGRAM_CHANGE

  * *Type*: int
  * *Value*: `12`


----

.. attribute::SEQUENCE_NUMBER

  * *Type*: str
  * *Value*: `'\x00'`


----

.. attribute::SET_TEMPO

  * *Type*: str
  * *Value*: `'Q'`


----

.. attribute::SMPTE_OFFSET

  * *Type*: str
  * *Value*: `'T'`


----

.. attribute::TEXT_EVENT

  * *Type*: str
  * *Value*: `'\x01'`


----

.. attribute::TIME_SIGNATURE

  * *Type*: str
  * *Value*: `'X'`


----

.. attribute::TRACK_HEADER

  * *Type*: str
  * *Value*: `'MTrk'`


----

.. attribute::TRACK_NAME

  * *Type*: str
  * *Value*: `'\x03'`


----

.. attribute::major_keys

  * *Type*: list
  * *Value*: `['Cb', 'Gb', 'Db', 'Ab', 'Eb', 'Bb', 'F', 'C', 'G', 'D', 'A', 'E', 'B', 'F#', 'C#']`


----

.. attribute::minor_keys

  * *Type*: list
  * *Value*: `['ab', 'eb', 'bb', 'f', 'c', 'g', 'd', 'a', 'e', 'b', 'f#', 'c#', 'g#', 'd#', 'a#']`

----

:doc:`Back to Index</index>`
