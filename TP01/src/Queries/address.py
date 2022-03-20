
from audioop import add
from distutils.log import info


def getAddress(dataset):

    perAddress = {}
    
    for address in dataset:

            perAddress[address] = {}
            currentAddresses = perAddress[address]

            lvl_address = dataset[address]                   

            for AgeGenderFilter in lvl_address:

                lvl_genderAge = lvl_address[AgeGenderFilter]

                for emdR in lvl_genderAge:

                        if emdR.address not in currentAddresses:
                            currentAddresses[emdR.address] = []

                        curAd = (currentAddresses[emdR.address])

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