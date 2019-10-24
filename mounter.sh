#!/bin/bash

#MADE BY WINSTICKS NO SKIDDING @ENCRYPTED

function ram(){
free -g
}

while true; do read -p "cmdline> " shell

if [[ $shell = 'help' ]]; then
free - show free ram space
mount - mount the wordlist
fi

if [[ $shell = 'free' ]]; then
ram
fi

if [[ $shell = 'mount' ]]; then
echo "making dir in /mnt/ramdisk"
mkdir /mnt/ramdisk
read -p "HOW MUCH DISK SPACE IN GIGS: " GIGS
sudo mount -t tmpfs -o size=$GIGS /mnt/ramdisk
fi

done
