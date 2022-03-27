"""studyDS.py : main do projeto

__author__ : grupo xx
__version__ : 1.0
__credits__ : [Diogo Araújo, Diogo Rebelo, Joel Araújo]
"""

from operator import ge, mod
from EMDsParser import *
from Queries import *
from Queries import dateStudy
from htmlGenerator import *

## load data from csv file
emdDS = loadDataStructure.buildData("dataset/emd.csv")

## dates
datesIndicators.datesIndicatorsHtml("datesIndicators", emdDS[0])
dateStudy.datesGraph(emdDS[0])

## age&Gender
ageGenderDetails = genderAgeQueries.getGenderDetails(emdDS[0])
ageGenderSorted = ageGenderDetails[1]
genderDetais = genderAgeQueries.calculateGenderDetails(ageGenderDetails)
genderAgeQueries.genderAge_Graph(ageGenderDetails)
genderAgeQueries.allYearsPieGraph(genderDetais)
genderAgeQueries.createBarGraphGender(genderDetais)
genderAgeQueries.createMultPieGender(genderDetais)
ageGenderIndicators.ageGenderIndicatorsHtml("ageGenderIndicators.html", ageGenderSorted)

## age
genderIndicators.genderIndicatorsHTML("genderIndicators.html", emdDS[0])

## address
addresses = addresStudy.getAddress(emdDS[0])
addressIndicators.addressIndicatorsHtml("addressIndicators.html", addresses)
addresStudy.createBarGraphAdress(addresses)

## federated and med results
fitAndfed = fitFederated.findAptosDic(emdDS[0])
fitFederated.createBarGraphAptos(fitAndfed)
fitFederated.createBarGraphFed(fitAndfed)
fitFederated.createMultPieGraphAptos(fitAndfed)
fitFederated.createMultPieGraphFed(fitAndfed)

## modality
modalities = modalityStudy.getModalities(emdDS[0])
modalitiesInfo = modalityStudy.calculateModalitiesInfo(modalities)
modalityIndicators.modalityIndicatorsHtml("modalityIndicators.html", modalities)
modalityStudy.modalidades_Graph(modalitiesInfo)
modalityStudy.mod_graph_AllYears(modalitiesInfo[0])

fitFedIndicators.federatedIndicatorsHTML("federatedIndicators.html", fitAndfed)

medResultsIndicators.medResultsIndicatorsHtml("medicalResultsIndicators.html", fitAndfed)

index.indexHTML()
