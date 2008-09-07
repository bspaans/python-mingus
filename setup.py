from distutils.core import setup

setup(name= "mingus",
	  version = "0.3",
	  description = "mingus is an advanced music theory and notation package",
	  long_description = "mingus is an advanced music theory and notation package "\
			"for Python. It can be used to play around with music theory, to build "\
			"editors, educational tools and other applications that need to process "\
			"music. It can also be used to create sheet music with LilyPond and do "\
			"automated musicological analysis.",
	  author = "Bart Spaans",
	  author_email = "onderstekop@gmail.com",
	  url = "http://mingus.googlecode.com/",
	  packages = ['mingus', 'mingus.core', 'mingus.containers', 'mingus.extra'],
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
			'Topic :: Multimedia :: Sound/Audio :: Analysis',
			'Topic :: Scientific/Engineering :: Information Analysis',
			'Topic :: Scientific/Engineering :: Visualization',
			'Topic :: Software Development :: Libraries :: Python Modules',
			  ]
	  )
