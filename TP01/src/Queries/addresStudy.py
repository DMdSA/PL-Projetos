"""addresStudy.py: Exploração das moradas presentes no dataset
"""

import matplotlib.pyplot as plt
import numpy as np

def getAddress(dataset):
    """Recolhe as informações relativas às moradas presentes no dataset
    
        Argumentos:
        ----------
            dataset (dictionary) : estrutura com os dados originais do dataset
        
        Returns:
        -------
            perAddress (dictionary) : devolve as moradas com os registos a elas associados
    """

    ## { Modalidade : [emd01, emd02], (...) }

    perAddress = {}
    
    for year in dataset:
        
        datasetLvl01 = dataset[year]
        
        for filter in datasetLvl01:

            registers = datasetLvl01[filter]                   

            for emdR in registers:

                if emdR.address not in perAddress:

                    perAddress[emdR.address] = []

                curAd = (perAddress[emdR.address])
                curAd.append(emdR)

    prepareAddressEMD(perAddress)        
    return perAddress
 


def prepareAddressEMD(dataset):
    """"""
    
    addressesInfo = getAddress(dataset)

    for filter in addressInfo:
        toSort = addressInfo[filter]
        toSort.sort(key=lambda x: (x.name))

    return toSort



def addressInfo(addresses, city):
    """"""
    info = []
    cont = 0

    for add in addresses:
        try:
            info = info + ((addresses[add])[city])
            cont = len(info)
        except:
            continue
    return (info, cont)



def createBarGraphAdress(addresses): 

    addressesAux = sorted(addresses , key=lambda k: len(addresses[k]), reverse=True)   #Sort por size dos values
    addressList = []
    numberPerAddress = []

    i = 0
    for i in range (0,10):      #Para as 10 cidades com mais registos, guardar o nome e numero de registos
        addressList.append(addressesAux[i])
        numberPerAddress.append(len(addresses.get(addressesAux[i])))


    fig = plt.figure()            #criação do gráfico
    X_axis = np.arange(len(addressList))
    
    
    plt.bar(X_axis - 0.2, numberPerAddress, 0.25, label = "Nº Registos")
    fig.set_size_inches(10.5, 7.5, forward=True)
    plt.draw()
    plt.xticks(X_axis, addressList, rotation=45)
    plt.xlabel("Cidades")
    plt.ylabel("Número de Registos")
    plt.title("10 Cidades Com Mais Registos")
    plt.legend()
    plt.show()
    fig.savefig('address_Bar_Graph.png')




    #df = pd.DataFrame(data,index= addressList)
    #fig = plt.figure()
    #plt.style.use('ggplot')
    #ax = df.plot.barh().get_figure().savefig('Address_Bar_Graph.png')
    #ax.set_ylabel("Número de Registos")
    #ax.set_title("Número de Registos por Modalidade")