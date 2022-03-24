from EMDsParser import *
from EMDsParser import loadDataStructure
from Queries import *
from htmlGenerator import *
from htmlGenerator.datesIndicators import *
from htmlGenerator.genderIndicators import *

## load data from csv file
emdDS = loadDataStructure.buildData("dataset/emd.csv")
print(emdDS[0])

#genderIndicatorsHTML(emdDS[0])
#datesIndicatorsHtml(emdDS[0])

#datesIndicatorsHtml(emdDS[0])


    