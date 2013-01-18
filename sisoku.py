#! /usr/bin/python
# -*- coding: utf-8 -*- 

##==========##
## argument ##
##==========##
import argparse
import sys
class ArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write('error: %s\n' % message)
        self.print_help()
        sys.exit(2)
class MyFormatter(argparse.ArgumentDefaultsHelpFormatter, argparse.RawDescriptionHelpFormatter): pass
            
parser = ArgumentParser(
formatter_class=MyFormatter,
description='''
=========================================================
Sisoku Game
=========================================================
''',epilog = '''
=========================================================
hikingko1@gmail.com
2013/1/18
=========================================================
''')

parser.add_argument('input_numbers', nargs='+', type=float)

parser.add_argument('--target', type=float, default=10)

##========##
## Import ##
##========##

##=======##
## Const ##
##=======##
CALCCHARAS = ['+', '-', '*', '/']
eps = 0.001

##===========##
## Functions ##
##===========##
def sisoku_search_dfs(now, target):

    if len(now)==1:
        try:
            if eval(now[0])>target-eps and eval(now[0])<target+eps:
                return [now[0]+"="+str(eval(now[0]))]
            else:
                return []
        except ZeroDivisionError:
            return []
    
    ans = []
    for i in xrange(len(now)):
        for j in xrange(i+1, len(now)):
            for chara in CALCCHARAS:
                ans+=(sisoku_search_dfs(["("+now[i]+chara+now[j]+")"]+now[:i]+now[i+1:j]+now[j+1:], target))
                ans+=(sisoku_search_dfs(["("+now[j]+chara+now[i]+")"]+now[:i]+now[i+1:j]+now[j+1:], target))
    return ans
    
def sisoku_search(input_numbers, target):
    return sisoku_search_dfs(map(str, input_numbers), target)


def main(args):
    ##======##
    ## init ##
    ##======##
    inputs = args.input_numbers
    target = args.target
    
    ##======##
    ## main ##
    ##======##
    print sisoku_search(inputs, target)

if __name__ == '__main__':
    args = parser.parse_args()
    print args
    main(args)
