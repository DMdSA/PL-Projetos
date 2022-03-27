from cgitb import html
from EMDsParser import loadDataStructure as emdLDS

htmlStart = '''<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>


/* Definições da lista colapsavel */
.collapsible {
  background-color: #777;
  color: white;
  cursor: pointer;
  padding: 18px;
  width: 100%;
  border: none;
  text-align: left;
  outline: none;
  font-size: 15px;
}

/* Cor da caixa com o rato por cima */
.active, .collapsible:hover {
  background-color: #555;
}

/* Sinal lado direito caso esteja fechado apresenta "plus" caso esteja aberto apresenta "minus" */
.collapsible:after {
  content: '\\02795'; /* Unicode character for "plus" sign (+) */
  font-size: 13px;
  color: white;
  float: right;
  margin-left: 5px;
}
.active:after {
  content: "\\2796"; /* Unicode character for "minus" sign (-) */
}

.content {
  padding: 0 18px;
  display: none;
  overflow: hidden;
  background-color: #f1f1f1;
}

html {
  box-sizing: border-box;
  background-color: white;
}

*, *:before, *:after {
  box-sizing: inherit;
}

.dateField {
  color: grey;
}

.bottomright {
  position: fixed;
  color: red;
  bottom: 10px;
  right: 55px;
  font-size: 18px;
}

/* line between entries */
.line {
  border-top: 1px solid grey;
  flex-grow: 1;
  margin: 0 10px;
}


.data {
  flex: 0 0 50%;
  padding: 10px;
}

.feminine {
  background-color: #777;
  color: white;
  cursor: pointer;
  padding: 18px;
  width: 100%;
  border: none;
  text-align: left;
  outline: none;
  font-size: 15px;
}


</style>
</head>
<body>

<h1>Gender Indicator</h1>
<p>Registos organizados por ordem alfabetica</p>
 
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
    """Formata um registo para a sua devida representação em html
    
      Arguments:
      ---------
        emdRegister (emd) : registo de exame médico
    """

    greaterEqual35 = "GE"
    lessThan35 = "LT"
    
    ageFilter = ""
    if int(emdRegister.age) >= 35: ageFilter = greaterEqual35
    else: ageFilter = lessThan35
    filterKeys = emdRegister.date + " " + ageFilter + " " + emdRegister.gender

    emdDivFormat = '''
                <p class="dateField"> [{}] </p>
                <p>{} {} - {} {}<br>
                <b>Email:</b> {}</p>
                <div class="line"></div>
    '''.format( emdRegister.date,
                emdRegister.name, 
                emdRegister.surname, 
                emdRegister.age, 
                emdRegister.gender, 
                emdRegister.email
                )

    global htmlStart
    htmlStart = htmlStart + emdDivFormat



htmlEnd = '''

<div class = "bottomright"><a href="index.html">< HOME ></a></div>

<script>
  var coll = document.getElementsByClassName("collapsible");
  var i;

  for (i = 0; i < coll.length; i++) {
    coll[i].addEventListener("click", function() {
      this.classList.toggle("active");
      var content = this.nextElementSibling;

      if (content.style.display === "block") {
        content.style.display = "none";
      } else {
        content.style.display = "block";
      }
    });
  }
</script>
</body>
</html>
'''

def genderIndicatorsHTML(filename, dataset):

    global htmlStart
    global htmlEnd
    preparedInfo = prepareData(dataset)
    dates = list(preparedInfo.keys())
    dates.sort()

    fileHandler = open(filename, "wt", encoding="utf-8")

    for year in dates:

        htmlStart = htmlStart + '''
    <h1> {} </h1>'''.format(year)

        for gender in preparedInfo[year]:
          
          genderContent = (preparedInfo[year])[gender]
          if gender == mascKey:
          
              htmlStart = htmlStart + '''

    <button type="male" class="collapsible">Male</button>
      <div class="content">
              '''
          else:
              htmlStart = htmlStart + '''
    <button type="female" class="collapsible">Female</button>
      <div class="content">
              '''
          for emdRegister in genderContent:
              emdFormatter(emdRegister)
          
          htmlStart = htmlStart + '''
      </div>'''
        htmlStart = htmlStart + '''
    </div> '''

    fileHandler.write(htmlStart + htmlEnd)
    fileHandler.close()