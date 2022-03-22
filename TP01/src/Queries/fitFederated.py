
import copy
import datetime
import graphlib
import matplotlib.pyplot as plt
import numpy as np

aptosKey = "nAptos" 
fedKey = "nFederados" 
overallKey = "nRegistos"  
aptosListKey = "aptosList"
fedListKey = "fedList" 
def findAptosDic(dataset):               #Criação do dataset de aptos e federados
    
    YearDic = {}
                     
    aptosCount = 0                         
    fedCount = 0
    overallCount = 0 
    aptosList = []      
    fedList = []

    AptosFedDict = {               
                        aptosKey: aptosCount,              #Por ano, tem o numero de registos, aptos, federados e as listas de aptos e federados
                        fedKey: fedCount,
                        overallKey: overallCount,
                        aptosListKey: aptosList,
                        fedListKey: fedList,
                    }

    for year in dataset:
        if year not in YearDic:                                  
            YearDic[year] = copy.deepcopy(AptosFedDict)   #Criar os anos que ainda não existam
        
        lvl_years = dataset[year]

        for AgeGender in lvl_years:

            lvl_genderAge = lvl_years[AgeGender]

            for Record in lvl_genderAge:
                ((YearDic[year])[overallKey]) = ((YearDic[year])[overallKey]) + 1     #Registos desse ano
                if(Record.medicalResult == "true"): 
                    ((YearDic[year])[aptosListKey]).append(Record)                    #Adicionar o registo se apto

                if(Record.federated == "true"):
                    ((YearDic[year])[fedListKey]).append(Record)                      #Adicionar o registo se federado
    
        ((YearDic[year])[aptosKey]) = len(((YearDic[year])[aptosListKey]))            #Numero de aptos
        ((YearDic[year])[fedKey]) = len(((YearDic[year])[fedListKey]))                #Numero de federados

        #Sort
    ((YearDic[year])[aptosListKey]).sort(key=lambda x: (x.name))   
    ((YearDic[year])[fedListKey]).sort(key=lambda x: (x.name))

    return YearDic

def createPieGraphAptos(YearDic):    # Grafico Pie para os Aptos
        
    for year in YearDic:
        aptosArray = []             #Valores para o gráfico
        aptosLabel = []             #Labels
        aptosLabel.append(str(year) + " Aptos")
        aptosLabel.append(str(year) +  " Não Aptos")
        aptos = ((YearDic[year][aptosKey]))        #Aptos
        nAptos = ((YearDic[year][overallKey])) - aptos   #Não Aptos

        aptosArray.append(aptos)
        aptosArray.append(nAptos)

    plt.pie(aptosArray, labels = aptosLabel, shadow = True)   #Funções para desenhar o grafico
    plt.show()

def createMultPieGraphAptos(YearDic):   #Multiplos Gráficos Pie

    fig, axes = plt.subplots(1, len(YearDic))  #Numero de subgráficos
    i = 0

    for year in YearDic:
        aptosArray = []
        aptosLabel = []
        aptosLabel.append("Apt")
        aptosLabel.append("Not Apt")
        aptos = ((YearDic[year][aptosKey]))
        nAptos = ((YearDic[year][overallKey])) - aptos

        aptosArray.append(aptos)
        aptosArray.append(nAptos)

        axes[i].pie(aptosArray, labels = aptosLabel, autopct='%1.1f%%', shadow = True, explode=(0, 0.1)) #Valores, Label, Percentagem, Sombra, Para o segundo valor ficar saído do gráfico
        axes[i].set_title('Apt in Year ' + str(year), fontsize = 12)   
        i = i + 1

    plt.show()

        
def createPieGraphFed(YearDic):   #Grafico Pie para federados

    fedArray = []
    fedLabel = []

    for year in YearDic:
        fedLabel.append(str(year) + " Federados")
        fedLabel.append(str(year) +  " Não Federados")
        federated = ((YearDic[year][fedKey]))
        nFederated = ((YearDic[year][overallKey])) - federated

        fedArray.append(federated)
        fedArray.append(nFederated)

    plt.pie(fedArray, labels = fedLabel, shadow = True)
    plt.show()


def createMultPieGraphFed(YearDic): #Multiplos Graficos Pie para federados

    fig, axes = plt.subplots(1, len(YearDic))
    i = 0
    for year in YearDic:
        fedArray = []
        fedLabel = []
        fedLabel.append("Fed.")
        fedLabel.append("Not Fed.")

        federated = ((YearDic[year][fedKey]))
        nFederated = ((YearDic[year][overallKey])) - federated

        fedArray.append(federated)
        fedArray.append(nFederated)

        axes[i].pie(fedArray, labels = fedLabel, autopct='%1.1f%%', shadow = True, explode=(0, 0.1))
        axes[i].set_title('Fed. in Year ' + str(year), fontsize = 12)
        i = i + 1

    plt.show()

def createBarGraphAptos(YearDic):   #Grafico de Barras Aptos

    years = []
    aptosArray = []
    nAptosArray = []
    
    for year in YearDic:
        years.append(year)
        aptos = ((YearDic[year][aptosKey]))
        nAptos = ((YearDic[year][overallKey])) - aptos

        aptosArray.append(aptos)
        nAptosArray.append(nAptos)

    X_axis = np.arange(len(years))
    
    plt.bar(X_axis - 0.2, aptosArray, 0.4, label = 'Aptos')
    plt.bar(X_axis + 0.2, nAptosArray, 0.4, label = 'Não Aptos')
    
    plt.xticks(X_axis, years)
    plt.xlabel("Anos")
    plt.ylabel("Número de Registos")
    plt.title("Numbero de Registos Aptos")
    plt.legend()
    plt.show()

def createBarGraphFed(YearDic): #Grafico de barras Federados

    years = []
    FedArray = []
    nFedArray = []
    
    for year in YearDic:
        years.append(year)
        aptos = ((YearDic[year][aptosKey]))
        nAptos = ((YearDic[year][overallKey])) - aptos

        FedArray.append(aptos)
        nFedArray.append(nAptos)

    years.sort()
    X_axis = np.arange(len(years))
    
    plt.bar(X_axis - 0.2, FedArray, 0.4, label = 'Aptos')
    plt.bar(X_axis + 0.2, nFedArray, 0.4, label = 'Não Aptos')
    
    plt.xticks(X_axis, years)
    plt.xlabel("Anos")
    plt.ylabel("Número de Registos")
    plt.title("Numbero de Registos Aptos")
    plt.legend()
    plt.show()