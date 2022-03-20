
def getAddress(dataset):

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
                
    return perAddress
     

def addressInfo(addresses, city):

    info = []
    cont = 0

    for add in addresses:
        try:
            info = info + ((addresses[add])[city])
            cont = len(info)
        except:
            continue
    return (info, cont)