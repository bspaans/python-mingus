from distutils.core import setup

setup(name= "mingus",
      version = "0.5.2",
      description = "mingus is a music package for Python",

      long_description = 
"""mingus is a package for Python used by programmers, musicians, \
composers and researchers to make and investigate music. At the core of mingus is music theory, \
which includes topics like intervals, chords, scales and progressions. These components are 
rigurously tested and can be used to generate and recognize musical elements using convenient 
shorthand where possible (for example some acceptable chords are: CM7, Am6, Ab7, G7).

On top of that are several packages that deal  with classical notation, MIDI (sequencing, \
loading and saving), MusicXML, ASCII tablature, and many other useful and plain cool things \
like LilyPond and FluidSynth support. Everything is fully documentated, put into simple \
APIs and has a tutorial making it easy to jump straight in.

http://mingus.googlecode.com
""",

      author = "Bart Spaans",
      author_email = "bart.spaans@gmail.com",
      url = "http://github.com/bspaans/python-mingus",
      packages = ['mingus', 'mingus.core', 'mingus.containers', 'mingus.extra', 'mingus.midi'],
      data_files = [('mingus_examples/pygame-drum', ['mingus_examples/pygame-drum/pad.png',\
                         'mingus_examples/pygame-drum/pygame-drum.py']),\
            ('mingus_examples/pygame-piano', ['mingus_examples/pygame-piano/pygame-piano.py',
                               'mingus_examples/pygame-piano/keys.png'])],
      license="GPLv3",
      classifiers = [
            'Intended Audience :: Developers',
            'Intended Audience :: Science/Research',
            'Intended Audience :: Other Audience',
            'License :: OSI Approved :: GNU General Public License (GPL)',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Topic :: Artistic Software',
            'Topic :: Education',
            'Topic :: Multimedia',
            'Topic :: Multimedia :: Graphics :: Presentation',
            'Topic :: Multimedia :: Sound/Audio',
            'Topic :: Multimedia :: Sound/Audio :: MIDI',
            'Topic :: Multimedia :: Sound/Audio :: Analysis',
            'Topic :: Scientific/Engineering :: Information Analysis',
            'Topic :: Scientific/Engineering :: Visualization',
            'Topic :: Software Development :: Libraries :: Python Modules',
              ]
      )
