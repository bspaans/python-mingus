=====================
mingus.extra.musicxml
=====================

Convert mingus.containers to MusicXML files.

The MusicXML format represents common Western musical notation from the 17th
century onwards. It lets you distribute interactive sheet music online, and
use sheet music files with a wide variety of musical applications.

The MusicXML format is open for use by anyone under a royalty-free license,
and is supported by over 100 applications.

http://www.musicxml.org/xml.html



.. class:: Document


----

.. attribute:: ATTRIBUTE_NODE

   Attribute of type: int
   ``2``

----

.. attribute:: CDATA_SECTION_NODE

   Attribute of type: int
   ``4``

----

.. attribute:: COMMENT_NODE

   Attribute of type: int
   ``8``

----

.. attribute:: DOCUMENT_FRAGMENT_NODE

   Attribute of type: int
   ``11``

----

.. attribute:: DOCUMENT_NODE

   Attribute of type: int
   ``9``

----

.. attribute:: DOCUMENT_TYPE_NODE

   Attribute of type: int
   ``10``

----

.. attribute:: ELEMENT_NODE

   Attribute of type: int
   ``1``

----

.. attribute:: ENTITY_NODE

   Attribute of type: int
   ``6``

----

.. attribute:: ENTITY_REFERENCE_NODE

   Attribute of type: int
   ``5``

----

.. attribute:: NOTATION_NODE

   Attribute of type: int
   ``12``

----

.. attribute:: PROCESSING_INSTRUCTION_NODE

   Attribute of type: int
   ``7``

----

.. attribute:: TEXT_NODE

   Attribute of type: int
   ``3``

----

.. attribute:: actualEncoding

   Attribute of type: NoneType
   ``None``

----

.. attribute:: async

   Attribute of type: bool
   ``False``

----

.. attribute:: attributes

   Attribute of type: NoneType
   ``None``

----

.. attribute:: doctype

   Attribute of type: NoneType
   ``None``

----

.. attribute:: documentElement

   Attribute of type: property
   ``<property object at 0x7f0e9d417310>``

----

.. attribute:: documentURI

   Attribute of type: NoneType
   ``None``

----

.. attribute:: encoding

   Attribute of type: NoneType
   ``None``

----

.. attribute:: errorHandler

   Attribute of type: NoneType
   ``None``

----

.. attribute:: firstChild

   Attribute of type: property
   ``<property object at 0x7f0e9d471680>``

----

.. attribute:: implementation

   Attribute of type: instance
   ``<xml.dom.minidom.DOMImplementation instance at 0x7f0e9d411950>``

----

.. attribute:: lastChild

   Attribute of type: property
   ``<property object at 0x7f0e9d471788>``

----

.. attribute:: localName

   Attribute of type: property
   ``<property object at 0x7f0e9d471db8>``

----

.. attribute:: namespaceURI

   Attribute of type: NoneType
   ``None``

----

.. attribute:: nextSibling

   Attribute of type: NoneType
   ``None``

----

.. attribute:: nodeName

   Attribute of type: str
   ``'#document'``

----

.. attribute:: nodeType

   Attribute of type: int
   ``9``

----

.. attribute:: nodeValue

   Attribute of type: NoneType
   ``None``

----

.. attribute:: ownerDocument

   Attribute of type: NoneType
   ``None``

----

.. attribute:: parentNode

   Attribute of type: NoneType
   ``None``

----

.. attribute:: prefix

   Attribute of type: NoneType
   ``None``

----

.. attribute:: previousSibling

   Attribute of type: NoneType
   ``None``

----

.. attribute:: standalone

   Attribute of type: NoneType
   ``None``

----

.. attribute:: strictErrorChecking

   Attribute of type: bool
   ``False``

----

.. attribute:: version

   Attribute of type: NoneType
   ``None``

----

