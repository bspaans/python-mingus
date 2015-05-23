#!/bin/bash -e

rm -rf doc
git checkout master doc
mv doc/wiki/mingusIndex.rst index.rst
make html
git add sphinx_build

