"""studyDS.py : main do projeto

__author__ : grupo xx
__version__ : 1.0
__credits__ : [Diogo Araújo, Diogo Rebelo, Joel Araújo]
"""

from EMDsParser import *
from EMDsParser import loadDataStructure
from Queries import *
from htmlGenerator import *
from htmlGenerator import modalityIndicators
from htmlGenerator.datesIndicators import *
from htmlGenerator.genderIndicators import *

## load data from csv file
emdDS = loadDataStructure.buildData("dataset/emd.csv")

modals = modalityStudy.getModalities(emdDS[0])

modalityIndicators.modalityIndicatorsHtml("modalidades.html", modals)
