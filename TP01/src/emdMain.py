"""emdMain.py : main do projeto

__author__ : grupo 04
__version__ : 1.0
__credits__ : [Diogo Araújo, Diogo Rebelo, Joel Araújo]
"""

from EMDsParser import *
from Queries import *
from htmlGenerator import *

## load data from csv file
emdDS = loadDataStructure.buildData("dataset/emd.csv")

## dates
datesIndicators.datesIndicatorsHtml("html/datesIndicators.html", emdDS[0])
dateStudy.datesGraph(emdDS[0])

## age&Gender
ageGenderDetails = genderAgeQueries.getGenderDetails(emdDS[0])
ageGenderSorted = ageGenderDetails[1]
genderDetais = genderAgeQueries.calculateGenderDetails(ageGenderDetails)
genderAgeQueries.genderAge_Graph(ageGenderDetails)
genderAgeQueries.allYearsPieGraph(genderDetais)
genderAgeQueries.createBarGraphGender(genderDetais)
genderAgeQueries.createMultPieGender(genderDetais)
ageGenderIndicators.ageGenderIndicatorsHtml("html/ageGenderIndicators.html", ageGenderSorted)

## age
genderIndicators.genderIndicatorsHTML("html/genderIndicators.html", emdDS[0])

## address
addresses = addresStudy.getAddress(emdDS[0])
addressIndicators.addressIndicatorsHtml("html/addressIndicators.html", addresses)
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
modalityIndicators.modalityIndicatorsHtml("html/modalityIndicators.html", modalities)
modalityStudy.modalidades_Graph(modalitiesInfo)
modalityStudy.mod_graph_AllYears(modalitiesInfo[0])

fedIndicators.federatedIndicatorsHTML("html/federatedIndicators.html", fitAndfed)
medResultsIndicators.medResultsIndicatorsHtml("html/medicalResultsIndicators.html", fitAndfed)

index.indexHTML(emdDS)