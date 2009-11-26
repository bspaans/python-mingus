#!/bin/bash
# This script goes through all the python files and tidies them

for dir in doc mingus mingus_examples unittest; do
    for file in `find ${dir} -iname "*.py"`; do
        echo $file;
        ./PythonTidy-1.19.python $file > tmp;
        chmod --reference=$file tmp;
        mv tmp $file;
    done;
done;

