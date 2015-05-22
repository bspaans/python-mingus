#!/bin/bash -e

rm -rf doc
git checkout master doc
make html

