#! /bin/bash

# mingus 0.4
# This little scripts checks the wiki documentation into google

WIKIREPO=""

if [[ "$1" ]] ; then
    if [ -d "$1" ] ; then
        WIKIREPO="$1"
    else 
        echo "Not a valid directory '$1'"
        exit 1
    fi
else
    echo "Usage: $0 WIKIREPO"
    echo "   Where WIKIREPO is a directory "
fi


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

hg status && hg ci -m "Generated wiki reference documentation"

echo
echo ==============================Push to Wiki====================================
echo

cp ../doc/wiki/*.wiki "$1" && cd "$1" && hg add *.wiki && hg status &&
hg ci -m "Updated wiki"


echo
echo Done
