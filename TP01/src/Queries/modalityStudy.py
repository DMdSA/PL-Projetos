from audioop import reverse
from EMDsParser import loadDataStructure as lDS
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

## V.02: { ano: { modalidade: [emds] } }

def getModalidades(dataset):

    ## { ano: { modalidade: [emds] } }
    modalitiesPerYear = {}

    for year in dataset:                           

        modalitiesPerYear[year] = {}
        currentYearModalities = modalitiesPerYear[year]
        
        lvl_years = dataset[year]                   ## informação presente em cada ano

        for AgeGenderFilter in lvl_years:           ## Por cada filtro encontrado,
            
            lvl_genderAge = lvl_years[AgeGenderFilter]                          # Lista de registos desse filtro

            for emdR in lvl_genderAge:

                if emdR.modality not in currentYearModalities:
                    currentYearModalities[emdR.modality] = []

                curModal = (currentYearModalities[emdR.modality])

                curModal.append(emdR)
    return modalitiesPerYear



def calculateModalidadesInfo(modalities):

    years = list(modalities.keys())
    years.sort()

    modalitiesDict = {}

    ## para cada ano na estrutura de dados
    for yearKey in modalities:

        ## para cada modalidade inserida, por ano
        for modalKey in modalities[yearKey]:

            ## se essa modalidade ainda não existir, adicioná-la à nova estrutura
            if modalKey not in modalitiesDict:
                modalitiesDict[modalKey] = {}
                ## para a inicializar, para cada ano que exista, inicializar o seu contador
                for year in years:
                    
                    (modalitiesDict[modalKey])[year] = 0
                    currentYearRegisters = 0
                    try:
                        currentYearRegisters = len((modalities[year])[modalKey])
                    except:
                        pass
                    (modalitiesDict[modalKey])[year] = currentYearRegisters

    
    return (modalitiesDict,years)
            
def modalidades_Graph(ModDict,years):

    values = [[] for _ in range(len(years))]
    modalities = []
    data = {}
    
    for modality in ModDict:
        modalities.append(modality)
        years_lvl = ModDict[modality]
        i = 0

        for datasetYear in years_lvl:
            participant = (ModDict[modality])[datasetYear]
            values[i].append(participant)
            i= i + 1
    i = 0
    for year in years:
        data[year] = values[i]
        i = i+1



    
    df = pd.DataFrame(data,columns=years,index=modalities)

    plt.style.use('ggplot')
    ax = df.plot.barh().get_figure().savefig('Modality_Bar_Graph.png')
    ax.set_ylabel("Número de Registos")
    ax.set_title("Número de Registos por Modalidade")

    plt.legend()
    plt.show()



