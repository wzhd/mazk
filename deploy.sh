#!/usr/bin/env bash
OUTPUT_DIR=output
cd output
git add -A
git status -s
git commit -m "update from Travis-CI build $TRAVIS_BUILD_NUMBER."
git push --quiet