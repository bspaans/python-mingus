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


Attributes
----------


----

.. attribute::DEFAULT_MODE

  * *Type*: int
  * *Value*: `0`


----

.. attribute::RTLD_GLOBAL

  * *Type*: int
  * *Value*: `256`


----

.. attribute::RTLD_LOCAL

  * *Type*: int
  * *Value*: `0`


----

.. attribute::api_version

  * *Type*: str
  * *Value*: `'1.2'`


----

.. attribute::cdll

  * *Type*: ctypes.LibraryLoader
  * *Value*: `<ctypes.LibraryLoader object at 0x7f1fe06118d0>`


----

.. attribute::lib

  * *Type*: str
  * *Value*: `'libfluidsynth.so.1'`


----

.. attribute::pydll

  * *Type*: ctypes.LibraryLoader
  * *Value*: `<ctypes.LibraryLoader object at 0x7f1fe0611910>`


----

.. attribute::pythonapi

  * *Type*: ctypes.PyDLL
  * *Value*: `<PyDLL 'None', handle 7f1fe3d2e188 at 7f1fe0611950>`

----

Functions
---------


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
