.. module:: mingus.midi.midi_file_in

========================
mingus.midi.midi_file_in
========================

Read a MIDI file and convert it into mingus.containers objects.


.. class:: FormatError


   .. attribute:: args

      Attribute of type: getset_descriptor
      ``<attribute 'args' of 'exceptions.BaseException' objects>``

   .. attribute:: message

      Attribute of type: getset_descriptor
      ``<attribute 'message' of 'exceptions.BaseException' objects>``

.. class:: HeaderError


   .. attribute:: args

      Attribute of type: getset_descriptor
      ``<attribute 'args' of 'exceptions.BaseException' objects>``

   .. attribute:: message

      Attribute of type: getset_descriptor
      ``<attribute 'message' of 'exceptions.BaseException' objects>``

.. class:: MidiFile


   .. method:: MIDI_to_Composition(self, file)


   .. attribute:: bpm

      Attribute of type: int
      ``120``

   .. attribute:: bytes_read

      Attribute of type: int
      ``0``

   .. method:: bytes_to_int(self, bytes)


   .. attribute:: meter

      Attribute of type: tuple
      ``(4, 4)``

   .. method:: parse_midi_event(self, fp)

      Parse a MIDI event.
      
      Return a dictionary and the number of bytes read.


   .. method:: parse_midi_file(self, file)

      Parse a MIDI file.
      
      Return the header -as a tuple containing respectively the MIDI
      format, the number of tracks and the time division-, the parsed
      track data and the number of bytes read.


   .. method:: parse_midi_file_header(self, fp)

      Read the header of a MIDI file and return a tuple containing the
      format type, number of tracks and parsed time division information.


   .. method:: parse_time_division(self, bytes)

      Parse the time division found in the header of a MIDI file and
      return a dictionary with the boolean fps set to indicate whether to
      use frames per second or ticks per beat.
      
      If fps is True, the values SMPTE_frames and clock_ticks will also be
      set. If fps is False, ticks_per_beat will hold the value.


   .. method:: parse_track(self, fp)

      Parse a MIDI track from its header to its events.
      
      Return a list of events and the number of bytes that were read.


   .. method:: parse_track_header(self, fp)

      Return the size of the track chunk.


   .. method:: parse_varbyte_as_int(self, fp, return_bytes_read=True)

      Read a variable length byte from the file and return the
      corresponding integer.


.. class:: TimeDivisionError


   .. attribute:: args

      Attribute of type: getset_descriptor
      ``<attribute 'args' of 'exceptions.BaseException' objects>``

   .. attribute:: message

      Attribute of type: getset_descriptor
      ``<attribute 'message' of 'exceptions.BaseException' objects>``

----

.. function:: MIDI_to_Composition(file)

      Convert a MIDI file to a mingus.containers.Composition and return it
      in a tuple with the last used tempo in beats per minute (this will
      change in the future).
      
      This function can raise all kinds of exceptions (IOError, HeaderError,
      TimeDivisionError, FormatError), so be sure to try and catch.

----



:doc:`Back to Index</index>`
