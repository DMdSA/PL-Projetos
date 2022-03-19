
import copy
import datetime

def findAptosDic(dataset):
    
    YearDic = {}
    
    aptosKey = "nAptos"                   
    aptosCount = 0                     
    
    fedKey = "nFederados"                 
    fedCount = 0

    aptosListKey = "aptosList"               
    aptosList = []
    
    fedListKey = "fedList"                
    fedList = []

    AptosFedDict = {               
                        aptosKey: aptosCount,
                        fedKey: fedCount,
                        aptosListKey: aptosList,
                        fedListKey: fedList,
                    }

    for year in dataset:
        if year not in YearDic:                                  
            YearDic[year] = copy.deepcopy(AptosFedDict)
        
        lvl_years = dataset[year]

        for AgeGender in lvl_years:

            lvl_genderAge = lvl_years[AgeGender]

            for Record in lvl_genderAge:
                if(Record.medicalResult == "true"):
                    ((YearDic[year])[aptosListKey]).append(Record)

                if(Record.federated == "true"):
                    ((YearDic[year])[fedListKey]).append(Record)
    
    ((YearDic[year])[aptosKey]) = len(((YearDic[year])[aptosListKey]))
    ((YearDic[year])[fedKey]) = len(((YearDic[year])[fedListKey]))
    ##((YearDic[year])[aptosListKey]).sort(key=lambda x: (x.name, datetime.strptime(x.date, '%Y-%m-%d'), x.address))
    ##((YearDic[year])[fedListKey]).sort(key=lambda x: (x.name, datetime.strptime(x.date, '%Y-%m-%d'), x.address))

    return YearDic