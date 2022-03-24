
from EMDsParser import emd, tokenizer
import re

fLT35 = "femLT35"                   ## Chave para os valores ('F' < 35)
fGET35 = "femGET35"                 ## Chave para os valores ('F' >= 35)
mLT35 = "mascLT35"                  ## Chave para os valores ('M' < 35)
mGET35 = "mascGET35"                ## Chave para os valores ('F' >= 35)

import sys
import copy
from datetime import datetime

def loadData(file):

    _years = {}                     ## Nível 1 da nossa estrutura de dados

    femLT = []               
    femGET = []
    mascLT = []
    mascGET = []

    genderAgeDict = {               ## Nivel 2 da nossa estrutura de dados
                        fLT35: femLT,         # Para cada ano distinto, há um dicionário que subdivide os registos encontrados
                        fGET35: femGET,       # pelos seus valores de #GÉNERO# E #IDADE#
                        mLT35: mascLT, 
                        mGET35: mascGET
                    }  


    fHandler = open(file, "rt", encoding="utf-8")


    fHandler.readline()                                 ## A primeira linha não fará parte da procura
    tknizer = tokenizer.getTokenizer()
    nWrongRegisters = 0
    oldestDate = datetime.max
    newestDate = datetime.min

    for line in fHandler:

        # RECOLHA REGEX -----
        tknizer.input(str(line))
        tokenizerValues = [x.value for x in tknizer]

        try:
            emdR = emd.emdRecord(tokenizerValues)
        except:
            nWrongRegisters = nWrongRegisters + 1
            print("#> error: ", sys.exc_info()[0], " occorred")
            
        year = int(re.search(r'(\d{4})-', emdR.date).group(1))
        #year = (emdR.date).split('-')[0]

        auxDate = datetime.strptime(emdR.date, '%Y-%m-%d')

        if oldestDate > auxDate:
            oldestDate = auxDate

        elif newestDate < auxDate:
            newestDate = auxDate


        if year not in _years:                                  ## Para cada nova entrada de um ano diferente
            _years[year] = copy.deepcopy(genderAgeDict)         ## Copiar a estrutura de filtragem [genderAgeDict]


        if re.search(r'[fF]', emdR.gender):

            if int(emdR.age) < 35:
                ((_years[year])[fLT35]).append(emdR)
            else:
                ((_years[year])[fGET35]).append(emdR)

        elif re.search(r'[mM]', emdR.gender):
            if int(emdR.age) < 35:
                ((_years[year])[mLT35]).append(emdR)
            else:
                ((_years[year])[mGET35]).append(emdR)
        


    fHandler.close()
    oldestDate = oldestDate.strftime("%Y-%m-%d")
    newestDate = newestDate.strftime("%Y-%m-%d") 
    return (_years, nWrongRegisters, oldestDate, newestDate)



## Ordenação aplicada
def sortDataset(dataset):

    for Years in dataset:           ## iterar por ano

        lvl_years = dataset[Years]           ## nível relativo aos anos

        for AgeGenderFilter in lvl_years:    ## (dicionários F&&<35, F&&>=35, etc)

            lvl_genderAge = lvl_years[AgeGenderFilter]     ## nível relativo a cada dicionário de filtro Age/Gender

            # Ordenar cada nível de filtro (i.e., cada lista com os EMD'S)
            lvl_genderAge.sort(key=lambda x: (datetime.strptime(x.date, '%Y-%m-%d'), x.name, x.address))



def buildData(file):

    datastructure = loadData(file)
    #sortDataset(datastructure[0])
    return datastructure