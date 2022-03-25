from EMDsParser import loadDataStructure as lDS
import matplotlib.pyplot as plt
import numpy as np

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
            
def modalidades_Graph(dataset,years):

    barWidth = 0.25
    fig = plt.subplots(figsize =(12, 8)) 
    colors = ['#0034FF','#FF007B','#00FF14','#FF0000','#FFED00','#BA00FF']
    values = []
    modalities = []
    aux = []

    for x in range (0,len(years)):
        values.append(aux)

    for modality in dataset:
        modalities.append(modality)
        i = 0
        for datasetYear in dataset:
            print(dataset)
            print(modality)
            participant = dataset[modality][datasetYear]
            print(participant)
            values[i].append(str(participant))
            i= i + 1
    j = 0
    fig = plt.figure()

    for year in years:
        x = np.arrange(len(values))
        plt.bar((x + barWidth*j), values[j], color = colors[j], width = barWidth,
        edgecolor ='grey', label = modalities[j])
        j = j +1
    
    plt.xticks([r + barWidth for r in range(len(values[0]))],years)
 
    plt.xlabel("Anos")
    plt.ylabel("Número de Registos")
    plt.title("Numbero de Registos por Genero")
    plt.legend()
    plt.show()
    fig.savefig('Gender_Bar_Graph.png')



