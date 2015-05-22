#!/bin/bash -e
#
#	mingus build script
#	Builds mingus, registers at PyPi, generates documentation and uploads to Google code

VERSION=`grep version setup.py | awk -F = '{print $2}' | awk -F \" '{print $2}'`

echo "*******************************************************************************"
echo "*****                     mingus :: Automatic Build                       *****"                     
echo "*****                  Building mingus version $VERSION                   *****"
echo "*******************************************************************************"
sudo rm -r ./build/ && sudo python setup.py install
echo "*******************************************************************************"
echo
echo "                 Registering package mingus-$VERSION at PyPi"
echo
echo "*******************************************************************************"
python setup.py register
echo "*******************************************************************************"
echo
echo "          Uploading source distribution and windows installer to PyPi"
echo
echo "*******************************************************************************"
sudo python setup.py sdist bdist_wininst upload

echo "WARNING: the code hasn't been tagged yet. Do this manually."
