#!/bin/bash

echo 'Limpeza em curso'

find /home/bkp -name "~*.*" -delete 
#&& find /home/source -name "~*.*" -delete
find /home/bkp -name "*.db" -delete 
#&& find /home/source -name "*.db" -delete
find /home/bkp -name "~*.*" -delete 
#&& find /home/source -name "~*.*" -delete
find /home/bkp -name "*.db" -delete 
#&& find /home/source -name "*.db" -delete
find /home/bkp -name "*.tmp" -delete 
#&& find /home/source -name "*.tmp" -delete
find /home/bkp -name "*.ini" -delete 
#&& find /home/source -name "*.ini" -delete
#/home/source -name ".*" -exec rm -f '{}' \;
#/home/source -name ".*" -exec rm -fd '{}' \;