from EMDsParser import loadDataStructure as lDS


# V.01: GET MODALIDADES

def getModalidades01(dataset):

    ## { ano: { modalidade: { f<35: #n, f>=35: #n, m<35: #n, m>=35: #n } } }
    modalitiesPerYear = {}

    for year in dataset:                           

        modalitiesPerYear[year] = {}
        currentYearModalities = modalitiesPerYear[year]
        
        lvl_years = dataset[year]                   ## informação presente em cada ano

        for AgeGenderFilter in lvl_years:           ## Por cada filtro encontrado,
            
            lvl_genderAge = lvl_years[AgeGenderFilter]                          # Lista de registos desse filtro

            for emdR in lvl_genderAge:

                if emdR.modality not in currentYearModalities:
                    currentYearModalities[emdR.modality] = {
                                                            lDS.fLT35:0, 
                                                            lDS.fGET35:0, 
                                                            lDS.mLT35:0, 
                                                            lDS.mGET35:0
                                                            }

                curModal = (currentYearModalities[emdR.modality])

                curModal[AgeGenderFilter] = curModal[AgeGenderFilter] + 1
            
    return modalitiesPerYear

#getModalidades01(emd_DATASET[0])



## V.02: { ano: { modalidade: [emds] } }

def getModalidades02(dataset):

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

## call
#modalidades = getModalidades02(emd_DATASET[0])
##


# Retirar a informação, POR ANO, de cada MODALIDADE

def getModalidadeInfo01(modalities, year, modality):

    info = []
    try:
        info = (modalities[year])[modality]
        info.sort(key=lambda x: (x.name, x.surname))
    except:
        print("\n#> error: Variáveis não encontradas...")
    
    return info

## call
#a = getModalidadeInfo02(modalidades, "2020", "Futebol")
#print(*a, sep="\n")
##


# Retirar a informação, POR MODALIDADE, de todos os anos
from datetime import datetime

def getModalidadeInfo02(modalities, modality):

    info = []

    for year in modalities:

        try:
            info = info + ((modalities[year])[modality])
        except:
            continue
            # aquele ano pode não ter essa modalidade

    # Ordenação por data
    info.sort(key=lambda x: (datetime.strptime(x.date, '%Y-%m-%d'), x.name, x.surname))
    return info

## call
#b = getModalidadeInfo(modalidades, "Futebol")
#print(*b, sep="\n")
##