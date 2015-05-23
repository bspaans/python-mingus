#!/bin/bash -e

rm -rf doc
git checkout master doc
mv doc/wiki/mingusIndex.rst index.rst
make html
git rm -rf doc
git add sphinx_build 
git commit -m "Automated build"
git push origin sphinx-workspace

