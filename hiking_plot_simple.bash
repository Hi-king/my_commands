#!/bin/bash

Document='
// -------------------------
//  hiking_plot_simple.plot
// -------------------------
arguments
    |- $filename
output
    |- gnuplot in X-window
options
    |-  -l: with lines
'


  # -------
  #  input
  # -------
  
  # --- get options ---
  options=""
  while getopts l OPT
  do
      echo $OPT
      case $OPT in
          "l")
              options+=" with lines"
              echo "with lines"
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
  while getopts l OPT
  do
      echo $OPT
      case $OPT in
          "l")
              options+=" with lines"
              echo "with lines"
              ;;
      esac
  done
  shift `expr $OPTIND - 1`
  



# ------
#  exec
# ------
echo gnuplot -p -e "plot \"$filename\" $options"
gnuplot -p -e "plot \"$filename\" $options"