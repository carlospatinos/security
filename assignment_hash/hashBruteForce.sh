#!/bin/bash
# declare an array called array and define 3 vales
names=("nOOB" "Noob")
#invalidones "Skein" "Tiger" "Whirlpool" "RIPEMD" "MD2" "HAVAL" "elf64"
hashFunction=("MD4" "MD5" "SHA1" "SHA256" "SHA384" "SHA512" )
for name in "${names[@]}"
do
    for hash in "${hashFunction[@]}"
    do
	    output=$(echo -n $name | openssl $hash | sed -e "s/(stdin)= //")
        echo "$hash on $name = $output"
    done
done



