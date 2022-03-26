"""datesIndicators.py: html file generator para os indicadores das datas
"""

from datetime import datetime

## HTML initial file format string
htmlStart = '''<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
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
</style>
</head>
<body>



<h2>Registos do dataset EMD</h2>
<p>Os registos encontram-se organizados pela sua data de criação.</p>
<br>
<div class="row">
'''

## emdFormatter (emdRegister)
## Dado um objeto EMD, prepara a string correspondente à sua apresentação no ficheiro .html preparado
# @emdRegister = objeto EMD
def emdFormatter(emdRegister):
    """Formata um registo para a sua devida representação em html
    
      Arguments:
      ---------
        emdRegister (emd) : registo de exame médico
    """
    
    alertMessage = "\\t[{} {}]\\nAge : : {}\\nGender : : {}\\nAddress : : {}".format(emdRegister.name, emdRegister.surname, emdRegister.age, emdRegister.gender, emdRegister.address)

    emdDivFormat = '''

    <div class="column">
        <div class="card">
            <div class="container">
                <h2>{} {}</h2>
                <p class="dateField"> {} </p>
                <p> Federado: {}, Apto: {}</p>
                <p>{}</p>
                <p><button class="button" onclick="alert('{}')">Extras</button></p>
            </div>
        </div>
    </div>
    
    '''.format(emdRegister.name, 
                emdRegister.surname, 
                emdRegister.date, 
                emdRegister.federated, 
                emdRegister.medicalResult, 
                emdRegister.email,
                alertMessage)

    global htmlStart
    htmlStart = htmlStart + emdDivFormat

## HTML final format string
htmlEnd = '''
    </div>

    </body>
    </html>
    '''

## Name of the file to be written
htmlFILE = "datesIndicators.html"



def datesIndicatorsHtml(dataset):
    """Cria a página html referente aos indicadores das datas dos registos no dataset
  
    Arguments:
    ---------
      dataset (dictionary) : estrutura de dados com o dataset original
      
    """

    preparedInfo = prepareDataset(dataset)
    dates = list(preparedInfo.keys())
    dates.sort()

    fileHandler = open(htmlFILE, "wt", encoding="utf-8")

    for year in dates:

      for emd in preparedInfo[year]:
        
        emdFormatter(emd)

    fileHandler.write(htmlStart + htmlEnd)

    fileHandler.close()



def prepareDataset(dataset):
  """Organiza a estrutura de dados com o dataset original pela data dos seus registos
  
    Arguments:
    ---------
      dataset (dictionary) : estrutura de dados com o dataset original

    Returns:
      perYear (dictionary) : estrutura de dados com os registos ordenados por data, em cada ano
  """

  perYear = {}

  for year in dataset:

    perYear[year] = []

    for filter in dataset[year]:

      info = (dataset[year])[filter]
      perYear[year] = perYear[year] + info
    perYear[year].sort(key=lambda x: (datetime.strptime(x.date, '%Y-%m-%d')))

  return perYear