#summary Reference documentation for `mingus.midi.fluidsynth`.

----

= mingus.midi.fluidsynth =
FluidSynth support for mingus.

FluidSynth is a software MIDI synthesizer which allows you to play the
containers in mingus.containers real-time. To work with this module, you'll
need fluidsynth and a nice instrument collection (look here:
http://www.hammersound.net, go to Sounds → Soundfont Library → Collections).

To start using FluidSynth with mingus, do:
>>> from mingus.midi import fluidsynth
>>> fluidsynth.init('soundfontlocation.sf2')

Now you are ready to play Notes, NoteContainers, etc.


----

== Attributes ==
=== `initialized` ===
  * *Type*: bool
  * *Value*: `False`

=== `midi` ===
  * *Type*: mingus.midi.fluidsynth.FluidSynthSequencer
  * *Value*: `<mingus.midi.fluidsynth.FluidSynthSequencer object at 0x1009e52d0>`


----

== Functions ==
=== `control_change(channel, control, value)` ===
Send a control change event on channel.

=== `init(sf2, driver, file)` ===
  * *Default values*: driver = None, file = None
Initialize the audio.

Return True on success, False on failure.

This function needs to be called before you can have any audio.

The sf2 argument should be the location of a valid soundfont file.

The optional driver argument can be any of 'alsa', 'oss', 'jack',
'portaudio', 'sndmgr', 'coreaudio' or 'Direct Sound'.

If the file argument is not None, then instead of loading the driver, a
new wave file will be initialized to store the audio data.

=== `main_volume(channel, value)` ===
=== `modulation(channel, value)` ===
=== `pan(channel, value)` ===
=== `play_Bar(bar, channel, bpm)` ===
  * *Default values*: channel = 1, bpm = 120
Play a Bar object using play_NoteContainer and stop_NoteContainer.

Set a bpm attribute on a NoteContainer to change the tempo.

=== `play_Bars(bars, channels, bpm)` ===
  * *Default values*: bpm = 120
Play a list of bars on the given list of channels.

Set a bpm attribute on a NoteContainer to change the tempo.

=== `play_Composition(composition, channels, bpm)` ===
  * *Default values*: channels = None, bpm = 120
Play a composition.

=== `play_Note(note, channel, velocity)` ===
  * *Default values*: channel = 1, velocity = 100
Convert a Note object to a 'midi on' command.

The channel and velocity can be set as Note attributes as well. If
that's the case those values take presedence over the ones given here as
function arguments.

Example:
{{{
>>> n = Note('C', 4)
>>> n.channel = 9
>>> n.velocity = 50
>>> FluidSynth.play_Note(n)
}}}

=== `play_NoteContainer(nc, channel, velocity)` ===
  * *Default values*: channel = 1, velocity = 100
Use play_Note to play the Notes in the NoteContainer nc.

=== `play_Track(track, channel, bpm)` ===
  * *Default values*: channel = 1, bpm = 120
Use play_Bar to play a Track object.

=== `play_Tracks(tracks, channels, bpm)` ===
  * *Default values*: bpm = 120
Use play_Bars to play a list of Tracks on the given list of channels.

=== `set_instrument(channel, instr, bank)` ===
  * *Default values*: bank = 0
=== `stop_Note(note, channel)` ===
  * *Default values*: channel = 1
Stop the Note playing at channel.

If a channel attribute is set on the note, it will take presedence.

=== `stop_NoteContainer(nc, channel)` ===
  * *Default values*: channel = 1
Use stop_Note to stop the notes in NoteContainer nc.

=== `stop_everything()` ===
Stop all the playing notes on all channels.


----

[mingusIndex Back to Index]
