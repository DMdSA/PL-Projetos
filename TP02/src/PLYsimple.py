#main
import sys
sys.path.append('../')

from plySimple import plySimpleObject

plysimple = plySimpleObject.PlySimple("../inputFiles/lexteste.txt")
plysimple.readPlySimple()

#plysimple.transcribeLex()
#plysimple.transcribeYacc()

#plysimple.transcribe_sorted()

#exec(open("test.py").read())