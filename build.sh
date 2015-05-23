#!/bin/bash -e

rm -rf doc
git checkout master doc
mv doc/wiki/mingusIndex.rst index.rst
make html
git add .
git commit -m "Scripted build"

