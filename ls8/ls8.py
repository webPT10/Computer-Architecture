#!/usr/bin/env python3

"""Main."""

import sys
from cpu import *

cpu = CPU()

# hard add argument for debugging purposes
# no command line args in vs2019 :(
#sys.argv.append('C:\\Users\\super pawn\\Desktop\\python projects\\Computer-Architecture\\ls8\\examples\print8.ls8')
#sys.argv.append('C:\\Users\\super pawn\\Desktop\\python projects\\Computer-Architecture\\ls8\\examples\mult.ls8')
# sys.argv.append('C:\\Users\\super pawn\\Desktop\\python projects\\Computer-Architecture\\ls8\\examples\call.ls8')

if len(sys.argv) > 1:
    cpu.load(sys.argv[1])
    cpu.run()
else:
    print("Add a program to run.")