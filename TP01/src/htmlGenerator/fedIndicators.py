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
}

*, *:before, *:after {
  box-sizing: inherit;
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


</style>
</head>
<body>

<h1>Federated Indicators</h1>
'''


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
</html>'''


def federatedIndicatorsHTML(filename, fitFedinfo):

  global htmlStart
  global htmlEnd

  
  fileHandler = open(filename, "wt", encoding="utf-8")

  for year in fitFedinfo:
    year_lvl = fitFedinfo[year]
    
    htmlStart = htmlStart + '''
    <h1> {} </h1>
    <button type="true" class="collapsible">Federated</button>
    <div class="content">
              '''.format(year)

    fed_records = year_lvl["fedList"]

    for record in fed_records:
        emdFormatter(record)

    htmlStart = htmlStart + '''
    </div>'''


    htmlStart = htmlStart + '''
    <button type="true" class="collapsible">Not Federated</button>
    <div class="content">
              '''

    not_fed_records = year_lvl["notFedList"]

    for record in not_fed_records:
      emdFormatter(record)
    
    htmlStart = htmlStart + '''
    </div>'''

  fileHandler.write(htmlStart + htmlEnd)
  fileHandler.close()

def emdFormatter(emdRegister):

  emdDivFormat = '''
        <p>{} {} - {} {}<br>
        <b>Fed:</b> {} <br>
        {}</p>
        <div class="line"></div>
    '''.format( emdRegister.name, 
                emdRegister.surname, 
                emdRegister.age, 
                emdRegister.gender, 
                emdRegister.federated,
                emdRegister.modality
                )

  global htmlStart
  htmlStart = htmlStart + emdDivFormat
