from Queries import addresStudy
from Queries import genderAgeQueries
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

.column {
  float: left;
  width: 45%;
  margin-right: 15px;
  margin-left: 15px;
}

.row:after {
content: "";
display: table;
clear: both;
}

</style>
</head>
<body>

<h1>Idade e Género</h1>
<p>Os dados encontram-se divididos em 4 secções e divididos por idades.</p>
<p>F < 35 | F >= 35 | M < 35 | M >= 35 </p>

<div class="row">'''

## emdFormatter (emdRegister)
## Dado um objeto EMD, prepara a string correspondente à sua apresentação no ficheiro .html preparado
# @emdRegister = objeto EMD
def emdFormatter(emdRegister):

  emdDivFormat = '''

        <p><b>Nome:</b> {} {} </p>
        <p><b>Idade:</b> {} <b>Genero:</b>{}</p>
        <div class="line"></div>'''.format(emdRegister.name, 
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

def ageGenderIndicatorsHtml(filename, ageGenderRegisters):

  global htmlStart
  global htmlEnd
 
  preparedInfo = ageGenderRegisters
  listAge = list(preparedInfo.keys())

  fileHandler = open(filename, "wt", encoding="utf-8")

  for key in listAge:

    if key == 'femLT35':
      htmlStart = htmlStart + '''

  <div class = "column">

      <h2> Feminino </h2>
      
      <button type="testing" class="collapsible"> Feminino < 35 </button>
      
      <div class="content">    '''

    if key == 'femGET35':
      htmlStart = htmlStart +'''

      <button type="testing" class="collapsible"> Feminino >= 35 </button>
      
      <div class="content">'''

    if key == 'mascLT35':
      htmlStart = htmlStart + '''
  </div>
  <div class = "column">

      <h2> Masculino </h2>
     
      <button type="testing" class="collapsible"> Masculino < 35 </button>
        
      <div class="content">'''

    elif key == 'mascGET35':
      htmlStart = htmlStart +'''
  
      <button type="testing" class="collapsible"> Masculino >= 35 </button>
      
      <div class="content">'''

    for emd in preparedInfo[key]:

      emdFormatter(emd)
    
    htmlStart = htmlStart +'''
      </div>
      '''
  htmlStart = htmlStart +'''
    </div>'''


  fileHandler.write(htmlStart + htmlEnd)
  fileHandler.close()

