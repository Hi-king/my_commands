#!/bin/bash
#compile tex file with bibtex
#arguments
#    1.texfile:hoge.tex
#output
#    hoge.pdf

#check arg
if [ $# != 1 ];then
    less $0|head -n 6
    exit 1
fi

#main
basename=${1%.tex}
platex $1
jbibtex ${basename}.aux
platex $1
dvipdfmx ${basename}.dvi
gnome-open ${basename}.pdf