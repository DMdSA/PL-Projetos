
import copy
import matplotlib.pyplot as plt
import numpy as np


aptosKey = "nAptos" 
fedKey = "nFederados" 
overallKey = "nRegistos"  
aptosListKey = "aptosList"
fedListKey = "fedList"
notAptosListKey = "notAptosList"
notFedListKey = "notFedList" 

def findAptosDic(dataset):               #Criação do dataset de aptos e federados
    """Agrupa os individuos do dataset pela categoria de federados e pelo resultado de exame médico(apto ou não apto)
    
        Arguments:
        ---------
            dataset (dictionary) : estrutura de dados original com todos os registos
            
        Returns:
        -------
            YearDict (dictionary) : número de indivíduos federados,com resultado médico positivo e com os registos organizados por ano segundo essas categorias"""
    
    YearDict = {}
                     
    aptosCount = 0                         
    fedCount = 0
    overallCount = 0 
    aptosList = []
    notAptosList = []      
    fedList = []
    notFedList = []

    AptosFedDict = {               
                        aptosKey: aptosCount,              #Por ano, tem o numero de registos, aptos, federados e as listas de aptos e federados
                        fedKey: fedCount,
                        overallKey: overallCount,
                        aptosListKey: aptosList,
                        notAptosListKey: notAptosList,
                        fedListKey: fedList,
                        notFedListKey: notFedList,
                    }

    for year in dataset:
        if year not in YearDict:                                  
            YearDict[year] = copy.deepcopy(AptosFedDict)   #Criar os anos que ainda não existam
        
        lvl_years = dataset[year]

        for AgeGender in lvl_years:

            lvl_genderAge = lvl_years[AgeGender]

            for Record in lvl_genderAge:
                ((YearDict[year])[overallKey]) = ((YearDict[year])[overallKey]) + 1     #Registos desse ano
                if(Record.medicalResult == "true"): 
                    ((YearDict[year])[aptosListKey]).append(Record)                    #Adicionar o registo se apto
                else:
                    ((YearDict[year])[notAptosListKey]).append(Record)

                if(Record.federated == "true"):
                    ((YearDict[year])[fedListKey]).append(Record)                      #Adicionar o registo se federado
                else:
                    ((YearDict[year])[notFedListKey]).append(Record)
    
        ((YearDict[year])[aptosKey]) = len(((YearDict[year])[aptosListKey]))            #Numero de aptos
        ((YearDict[year])[fedKey]) = len(((YearDict[year])[fedListKey]))                #Numero de federados

        #Sort
    ((YearDict[year])[aptosListKey]).sort(key=lambda x: (x.name))   
    ((YearDict[year])[fedListKey]).sort(key=lambda x: (x.name))

    return YearDict
    

def createMultPieGraphAptos(YearDict):   #Multiplos Gráficos Pie
    """Criação de um gráfico circular com a informação da quantidade de registos com exame médico positivo e negativo, por ano

        Arguments:
        ---------
            YearDict (dictionary) : estrutura de dados com os registos organizados por federado e resultado dos exames"""

    fig, axes = plt.subplots(1, len(YearDict))  #Numero de subgráficos
    i = 0

    for year in YearDict:
        aptosArray = []
        aptosLabel = []
        aptosLabel.append("Apt")
        aptosLabel.append("Not Apt")
        aptos = ((YearDict[year][aptosKey]))
        nAptos = ((YearDict[year][overallKey])) - aptos

        aptosArray.append(aptos)
        aptosArray.append(nAptos)

        axes[i].pie(aptosArray, labels = aptosLabel, autopct='%1.1f%%', shadow = True, explode=(0, 0.1)) #Valores, Label, Percentagem, Sombra, Para o segundo valor ficar saído do gráfico
        axes[i].set_title('Apt in Year ' + str(year), fontsize = 12)
        fig.savefig('apt_Mult_Pie.png')
        i = i + 1

    plt.show()


def createMultPieGraphFed(YearDict): #Multiplos Graficos Pie para federados
    """Criação de um gráfico circular com a informação da quantidade de registos federados e não federados, por ano

        Arguments:
        ---------
            YearDict (dictionary) : estrutura de dados com os registos organizados por federado e resultado dos exames"""

    fig, axes = plt.subplots(1, len(YearDict))
    i = 0
    for year in YearDict:
        fedArray = []
        fedLabel = []
        fedLabel.append("Fed.")
        fedLabel.append("Not Fed.")

        federated = ((YearDict[year][fedKey]))
        nFederated = ((YearDict[year][overallKey])) - federated

        fedArray.append(federated)
        fedArray.append(nFederated)

        axes[i].pie(fedArray, labels = fedLabel, autopct='%1.1f%%', shadow = True, explode=(0, 0.1))
        axes[i].set_title('Fed. in Year ' + str(year), fontsize = 12)
        fig.savefig('fed_Mult_Pie.png')
        i = i + 1

    plt.show()

def createBarGraphAptos(YearDict):   #Grafico de Barras Aptos
    """Criação de um gráfico de barras com a informação da quantidade de registos com exame médico positivo e negativo, por ano

        Arguments:
        ---------
            YearDict (dictionary) : estrutura de dados com os registos organizados por federado e resultado dos exames"""

    years = []
    aptosArray = []
    nAptosArray = []
    
    for year in YearDict:
        years.append(year)
        aptos = ((YearDict[year][aptosKey]))
        nAptos = ((YearDict[year][overallKey])) - aptos

        aptosArray.append(aptos)
        nAptosArray.append(nAptos)

    fig = plt.figure()
    X_axis = np.arange(len(years))
    
    plt.bar(X_axis - 0.2, aptosArray, 0.4, label = 'Aptos')
    plt.bar(X_axis + 0.2, nAptosArray, 0.4, label = 'Não Aptos')
    
    plt.xticks(X_axis, years)
    plt.xlabel("Anos")
    plt.ylabel("Número de Registos")
    plt.title("Numbero de Registos Aptos")
    plt.legend()
    plt.show()
    fig.savefig('apt_Bar_Graph.png')

def createBarGraphFed(YearDict): #Grafico de barras Federados
    """Criação de um gráfico de barras com a informação da quantidade de registos federados e não federados, por ano

        Arguments:
        ---------
            YearDict (dictionary) : estrutura de dados com os registos organizados por federado e resultado dos exames"""

    years = []
    FedArray = []
    nFedArray = []
    
    for year in YearDict:
        years.append(year)
        aptos = ((YearDict[year][aptosKey]))
        nAptos = ((YearDict[year][overallKey])) - aptos

        FedArray.append(aptos)
        nFedArray.append(nAptos)

    fig = plt.figure()
    X_axis = np.arange(len(years))
    
    plt.bar(X_axis - 0.2, FedArray, 0.4, label = 'Federados')
    plt.bar(X_axis + 0.2, nFedArray, 0.4, label = 'Não Federados')
    
    plt.xticks(X_axis, years)
    plt.xlabel("Anos")
    plt.ylabel("Número de Registos")
    plt.title("Numbero de Registos Federados")
    plt.legend()
    plt.show()
    fig.savefig('fed_Bar_Graph.png')