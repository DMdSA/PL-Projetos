"""studyDS.py : main do projeto

__author__ : grupo xx
__version__ : 1.0
__credits__ : [Diogo Araújo, Diogo Rebelo, Joel Araújo]
"""

import webbrowser
from EMDsParser import *
from EMDsParser import loadDataStructure
from Queries import *
from htmlGenerator import *
from htmlGenerator import fitFedIndicators
from htmlGenerator import medResultsIndicators
from htmlGenerator.medResultsIndicators import *
from htmlGenerator.datesIndicators import *
from htmlGenerator.genderIndicators import *

## load data from csv file
emdDS = loadDataStructure.buildData("dataset/emd.csv")

#genderIndicatorsHTML(emdDS[0])
#datesIndicatorsHtml(emdDS[0])

#datesIndicatorsHtml(emdDS[0])
aa = genderAgeQueries.getGenderDetails(emdDS[0])
generos = genderAgeQueries.calculateGenderDetails(aa)
genderAgeQueries.createBarGraphGender(generos)

#medResultIndicatorsHTML(emdDS[0])

a = fitFederated.findAptosDic(emdDS[0])
fitFedIndicators.federatedIndicatorsHTML(a)
medResultsIndicators.medResultsIndicatorsHtml(a)
fitFederated.createBarGraphAptos(a)
fitFederated.createBarGraphFed(a)
fitFederated.createMultPieGraphAptos(a)
fitFederated.createMultPieGraphFed(a)

webbrowser.open_new_tab("medResultsIndicators.html")