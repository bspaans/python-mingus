#! /bin/bash

# mingus 0.5


echo mingus 0.5 - Generate documentation and upload to googlecode
echo
echo
echo =========================Generating documentation=========================
echo

mkdir tmpwiki && ./api_doc_generator.py tmpwiki &&
mv tmpwiki/*.rst ../doc/wiki/ && rm -r tmpwiki && 

echo
echo Done
