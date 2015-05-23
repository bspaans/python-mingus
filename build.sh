#!/bin/bash -e

git checkout sphinx-workspace sphinx_build/html
mv sphinx_build/html/* .
rm -rf sphinx_build
