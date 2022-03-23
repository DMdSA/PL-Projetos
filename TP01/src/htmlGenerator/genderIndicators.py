from cgitb import html
from EMDsParser import loadDataStructure as emdLDS
htmlStart = '''<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>

html {
  box-sizing: border-box;
  background-color: white;
}

*, *:before, *:after {
  box-sizing: inherit;
}

.column {
  float: left;
  width: 19.9.3%;
  margin-bottom: 16px;
  padding: 0 8px;
}

@media screen and (max-width: 650px) {
  .column {
    width: 100%;
    display: block;
  }
}

.card {
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
}

.container {
  padding: 0 16px;
}

.container::after, .row::after {
  content: "";
  clear: both;
  display: table;
}

.dateField {
  color: grey;
}
h1{
    text-align: center;
    color: darkgreen
}
.masculine{
    float: left;
    margin: -8px;
    padding: -8px;
    background-color: cyan;
}
.feminine{
    float: left;
    margin: -8px;
    padding: -8px;
    background-color: palevioletred;
}

</style>
</head>
<body>

<h1>Gender Indicators <sub style="font-size: 20px">by name, alphabetically</sub></h1>
'''

femKey = "F"
mascKey = "M"

def prepareData(dataset):

    records = {}
    for year in dataset:                            ## por casa ano identificado

        records[year] = {femKey: [], mascKey: []}
        currentYearRecords = records[year]
        lvl_years = dataset[year]

        for AgeGenderFilter in lvl_years:           ## Por cada filtro encontrado,
            
            lvl_genderAge = lvl_years[AgeGenderFilter]                          # Lista de registos desse filtro
    
            if AgeGenderFilter == emdLDS.fLT35 or AgeGenderFilter == emdLDS.fGET35:               # Se o filtro for direcionado ao género 'F'
                currentYearRecords[femKey] = currentYearRecords[femKey] + lvl_genderAge
                        
            elif AgeGenderFilter == emdLDS.mLT35 or AgeGenderFilter == emdLDS.mGET35:             # Se o filtro for direcionado ao género 'M'
                currentYearRecords[mascKey] = currentYearRecords[mascKey] + lvl_genderAge

        currentYearRecords[femKey].sort(key=lambda x: x.name)
        currentYearRecords[mascKey].sort(key=lambda x: x.name)
    return records


def emdFormatter(emdRegister):

    greaterEqual35 = "GE"
    lessThan35 = "LT"
    
    ageFilter = ""
    if int(emdRegister.age) >= 35: ageFilter = greaterEqual35
    else: ageFilter = lessThan35
    filterKeys = emdRegister.date + " " + ageFilter + " " + emdRegister.gender

    emdDivFormat = '''
    <div class="column {}">
        <div class="card">
            <div class="container">
                <h2>{} {}</h2>
                <p class="dateField"> {} </p>
                <p> Idade: {}, Género: {}</p>
                <p>{}</p>
            </div>
        </div>
    </div>
    
    '''.format(filterKeys,
                emdRegister.name, 
                emdRegister.surname, 
                emdRegister.date, 
                emdRegister.age, 
                emdRegister.gender, 
                emdRegister.email)

    global htmlStart
    htmlStart = htmlStart + emdDivFormat



htmlEnd = '''
</body>
</html>'''


## Name of the file to be written
htmlFILE = "genderIndicators.html"

def genderIndicatorsHTML(dataset):

    global htmlStart
    global htmlEnd
    preparedInfo = prepareData(dataset)
    dates = list(preparedInfo.keys())
    dates.sort()

    fileHandler = open(htmlFILE, "wt", encoding="utf-8")

    for year in dates:

        htmlStart = htmlStart + "\n<h1> " + year + "</h1>\n"

        for gender in preparedInfo[year]:
          
          genderContent = (preparedInfo[year])[gender]
          if gender == mascKey:
          
              htmlStart = htmlStart + '''
              <div class="masculine">
              '''
          else:
              htmlStart = htmlStart + '''
              <div class="feminine">
              '''
          for emdRegister in genderContent:
              emdFormatter(emdRegister)
          
          htmlStart = htmlStart + "\n</div>"



    fileHandler.write(htmlStart + htmlEnd)

    fileHandler.close()