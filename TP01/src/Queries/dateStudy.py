from cProfile import label
import matplotlib.pyplot as plt
import numpy as np

def datesGraph(dataset):
    """Criação de um gráfico de barras com a informação da quantidade de registos por ano 

        Arguments:
        ---------
            dataset (dictionary) : estrutura de dados original com todos os registos"""

    years = []
    registPerYear = []

    yearsSorted = [x for x in dataset.keys()]
    yearsSorted.sort()

    for year in yearsSorted:
        years.append(year)
        lvl_years = dataset[year]
        sum = 0
        for AgeGenderFilter in lvl_years:
            sum = sum + len(lvl_years[AgeGenderFilter])    #Somar registos masculinos, femininos, maiores e menores do que 35 anos
        
        registPerYear.append(sum)

    fig = plt.figure()
    X_axis = np.arange(len(years))
    
    plt.bar(X_axis, registPerYear, 0.4, label = 'Nº Registos')
    
    plt.xticks(X_axis, years)
    plt.xlabel("Anos")
    plt.ylabel("Número de Registos")
    plt.title("Número de Registos, por Ano")
    plt.legend()
    fig.savefig("graphs/Dates_Bar_Graph.png")