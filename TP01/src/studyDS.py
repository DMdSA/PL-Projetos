from EMDsParser import *
from EMDsParser import loadDataStructure
from Queries import *
from htmlGenerator import *
from htmlGenerator.genderIndicators import *

## load data from csv file
emdDS = loadDataStructure.buildData("dataset/emd.csv")


genderIndicatorsHTML(emdDS[0])
#datesIndicatorsHtml(emdDS[0])
