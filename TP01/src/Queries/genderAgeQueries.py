"""genderAgeQueries.py: Queries de procura sobre idade e/ou género nos registos
"""

from operator import le
from EMDsParser import loadDataStructure as emdLDS
import matplotlib.pyplot as plt
import numpy as np


def getGenderDetails(dataset):
    """Explora o número de indivíduos presentes no dataset, por idade e género
    
        Arguments:
        ---------
            dataset (dictionary) : estrutura de dados original com todos os registos
            
        Returns:
        -------
            perYear (dictionary) : número de indivíduos registados, por ano, idade e género
        
    """

    perYear = {}
    emdRegisters = {emdLDS.fLT35: [], emdLDS.fGET35: [], emdLDS.mLT35: [], emdLDS.mGET35: []}

    for Year in dataset:                            ## por casa ano identificado

        if Year not in perYear:                     ## adicioná-lo
            perYear[Year] = [
                            {emdLDS.fLT35: 0, emdLDS.fGET35: 0},      ## Dicionário para o género 'feminino'
                            {emdLDS.mLT35: 0, emdLDS.mGET35: 0}       ## Dicionário para o género 'masculino'
                            ]

        lvl_years = dataset[Year]                   ## informação presente em cada ano

        for AgeGenderFilter in lvl_years:           ## Por cada filtro encontrado,
            
            lvl_genderAge = lvl_years[AgeGenderFilter]                          # Lista de registos desse filtro
            size = len(lvl_genderAge)                                           # Tamanho da lista
            anoAtual = perYear[Year]                                            # Ano sobre o qual estamos a calcular a informação

            if AgeGenderFilter == emdLDS.fLT35 or AgeGenderFilter == emdLDS.fGET35:               # Se o filtro for direcionado ao género 'F'
                feminino = anoAtual[0]
                feminino[AgeGenderFilter] = feminino[AgeGenderFilter] + size    # Atualizar o seu valor
                emdRegisters[AgeGenderFilter] = emdRegisters[AgeGenderFilter] + lvl_genderAge
                        
            elif AgeGenderFilter == emdLDS.mLT35 or AgeGenderFilter == emdLDS.mGET35:             # Se o filtro for direcionado ao género 'M'
                masculino = anoAtual[1]
                masculino[AgeGenderFilter] = masculino[AgeGenderFilter] + size  # Atualizar o seu valor
                emdRegisters[AgeGenderFilter] = emdRegisters[AgeGenderFilter] + lvl_genderAge

            else:
                continue                # Em caso de erro, continuar (possível erro para controlar)
    
    for filter in emdRegisters:
        toSort = emdRegisters[filter]
        toSort.sort(key=lambda x: (x.age))

    return (perYear, emdRegisters)

#genderDetails = getGenderDetails(emd_DATASET[0])
#print(genderDetails)


def calculateGenderDetails(genderDetails):
    """Cálculo do número de registos, por ano, apenas por género
    
        Arguments:
        ---------
            genderDetails (dictionary) : estrutura de dados com os registos organizados por idade&género
        
        Returns:
        -------
            eachYear (dictionary) : é devolvido o número de indivíduos, por género, em cada ano, assim como o contabilizado em todos os anos"""

    # Answer: { Ano : {M : #n, F: #n}}
    eachYear = {}
    
    ## argument details
    detailsPerYear = genderDetails[0]

    ## calculation of numbers
    allTimeFemales = 0
    allTimeMales = 0

    for year in detailsPerYear:

        currentYearFemales = 0
        currentYearMales = 0

        currentYear = detailsPerYear[year]

        for genderDict in currentYear:

            for gender in genderDict:

                if gender == emdLDS.fLT35 or gender == emdLDS.fGET35:               ## A idade não importa
                    currentYearFemales = currentYearFemales + genderDict[gender]    ## Então só se adiciona o número disponibilizado
                
                elif gender == emdLDS.mLT35 or gender == emdLDS.mGET35:
                    currentYearMales = currentYearMales + genderDict[gender]

        eachYear[year] = {"F" : currentYearFemales, "M" : currentYearMales}

        allTimeFemales = allTimeFemales + currentYearFemales
        allTimeMales = allTimeMales + currentYearMales
    
    eachYear["allYears"] = {"F": allTimeFemales, "M": allTimeMales} 
    return (eachYear)

