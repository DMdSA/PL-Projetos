from EMDsParser import *
from EMDsParser import loadDataStructure
from Queries import *
from htmlGenerator import *
from htmlGenerator.datesIndicators import *
from htmlGenerator.genderIndicators import *

## load data from csv file
emdDS = loadDataStructure.buildData("dataset/emd.csv")

#genderIndicatorsHTML(emdDS[0])
#datesIndicatorsHtml(emdDS[0])

#datesIndicatorsHtml(emdDS[0])


modalidades = modalityStudy.getModalidades(emdDS[0])
(modalidadesValues,years) = modalityStudy.calculateModalidadesInfo(modalidades)
modalityStudy.modalidades_Graph(modalidadesValues,years)

print(modalidadesValues)
    