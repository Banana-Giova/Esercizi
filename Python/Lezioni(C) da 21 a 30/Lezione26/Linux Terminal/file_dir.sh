#! /bin/bash

checkf=0
checkd=0
counter=1

if test -f $1
then echo "$1 esiste ed è un file"
else checkf=1
fi

if test -d $1
then echo "$1 esiste ed è una directory"
else checkd=1
fi

if test $checkf -eq $counter && test $checkd -eq $counter
then echo "$1 non esiste"
fi
