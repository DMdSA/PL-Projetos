#main
import sys
sys.path.append('../')

from plySimple import plySimpleObject

plysimple = plySimpleObject.PlySimple("../inputFiles/lexteste.txt","../outputFiles/lexteste.py")
plysimple.readPlySimple()


plysimple.transcribe_plySimple()

#exec(open("test.py").read())