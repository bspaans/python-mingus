#!/bin/bash -e

CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD)
DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

cd "$DIR/../"
git checkout gh-pages
./build.sh
git add .
git commit -m "Scripted build"
git checkout "$CURRENT_BRANCH"
