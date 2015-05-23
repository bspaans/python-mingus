#!/bin/bash -e

git rm -rf doc/ genindex.html _images/ index.html _modules/ objects.inv py-modindex.html search.html searchindex.js _sources/ _static/
git checkout sphinx-workspace sphinx_build/html
mv sphinx_build/html/* .
rm -rf sphinx_build
git add doc/ genindex.html _images/ index.html _modules/ objects.inv py-modindex.html search.html searchindex.js _sources/ _static/
git commit -m "Scripted build"
git push origin gh-pages
