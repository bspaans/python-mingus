======================
mingus.midi.midi_track
======================

Methods for working with MIDI data as bytes.

The MIDI file format specification I used can be found here:
http://www.sonicspot.com/guide/midifiles.html



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
:doc:`Back to Index</index>`
