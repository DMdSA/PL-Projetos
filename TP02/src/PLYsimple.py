#main
import sys
sys.path.append('../')

from plySimple import plySimpleObject

if len(sys.argv) == 1:
    print("#>Error, faltam argumentos")

elif len(sys.argv) == 2:
    if sys.argv[1] == 'web':
        print("site")
        exit(0)
    else: 
        inputname = "../inputFiles/" + sys.argv[1]

elif len(sys.argv) == 3:
    inputname = "../inputFiles/" + sys.argv[1]
    outputname = "../outputFiles/" + sys.argv[2] 

else:
    print("#> Error, demasiados argumentos")


plysimple = plySimpleObject.PlySimple(inputname,outputname)
plysimple.readPlySimple()


plysimple.transcribe_plySimple()