.. data:: major_keys

   Attribute of type: list
   ``['Cb', 'Gb', 'Db', 'Ab', 'Eb', 'Bb', 'F', 'C', 'G', 'D', 'A', 'E', 'B', 'F#', 'C#']``

----

.. data:: minor_keys

   Attribute of type: list
   ``['ab', 'eb', 'bb', 'f', 'c', 'g', 'd', 'a', 'e', 'b', 'f#', 'c#', 'g#', 'd#', 'a#']``

----

.. function:: _bar2musicxml(bar)


----

.. function:: _composition2musicxml(comp)


----

.. function:: _gcd(a=None, b=None, terms=None)

   Return greatest common divisor using Euclid's Algorithm.


----

.. function:: _lcm(a=None, b=None, terms=None)

   Return lowest common multiple.


----

.. function:: _note2musicxml(note)


----

.. function:: _track2musicxml(track)


----

.. function:: from_Bar(bar)


----

.. function:: from_Composition(comp)


----

.. function:: from_Note(note)


----

.. function:: from_Track(track)


----

.. function:: write_Composition(composition, filename, zip=False)

   Create an XML file (or MXL if compressed) for a given composition.


----

.. method:: __init__(self)


----

.. method:: __nonzero__(self)


----

.. method:: _call_user_data_handler(self, operation, src, dst)


----

.. method:: _create_entity(self, name, publicId, systemId, notationName)


----

.. method:: _create_notation(self, name, publicId, systemId)


----

.. method:: _get_actualEncoding(self)


----

.. method:: _get_async(self)


----

.. method:: _get_childNodes(self)


----

.. method:: _get_doctype(self)


----

.. method:: _get_documentElement(self)


----

.. method:: _get_documentURI(self)


----

.. method:: _get_elem_info(self, element)


----

.. method:: _get_encoding(self)


----

.. method:: _get_errorHandler(self)


----

.. method:: _get_firstChild(self)


----

.. method:: _get_lastChild(self)


----

.. method:: _get_localName(self)


----

.. method:: _get_standalone(self)


----

.. method:: _get_strictErrorChecking(self)


----

.. method:: _get_version(self)


----

.. method:: _set_async(self, async)


----

.. method:: abort(self)


----

.. method:: appendChild(self, node)


----

.. method:: cloneNode(self, deep)


----

.. method:: createAttribute(self, qName)


----

.. method:: createAttributeNS(self, namespaceURI, qualifiedName)


----

.. method:: createCDATASection(self, data)


----

.. method:: createComment(self, data)


----

.. method:: createDocumentFragment(self)


----

.. method:: createElement(self, tagName)


----

.. method:: createElementNS(self, namespaceURI, qualifiedName)


----

.. method:: createProcessingInstruction(self, target, data)


----

.. method:: createTextNode(self, data)


----

.. method:: getElementById(self, id)


----

.. method:: getElementsByTagName(self, name)


----

.. method:: getElementsByTagNameNS(self, namespaceURI, localName)


----

.. method:: getInterface(self, feature)


----

.. method:: getUserData(self, key)


----

.. method:: hasChildNodes(self)


----

.. method:: importNode(self, node, deep)


----

.. method:: insertBefore(self, newChild, refChild)


----

.. method:: isSameNode(self, other)


----

.. method:: isSupported(self, feature, version)


----

.. method:: load(self, uri)


----

.. method:: loadXML(self, source)


----

.. method:: normalize(self)


----

.. method:: removeChild(self, oldChild)


----

.. method:: renameNode(self, n, namespaceURI, name)


----

.. method:: replaceChild(self, newChild, oldChild)


----

.. method:: saveXML(self, snode)


----

.. method:: setUserData(self, key, data, handler)


----

.. method:: toprettyxml(self, indent=	, newl=
, encoding=None)


----

.. method:: toxml(self, encoding=None)


----

.. method:: unlink(self)


----

.. method:: writexml(self, writer, indent=, addindent=, newl=, encoding=None)

----



:doc:`Back to Index</index>`
