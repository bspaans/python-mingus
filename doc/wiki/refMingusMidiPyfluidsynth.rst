.. module:: mingus.midi.pyfluidsynth

========================
mingus.midi.pyfluidsynth
========================

Python bindings for FluidSynth.

FluidSynth is a software synthesizer for generating music.  It works like a
MIDI synthesizer.

You load patches, set parameters, then send NOTEON and NOTEOFF events to
play notes.

Instruments are defined in SoundFonts, generally files with the extension
SF2.

FluidSynth can either be used to play audio itself, or you can call a
function that returns chunks of audio data and output the data to the
soundcard yourself.

FluidSynth works on all major platforms, so pyFluidSynth should also.



.. class:: Synth


   .. method:: __init__(self, gain=0.2, samplerate=44100)

      Create a new synthesizer object to control sound generation.
      
      Optional keyword arguments:
        gain: scale factor for audio output, default is 0.2
              lower values are quieter, allow more simultaneous notes
        samplerate: output samplerate in Hz, default is 44100 Hz


   .. method:: bank_select(self, chan, bank)

      Choose a bank.


   .. method:: cc(self, chan, ctrl, val)

      Send control change value.
      
      The controls that are recognized are dependent on the
      SoundFont.  Values are always 0 to 127.  Typical controls
      include:
        1: vibrato
        7: volume
        10: pan (left to right)
        11: expression (soft to loud)
        64: sustain
        91: reverb
        93: chorus


   .. method:: delete(self)


   .. method:: get_samples(self, len=1024)

      Generate audio samples.
      
      The return value will be a NumPy array containing the given
      length of audio samples.  If the synth is set to stereo output
      (the default) the array will be size 2 * len.


   .. method:: noteoff(self, chan, key)

      Stop a note.


   .. method:: noteon(self, chan, key, vel)

      Play a note.


   .. method:: pitch_bend(self, chan, val)

      Adjust pitch of a playing channel by small amounts.
      
      A pitch bend value of 0 is no pitch change from default.
      A value of -2048 is 1 semitone down.
      A value of 2048 is 1 semitone up.
      Maximum values are -8192 to +8192 (transposing by 4 semitones).


   .. method:: program_change(self, chan, prg)

      Change the program.


   .. method:: program_reset(self)

      Reset the programs on all channels.


   .. method:: program_select(self, chan, sfid, bank, preset)

      Select a program.


   .. method:: sfload(self, filename, update_midi_preset=0)

      Load SoundFont and return its IDi.


   .. method:: sfont_select(self, chan, sfid)

      Choose a SoundFont.


   .. method:: sfunload(self, sfid, update_midi_preset=0)

      Unload a SoundFont and free memory it used.


   .. method:: start(self, driver=None)

      Start audio output driver in separate background thread.
      
      Call this function any time after creating the Synth object.
      If you don't call this function, use get_samples() to generate
      samples.
      
      Optional keyword argument:
        driver: which audio driver to use for output
                Possible choices:
                  'alsa', 'oss', 'jack', 'portaudio'
                  'sndmgr', 'coreaudio', 'Direct Sound',
                  'dsound', 'pulseaudio'
      
      Not all drivers will be available for every platform, it depends on
      which drivers were compiled into FluidSynth for your platform.


   .. method:: system_reset(self)

      Stop all notes and reset all programs.


----

.. data:: DEFAULT_MODE

      Attribute of type: int
      ``0``

----

.. data:: RTLD_GLOBAL

      Attribute of type: int
      ``256``

----

.. data:: RTLD_LOCAL

      Attribute of type: int
      ``0``

----

.. data:: api_version

      Attribute of type: str
      ``'1.2'``

----

.. data:: cdll

      Attribute of type: ctypes.LibraryLoader
      ``<ctypes.LibraryLoader object at 0x7f9066868810>``

----

.. data:: lib

      Attribute of type: str
      ``'libfluidsynth.so.1'``

----

.. data:: pydll

      Attribute of type: ctypes.LibraryLoader
      ``<ctypes.LibraryLoader object at 0x7f9066868850>``

----

.. data:: pythonapi

      Attribute of type: ctypes.PyDLL
      ``<PyDLL 'None', handle 7f9069f84188 at 7f9066868890>``

----

.. function:: ARRAY(typ, len)


----

.. function:: CFUNCTYPE(restype)

      CFUNCTYPE(restype, *argtypes,
                   use_errno=False, use_last_error=False) -> function prototype.
      
      restype: the result type
      argtypes: a sequence specifying the argument types
      
      The function prototype can be called in different ways to create a
      callable object:
      
      prototype(integer address) -> foreign function
      prototype(callable) -> create and return a C callable function from callable
      prototype(integer index, method name[, paramflags]) -> foreign function calling a COM method
      prototype((ordinal number, dll object)[, paramflags]) -> foreign function exported by ordinal
      prototype((function name, dll object)[, paramflags]) -> foreign function exported by name


----

.. function:: PYFUNCTYPE(restype)


----

.. function:: SetPointerType(pointer, cls)


----

.. function:: c_buffer(init, size=None)


----

.. function:: cast(obj, typ)


----

.. function:: cfunc(name, result)

      Build and apply a ctypes prototype complete with parameter flags.


----

.. function:: create_string_buffer(init, size=None)

      create_string_buffer(aString) -> character array
      create_string_buffer(anInteger) -> character array
      create_string_buffer(aString, anInteger) -> character array


----

.. function:: create_unicode_buffer(init, size=None)

      create_unicode_buffer(aString) -> character array
      create_unicode_buffer(anInteger) -> character array
      create_unicode_buffer(aString, anInteger) -> character array


----

.. function:: find_library(name)


----

.. function:: fluid_synth_write_s16_stereo(synth, len)

      Return generated samples in stereo 16-bit format.
      
      Return value is a Numpy array of samples.


----

.. function:: raw_audio_string(data)

      Return a string of bytes to send to soundcard.
      
      Input is a numpy array of samples. Default output format is 16-bit
      signed (other formats not currently supported).


----

.. function:: string_at(ptr, size=-1)

      string_at(addr[, size]) -> string
      
      Return the string at addr.


----

.. function:: wstring_at(ptr, size=-1)

      wstring_at(addr[, size]) -> string
      
      Return the string at addr.

----



:doc:`Back to Index</index>`
