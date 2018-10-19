#!/bin/bash
pg=$(pgrep python)
pof=$(pidof python)
echo $pg
echo $pof
if [ -z $pg  ];
then
sudo reboot
else
if [ $pg = $pof ]; then
echo "Python corriendo"
fi
fi
