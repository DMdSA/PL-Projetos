"""ageGenderIndicators.py: Geração de ficheiro html para listagem de indicadores de idade e género"""

from EMDsParser import loadDataStructure as emdLDS

## HTML initial file format string
htmlStart = '''
<!DOCTYPE html>
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

.button {
  border: none;
  outline: 0;
  display: inline-block;
  padding: 8px;
  color: white;
  background-color: #000;
  text-align: center;
  cursor: pointer;
  width: 100%;
}

.button:hover {
  background-color: #555;
}

.bottomright {
  position: fixed;
  color: red;
  bottom: 10px;
  right: 15px;
  font-size: 18px;
}

/* line between entries */
.line {
  border-top: 1px solid grey;
  flex-grow: 1;
  margin: 0 10px;
}

.address {
  -webkit-columns: 2; /* Chrome, Safari, Opera */
  -moz-columns: 2; /* Firefox */
  columns: 2;
}

.data {
  flex: 0 0 50%;
  padding: 10px;
}


</style>
</head>
<body>

<h1>Idade e Genero</h1>
<p>Os dados encontram-se divididos em 4 secções e divididos por idades.
F < 35 | F >= 35 | M < 35 | M >= 35 </p>
<div class="gender">'''


def emdFormatter(emdRegister):
  """Formata um registo para a sua devida representação em html
    
      Arguments:
      ---------
        emdRegister (emd) : registo de exame médico
  """


  emdDivFormat = '''
      <p><b>Nome:</b> {} {} </p>
      <p><b>Idade:</b> {} <b>Genero:</b>{}</p>'''.format(emdRegister.name, 
                emdRegister.surname, 
                emdRegister.age,
                emdRegister.gender)

  global htmlStart
  htmlStart = htmlStart + emdDivFormat

## HTML final format string
htmlEnd = '''
</div>

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

  ## devia ser confirmado o ".html"
def ageGenderIndicatorsHtml(filename, dataset):
  """Gerador de ficheiro html para indicadores de idade&género
  
    Arguments:
    ---------
      filename (str) : nome do ficheiro final
      dataset (dictionary) : estrutura original dos dados presentes no dataset
      
  """

  global htmlStart
  global htmlEnd
 
  preparedInfo = prepareData(dataset)
  listAge = list(preparedInfo.keys())

  fileHandler = open(filename, "wt", encoding="utf-8")

  for key in listAge:
    
    if key == 'femLT35':
      htmlStart = htmlStart + '''
  <div class = "femLT35">
    <h2> Feminino < 35 anos </h2>'''

    if key == 'femGET35':
      htmlStart = htmlStart +'''
  <div class = "femGET35">
    <h2> Feminino >= 35 anos </h2>'''

    if key == 'mascLT35':
      htmlStart = htmlStart + '''
  <div class = "mascLT35">
    <h2> Masculino < 35 anos </h2>'''

    elif key == 'mascGET35':
      htmlStart = htmlStart +'''
  <div class = "mascGET35">
    <h2> Masculino >= 35 anos </h2>'''

    for emd in preparedInfo[key]:

      htmlStart = htmlStart +  '''

    <button type="testing" class="collapsible"> {} {} </button>
    <div class="content">'''.format(emd.name,emd.surname)
      emdFormatter(emd)
      
      htmlStart = htmlStart + '''
      <div class="line"></div>'''
  
    htmlStart = htmlStart + '''
    </div>    '''


  fileHandler.write(htmlStart + htmlEnd)
  fileHandler.close()



def prepareData(dataset):

  emdRegisters = {emdLDS.fLT35: [], emdLDS.fGET35: [], emdLDS.mLT35: [], emdLDS.mGET35: []}

  for year in dataset:
    lvl_years=dataset[year]

    for AgeGenderFilter in lvl_years:
      lvl_genderAge = lvl_years[AgeGenderFilter]
      
      if AgeGenderFilter == emdLDS.fLT35 or AgeGenderFilter == emdLDS.fGET35:               # Se o filtro for direcionado ao género 'F'
        emdRegisters[AgeGenderFilter] = emdRegisters[AgeGenderFilter] + lvl_genderAge
      
      elif AgeGenderFilter == emdLDS.mLT35 or AgeGenderFilter == emdLDS.mGET35:             # Se o filtro for direcionado ao género 'M'
        emdRegisters[AgeGenderFilter] = emdRegisters[AgeGenderFilter] + lvl_genderAge
      
      else:
        continue
    
    for filter in emdRegisters:
        toSort = emdRegisters[filter]
        toSort.sort(key=lambda x: (x.age))

  return emdRegisters