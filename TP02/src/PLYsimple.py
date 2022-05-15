#main
import sys
sys.path.append('../')
from website import create_html
from plySimple import plySimpleObject

if len(sys.argv) == 1:
    print("#>Error, missing arguments")

elif len(sys.argv) == 2:
    if sys.argv[1].lower()== 'web':
        html = create_html()
        html.run(debug=True)
    else: 
        inputname = "../inputFiles/" + sys.argv[1]
        outputname = "../outputFiles/" + sys.argv[1].rpartition('.')[0] + ".py"

elif len(sys.argv) == 3:
    inputname = "../inputFiles/" + sys.argv[1]
    outputname = "../outputFiles/" + sys.argv[2] 

else:
    print("#> Error, too many argument")


plysimple = plySimpleObject.PlySimple(inputname,outputname)
plysimple.readPlySimple()


plysimple.transcribe_plySimple()