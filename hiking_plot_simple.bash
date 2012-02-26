#!/bin/bash

Document='
============================
 hiking_plot_simple.plot
----------------------------
arguments
    |- $filename
output
    |- gnuplot in X-window
    |- if(-s)
        |- out.eps
options
    |-  -l: with lines
    |-  -s: output to epsfile
    |-  -d: $s...$e
        |- $s : start dimention
        |- $e : end dimention
============================
'

# --- init ---
plotcommand=""
startdim=1
enddim=1
enddiminput=0

# --- get options ---
options=""
while getopts d:ls OPT
do
    echo $OPT
    case $OPT in
        "l")
            options+=" with lines"
            echo "with lines"
            ;;
        "s")
            plotcommand=$plotcommand'set terminal postscript eps enhanced color;set output "out.eps";'
            ;;
        "d")
            echo $OPTARG
            D=(${OPTARG//.../ })
            echo ${D[0]}
            echo ${D[1]}
            startdim=${D[0]}
            enddiminput=${D[1]}
            ;;
    esac
done
shift `expr $OPTIND - 1`


# --- arguments ---
if [ $# -lt 1 ];then
   echo "$Document"
   exit 1
fi

filename=$1
shift 1

# --- get options ---
while getopts d:ls OPT
do
    echo $OPT
    case $OPT in
        "l")
            options+=" with lines"
            echo "with lines"
            ;;
        "s")
            plotcommand=$plotcommand'set terminal postscript eps enhanced color;set output "out.eps";'
            ;;
        "d")
            echo $OPTARG
            D=(${OPTARG//.../ })
            echo ${D[0]}
            echo ${D[1]}
            startdim=${D[0]}
            enddiminput=${D[1]}
            ;;
    esac
done
shift `expr $OPTIND - 1`
  


# ------
#  exec
# ------

## --- enddim --- 
if(test $enddiminput -eq 0);then ##enddiminput==0
    D=(`less $filename|tr "," " "|wc`)
    enddim=$((D[1]/D[0]))
else
    enddim=$enddiminput
fi

## --- outputfilename ---
outfile=${filename%.*}"_D"$startdim"toD"$enddim.eps
echo $outfile
plotcommand=${plotcommand//out.eps/$outfile}

## --- plot ---
plotcommand=$plotcommand"plot "
for((i=startdim;i<=$enddim;i++)){
  plotcommand=$plotcommand"\"$filename\" using 0:$i $options,"    
}
plotcommand=`echo $plotcommand|sed "s/.\$//"`

echo $plotcommand
echo -e gnuplot -p -e "'$plotcommand' "
gnuplot -p -e "$plotcommand"
#gnuplot -p -e "$plotcommand"
#gnuplot -p -e "plot \"$filename\" $options"