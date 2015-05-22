#!/bin/bash -e

rm -rf doc
git checkout master doc
cp doc/wiki/mingusIndex.rst index.rst
make html

