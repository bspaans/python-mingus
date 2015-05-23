=================
mingus.core.meter
=================

Module for dealing with meters.

A meter is represented by a tuple. 4/4 time would look like (4,4), 3/4 like
(3,4), etc.


Attributes
----------

common_time
^^^^^^^^^^^

  * *Type*: tuple
  * *Value*: `(4, 4)`

cut_time
^^^^^^^^

  * *Type*: tuple
  * *Value*: `(2, 2)`

----

Functions
---------

.. function:: is_asymmetrical(meter)Return True if meter is an asymmetrical meter, False otherwise.

Examples:

>>> is_asymmetrical((3,4))
True
>>> is_asymmetrical((4,4))
False

.. function:: is_compound(meter)Return True if meter is a compound meter, False otherwise.

Examples:

>>> is_compound((3,4))
True
>>> is_compound((4,4))
False

.. function:: is_simple(meter)Return True if meter is a simple meter, False otherwise.

Examples:

>>> is_simple((3,4))
True
>>> is_simple((4,4))
True

.. function:: is_valid(meter)Return True if meter is a valid tuple representation of a meter.

Examples for meters are (3,4) for 3/4, (4,4) for 4/4, etc.

.. function:: valid_beat_duration(duration)Return True when log2(duration) is an integer.

----

:doc:`Back to Index</index>`
