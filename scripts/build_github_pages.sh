#!/bin/bash -e

CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD)
DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

cd "$DIR/../"
git checkout sphinx-workspace
./build.sh

git checkout gh-pages
./build.sh

git checkout "$CURRENT_BRANCH"

