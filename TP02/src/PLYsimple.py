#main
import sys
sys.path.append('../')

from plySimple import plySimpleObject

plysimple = plySimpleObject.PlySimple("../inputFiles/lexteste.txt")
plysimple.readPlySimple()


plysimple.transcribe_sorted()
plysimple.transcribe_yacc_sorted()

#exec(open("test.py").read())