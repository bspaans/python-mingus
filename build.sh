#!/bin/bash -e

git checkout sphinx-workspace sphinx_build/html
git clean -xf
mv sphinx_build/html/* .
rm -rf sphinx_build
git add .
git commit -m "Scripted build"
git push origin gh-pages
