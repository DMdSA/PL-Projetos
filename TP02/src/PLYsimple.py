#main
import sys
sys.path.append('../')

from plySimple import plySimpleObject

plysimple = plySimpleObject.PlySimple("../inputFiles/lexteste.txt","ply_file.py")
plysimple.readPlySimple()


plysimple.transcribe_plySimple()

#exec(open("test.py").read())