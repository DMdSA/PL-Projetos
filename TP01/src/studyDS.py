"""studyDS.py : main do projeto

__author__ : grupo xx
__version__ : 1.0
__credits__ : [Diogo Araújo, Diogo Rebelo, Joel Araújo]
"""

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