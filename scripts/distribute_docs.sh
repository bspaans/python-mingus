#! /bin/bash

# mingus 0.4
# This little scripts checks the wiki documentation into google

echo mingus 0.4 - Generate wiki documentation and upload to googlecode
echo
echo
echo =========================Generating wiki documentation=========================
echo

mkdir tmpwiki && ./generate_wiki_docs.py tmpwiki &&
mv tmpwiki/*.wiki ../doc/wiki/ && rm -r tmpwiki && 

echo
echo =====================Adding .wiki files to the repository======================
echo

hg add ../doc/wiki/ref*.wiki &&

echo
echo =============================Commit Changes====================================
echo

hg status && hg ci -m "Automated upload of reference docs"

echo
echo Done
