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
  color: black;
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
  right: 55px;
  font-size: 18px;
}

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

.records {
  -webkit-columns: 2; /* Chrome, Safari, Opera */
  -moz-columns: 2; /* Firefox */
  columns: 2;
}

</style>
</head>
<body>

<h1>Registos do dataset EMD</h1>
<p>Os registos encontram-se organizados pela sua data de criação.</p>
<br>
<div class="records">
'''

## emdFormatter (emdRegister)
## Dado um objeto EMD, prepara a string correspondente à sua apresentação no ficheiro .html preparado
# @emdRegister = objeto EMD
def emdFormatter(emdRegister):

    emdDivFormat = '''

    <button type="name" class="collapsible"><div class="dateField"> [{}] </div> {} {} | Email: {}</button>
          <div class="content">
              {} {}<br>{} <br>
              Federado: {} | Apto: {}
          </div>

          '''.format(emdRegister.date,
                emdRegister.name, 
                emdRegister.surname, 
                emdRegister.email, 
                emdRegister.age, 
                emdRegister.gender,
                emdRegister.modality,
                emdRegister.federated,
                emdRegister.medicalResult )

    global htmlStart
    htmlStart = htmlStart + emdDivFormat

## HTML final format string
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

def datesIndicatorsHtml(filename, dataset):

    preparedInfo = prepareDataset(dataset)
    dates = list(preparedInfo.keys())
    dates.sort()

    fileHandler = open(filename, "wt", encoding="utf-8")

    for year in dates:

      for emd in preparedInfo[year]:
        
        emdFormatter(emd)

    fileHandler.write(htmlStart + htmlEnd)

    fileHandler.close()

## Iterando o dataset principal, organiza a informação recolhida por ano, ordenando pela sua data.
def prepareDataset(dataset):

  perYear = {}

  for year in dataset:

    perYear[year] = []

    for filter in dataset[year]:

      info = (dataset[year])[filter]
      perYear[year] = perYear[year] + info
    perYear[year].sort(key=lambda x: (datetime.strptime(x.date, '%Y-%m-%d')))

  return perYear