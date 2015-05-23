#!/bin/bash -e

git checkout gh_pages_base
git clean -df
git checkout sphinx-workspace sphinx_build/html
mv sphinx_build/html/* .
rm -rf sphinx_build
git add .
git commit -m "Scripted build"
git push origin gh-pages