# Com esta informação dá para calcular PERCENTAGENS e RATIOS W:M && M:W
# Para apresentar a amostragem considerada só é preciso ordená-la segundo um critério, visto que já se encontra agrupada


def createMultPieGender(genderDataSet):
    """Criação de um conjunto de gráficos circulares, um para cada ano presente no dataset
    
        Arguments:
        ---------
            genderDataSet (dictionary) : estrutura de dados com os registos organizados por género"""

    
    fig, axes = plt.subplots(1, len(genderDataSet)-1)
    i = 0
    genderLabel = []
    colors = ["#FC3EEB","#0098FF"]
    genderLabel.append("Female")
    genderLabel.append("Male")

    years = [str(x) for x in genderDataSet.keys()]
    years.sort()


    for year in years:
        if year != "allYears":
            genderArray = []

            nFemale = ((genderDataSet[int(year)])["F"])
            nMale = ((genderDataSet[int(year)])["M"])

            genderArray.append(nFemale)
            genderArray.append(nMale)

            axes[i].pie(genderArray, labels = genderLabel, colors = colors, autopct='%1.1f%%', shadow = True, explode=(0, 0.1))
            axes[i].set_title(str(year), fontsize = 12)
            fig.savefig('gender_Mult_Pie.png')
            i = i + 1

    plt.show()


def allYearsPieGraph(genderDataSet):
    """Criação de um gráfico circular com a informação da quantidade de registos masculinos e femininos na totalidade dos anos
    
        Arguments:
        ---------
            genderDataSet (dictionary) : estrutura de dados com os registos organizados por género"""

    genderArray = []
    genderLegend = []
    colors = ["#FC3EEB","#0098FF"]  # [pink,blue]
    
    genderLegend.append("Female")
    genderLegend.append("Male")
    nFemale = ((genderDataSet["allYears"])["F"])
    nMale = ((genderDataSet["allYears"])["M"])

    genderArray.append(nFemale)
    genderArray.append(nMale)

    fig = plt.figure()
    plt.pie(genderArray, labels = genderArray, colors = colors, autopct='%1.1f%%', shadow = True, explode=(0, 0.1))
    plt.title("Número de Registos por Género")
    plt.legend(genderLegend)
    plt.show()
    fig.savefig('Gender_allYears_Pie.png')
    


def createBarGraphGender(genderDataSet): 
    """Criação de um gráfico de barras com a quantidade de registos masculinos e femininos por ano
    
        Arguments:
        ---------
            genderDataSet (dictionary) : estrutura de dados com os registos organizados por género"""

    years = []
    maleArray = []
    femaleArray = []
    
    for year in genderDataSet:
        if year != "allYears":
            years.append(year)
            nFemale = ((genderDataSet[year])["F"])
            nMale = ((genderDataSet[year]["M"]))

            maleArray.append(nMale)
            femaleArray.append(nFemale)

    fig = plt.figure()
    X_axis = np.arange(len(years))
    
    plt.bar(X_axis - 0.2, femaleArray, 0.4, label = 'Female', color = "#FC3EEB")
    plt.bar(X_axis + 0.2, maleArray, 0.4, label = 'Male', color = "#0098FF")
    
    plt.xticks(X_axis, years)
    plt.xlabel("Anos")
    plt.ylabel("Número de Registos")
    plt.title("Número de Registos por Género")
    plt.legend()
    plt.show()
    fig.savefig('Gender_Bar_Graph.png')


def genderAge_Graph(ageGenderData):
    """Criação de um gráfico de barras com a quantidade de registos masculinos e femininos com mais ou menos do que 35 anos
    
        Arguments:
        ---------
            ageGenderData (dictionary) : estrutura de dados com os registos organizados por género e idade"""

    values = []
    details = ageGenderData[1]
    
    values.append(len(details[emdLDS.fLT35]))
    values.append(len(details[emdLDS.mLT35]))
    values.append(len(details[emdLDS.fGET35]))
    values.append(len(details[emdLDS.mGET35]))

    legenda = ['F < 35','M < 35', 'F >= 35','M >= 35']

    fig = plt.figure()
    
    plt.bar(legenda, values)

    plt.xlabel("Idade e Género")
    plt.ylabel("Número de Registos")
    plt.title("Número de Registos por Idade e Género")
    plt.legend()
    plt.show()
    fig.savefig('AgeGender_Bar_Graph.png')
