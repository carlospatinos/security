#!/bin/bash
if [ $# -lt 1 ]
then
        echo "Usage : $0 [1|2|3]"
        exit
fi

case "$1" in

1)  echo "ssh into ubuntu"
    ssh developer@192.168.0.100
    ;;
2)  echo "ssh into ubuntu2"
    ssh developer@192.168.0.101
    ;;
3)  echo "ssh into ubuntu3"
    ssh developer@192.168.0.102
    ;;
*) echo "Ubuntu machine [$1] is not available."
   ;;
esac