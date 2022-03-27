"""loadDataStructure.py : Leitura e armazenamento da informação do dataset
"""

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
    """Leitura e parsing do dataset emd.csv
    
        Arguments:
        ---------
            file : str
                path do ficheiro com o dataset

        Returns:
        -------
            _years (dictionary) : dicionário com os registos separada por anos (key primária), idade e género (key secundária)
    """

    _years = {}                     ## Nível 1 da nossa estrutura de dados

    femLT = []               
    femGET = []
    mascLT = []
    mascGET = []

    genderAgeDict = {                       ## Nivel 2 da nossa estrutura de dados
                        fLT35: femLT,         # Para cada ano distinto, há um dicionário que subdivide os registos encontrados
                        fGET35: femGET,       # pelos seus valores de #GÉNERO# E #IDADE#
                        mLT35: mascLT, 
                        mGET35: mascGET
                    }  


    fHandler = open(file, "rt", encoding="utf-8")   ## Abertura do ficheiro de texto com encoding "utf-8"

    fHandler.readline()                             ## A primeira linha não fará parte da procura
    tknizer = tokenizer.getTokenizer()              ## Tokenizer

    nWrongRegisters = 0                             ## Registar o número de registos inválidos
    oldestDate = datetime.max                       ## variável p/ procura da data mais antiga
    newestDate = datetime.min                       ## variável p/ procura da data mais recente

    for line in fHandler:

        # RECOLHA REGEX -----
        tknizer.input(str(line))
        tokenizerValues = [x.value for x in tknizer]        ## valores dos tokens apanhados no input

        try:
            emdR = emd.emdRecord(tokenizerValues)           ## se o parse for possível
            
            year = int(re.search(r'(\d{4})-', emdR.date).group(1))
            

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
        
        except:                                             ## se o parse não for possível, incrementar variável de controlo
            nWrongRegisters = nWrongRegisters + 1
            print("#> error: ", sys.exc_info()[0], " occorred")
        
    fHandler.close()

    oldestDate = oldestDate.strftime("%Y-%m-%d")
    newestDate = newestDate.strftime("%Y-%m-%d") 
    return (_years, nWrongRegisters, oldestDate, newestDate)



def sortDataset(dataset):
    """Ordenação da estrutura com o dataset original"""

    for Years in dataset:                                   ## iterar por ano

        lvl_years = dataset[Years]                          ## nível relativo aos anos

        for AgeGenderFilter in lvl_years:                   ## (dicionários F&&<35, F&&>=35, etc)

            lvl_genderAge = lvl_years[AgeGenderFilter]      ## nível relativo a cada dicionário de filtro Age/Gender

            # Ordenar cada nível de filtro (i.e., cada lista com os EMD'S)
            lvl_genderAge.sort(key=lambda x: (datetime.strptime(x.date, '%Y-%m-%d'), x.name, x.address))



def buildData(file):
    """Devolve a estrutura de dados com o dataset original"""

    datastructure = loadData(file)
    return datastructure