"""studyDS.py : main do projeto

__author__ : grupo xx
__version__ : 1.0
__credits__ : [Diogo Araújo, Diogo Rebelo, Joel Araújo]
"""

from EMDsParser import *
from Queries import *
from htmlGenerator import *

## load data from csv file
emdDS = loadDataStructure.buildData("dataset/emd.csv")

## dates
datesIndicators.datesIndicatorsHtml("datesIndicators", emdDS[0])

## age&Gender
ageGenderDetails = genderAgeQueries.getGenderDetails(emdDS[0])
ageGenderSorted = ageGenderDetails[1]
ageGenderIndicators.ageGenderIndicatorsHtml("ageGenderIndicators.html", ageGenderSorted)

## age
genderIndicators.genderIndicatorsHTML("genderIndicators.html", emdDS[0])

## modality
modalities = modalityStudy.getModalities(emdDS[0])
modalityIndicators.modalityIndicatorsHtml("modalityIndicators.html", modalities)

## address
addresses = addresStudy.getAddress(emdDS[0])
addressIndicators.addressIndicatorsHtml("addressIndicators.html", addresses)

## federated and med results
fitAndfed = fitFederated.findAptosDic(emdDS[0])
fitFedIndicators.federatedIndicatorsHTML("federatedIndicators.html", fitAndfed)
medResultsIndicators.medResultsIndicatorsHtml("medicalResultsIndicators.html", fitAndfed)

index.indexHTML()
