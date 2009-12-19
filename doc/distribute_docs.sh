#! /bin/bash

# mingus 0.2
# This little scripts checks the wiki documentation into google

echo mingus 0.2 - Generate wiki documentation and upload to googlecode
echo
echo
echo =========================Generating wiki documentation=========================
echo

~/mingus/doc/generate_wiki_docs.py &&
mv ~/mingus/doc/*.wiki ~/coding/python/mingus-gc-wiki &&

echo 
echo ===========================Listing repository info=============================
echo

cd ~/coding/python/mingus-gc-wiki &&
svn info &&

echo
echo =====================Adding .wiki files to the repository======================
echo

hg add ref*.wiki &&

echo
echo =============================Commit Changes====================================
echo

hg status -q &&
hg ci -m "Automated upload of reference docs"

echo
echo Done
