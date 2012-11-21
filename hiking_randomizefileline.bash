#!/bin/bash
Document='
===============================================
Randomize lines (Speedup)
-----------------------------------------------
arguments
    |- $filename
output
    |- randomized lines to STDOUT
===============================================
Algorithm is based on following web
[[http://ray.sakura.ne.jp/tips/shaffle.html]]
===============================================
'

# --- arguments ---
NEEDARGNUM=`echo "$Document"|grep -A 100 "arguments"|grep -B 100 "output"|perl -pe 's/^\(.*\n$//'|wc -l`
NEEDARGNUM=$(($NEEDARGNUM-2))
if [ $# -lt $NEEDARGNUM ];then
   echo "$Document"
   exit 1
fi

filename=$1

a=($(less $filename))
for i in $(seq 1 $((${#a[@]}-1)));do 
    randi=$(($RANDOM%$i));
    tmp=${a[$i]};
    a[$i]=${a[$randi]};
    a[$randi]=$tmp;
done;

for i in ${a[*]};do echo $i;done