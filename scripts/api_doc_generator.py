#!/usr/bin/python
# -*- coding: utf-8 -*-

#    mingus - Music theory Python package, generate_wiki_docs module.
#    Copyright (C) 2008, 2009, Bart Spaans
#    Copyright (C) 2011, Carlo Stemberger
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Script for updating the automatically generated documentation.

This module builds the reference documentation for mingus.
"""

import mingus
from mingus.core import *
from mingus.containers import *
from mingus.extra import *
from mingus.midi import *
import types
import inspect
import sys
import os
import inspect

class Documize(object):

    """Generate documents from modules."""

    functions = []
    classes = []
    attributes = []

    def __init__(self, module_string=''):
        self.set_module(module_string)

    def process_element_recursively(self, element_string, element_evaled, is_class = False):
        for element in dir(element_evaled):
            e = eval('{0}.{1}'.format(element_string, element))
            if not callable(e):
                self.generate_non_callable_docs(element_string, element, e, is_class)
            else:
                self.generate_callable_wikidocs(element_string, element, e, is_class)

    def generate_module_wikidocs(self):
        self.reset()
        header = '=' * len(self.module_string)
        res = '.. module:: %s\n\n' % self.module_string
        res += '%s\n%s\n%s\n\n' % (header, self.module_string, header)

        if self.module.__doc__ is not None:
            res += self.module.__doc__ + '\n\n'

        # Gather all the documentation
        self.process_element_recursively(self.module_string, self.module)

        # Order it
        self.functions.sort()
        self.attributes.sort()

        # Present classes
        for c in self.classes:
            res += c

        # Present attributes
        for a in self.attributes:
            res += a

        # Present functions
        for f in self.functions:
            res += f
        res += '----\n\n'
        res += '\n\n:doc:`Back to Index</index>`\n'
        return res

    def generate_non_callable_docs(self, module_string, element_string, evaled, is_class = False):
        if element_string[0] != '_' and type(evaled) != types.ModuleType:
            t = str(type(evaled))
            t = t.split("'")
            directive = "----\n\n.. data" if not is_class else "   .. attribute"
            res = '\n{0}:: {1}\n\n'.format(directive , element_string)
            res += '      Attribute of type: {0}\n'.format(t[1])
            res += '      ``{0}``\n'.format(repr(evaled))
            if not is_class:
                self.attributes.append(res)
            else:
                self.classes.append(res)

    def generate_callable_wikidocs(self, module_string, element_string, evaled, is_class = False):
        if type(evaled) in [types.FunctionType, types.MethodType]:
            docs = self.generate_function_wikidocs(element_string, evaled, is_class)
            if not is_class:
                self.functions.append(docs)
            else:
                self.classes.append(docs)
        elif type(evaled) == type:
            self.classes.append('\n.. class:: ' + element_string + '\n\n')
            module_string = module_string + "." + element_string
            self.process_element_recursively(module_string, evaled, True)
        elif hasattr(evaled, '__module__') and evaled.__module__ is not None and evaled.__module__.startswith(module_string):
            self.classes.append('\n.. class:: ' + element_string + '\n\n')
            module_string = module_string + "." + element_string
            self.process_element_recursively(module_string, evaled, True)
        else:
            pass

    def generate_function_wikidocs(self, func_string, func, is_class = False):
        directive = '----\n\n.. function' if not is_class else '   .. method'
        res = '\n{0}:: {1}('.format(directive, func_string)
        argspec = inspect.getargspec(func)
        args = argspec[0]
        defaults = argspec[3]
        def_values = []

        # Get the arguments
        for n in range(0, len(args)):
            try:
                if defaults != None and len(defaults) >= len(args) - n:
                    res += '{0}={1}, '.format(args[n], defaults[n - (len(args) - len(defaults))])
                    
                    def_values.append((args[n], defaults[n - (len(args) - len(defaults))]))
                else:
                    res += '{0}, '.format(args[n])
            except:
                res += '{0}, '.format(args[n])
        if res[-1] != '(':
            res = res[:-2]
        res += ')\n\n'

        # Add docstring
        if func.__doc__ != None:
            # Remove indentation
            doc = inspect.cleandoc(func.__doc__)
            seen_code = False

            # Add wiki syntax for code
            l = []
            for line in doc.splitlines():
                if line.startswith('>>>') and not seen_code:
                    l.append('\n      ' + line)
                    seen_code = True
                else:
                    l.append(line)
            doc = '\n      '.join(l)

            res += '      {0}\n\n'.format(doc)
        return res

    def reset(self):
        self.functions = []
        self.classes = []
        self.attributes = []

    def set_module(self, module_string):
        if module_string != '':
            self.module_string = module_string
            self.module = eval(module_string)
            self.reset()

    def output_wiki(self):
        return self.generate_module_wikidocs()


def generate_package_wikidocs(package_string, file_prefix='ref',
        file_suffix='.wiki'):
    d = Documize()
    package = eval(package_string)
    print('\nGenerating documentation for package {0}'.format(package_string))
    for element in dir(package):
        if not callable(element) and not element.startswith('__'):
            fullname = '{0}.{1}'.format(package_string, element)
            e = eval(fullname)
            typ = type(eval(fullname))
            d.set_module(fullname)
            wikiname = file_prefix
            for parts in fullname.split('.'):
                wikiname += parts.capitalize()
            wikiname += file_suffix
            print('Writing {0}...'.format(wikiname), end=' ')
            result = d.output_wiki()
            try:
                f = open(os.path.join(sys.argv[1], wikiname), 'w')
                try:
                    f.write(result)
                    print('OK')
                except:
                    print("ERROR. Couldn't write to file.")
                f.close()
            except:
                print("ERROR. Couldn't open file for writing.")

def main():
    print('mingus version 0.5, Copyright (C) 2008-2015, Bart Spaans\n')
    print('mingus comes with ABSOLUTELY NO WARRANTY. This is free')
    print('software and you are welcome to redistribute it under')
    print('certain conditions.')
    if len(sys.argv) == 1:
        print('\n\nUsage:', sys.argv[0], 'OUTPUT-DIRECTORY')
        sys.exit(1)
    elif not os.path.isdir(sys.argv[1]):
        print('\n\nError: not a valid directory:', sys.argv[1])
        sys.exit(1)
    generate_package_wikidocs('mingus.core', 'ref', '.rst')
    generate_package_wikidocs('mingus.midi', 'ref', '.rst')
    generate_package_wikidocs('mingus.containers', 'ref', '.rst')
    generate_package_wikidocs('mingus.extra', 'ref', '.rst')

if __name__ == '__main__':
    main()
