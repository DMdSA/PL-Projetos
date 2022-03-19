from EMDsParser import *
from EMDsParser import loadDataStructure
from Queries import *


## load data from csv file
emdDS = loadDataStructure.buildData("dataset/emd.csv")

genderAge = genderAgeQueries.getGenderDetails(emdDS[0])
#print(genderAge[1])
#print(genderAge)

genderDetails = genderAgeQueries.calculateGenderDetails(genderAge[0])
##for a in genderAge[1]:
##    for emdd in (genderAge[1])[a]:
##        print(emdd)


modalidades01 = modalities.getModalidades01(emdDS[0])
#print(modalidades01)


modalidades02 = modalities.getModalidades02(emdDS[0])
print(modalidades02)

#modalidadesPerYear = modalities.getModalidadeInfo01(modalidades02, "2020", "Futebol")
#modalidadesPerModal = modalities.getModalidadeInfo02(modalidades02, "Andebol")