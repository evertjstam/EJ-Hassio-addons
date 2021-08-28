#!/usr/bin/with-contenv bashio

apt-get install git-core

git clone --recursive git://github.com/ninjablocks/433Utils.git

cd 433Utils/RPi_utils

git clone git://git.drogon.net/wiringPi

cd wiringPi
./build

make