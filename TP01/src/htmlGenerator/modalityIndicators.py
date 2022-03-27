"""modalityIndicators.py: Geração de ficheiro html para indicação dos indicadores das modalidades"""

from Queries import modalityStudy

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

<h1>Modalidades</h1>
<p>As modalidades encontram-se organizadas alfabeticamente</p>
<div class="address">'''


def emdFormatter(emdRegister):
  """Formata um registo para a sua devida representação em html
    
      Arguments:
      ---------
        emdRegister (emd) : registo de exame médico
  """

  emdDivFormat = '''
      <p><b>Nome:</b> {} {} </p>
      <p><b>Modalidade:</b> {} </p>'''.format( emdRegister.name, 
                emdRegister.surname, 
                emdRegister.modality)

  global htmlStart
  htmlStart = htmlStart + emdDivFormat

## HTML final format string
htmlEnd = '''
  </div>
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


def modalityIndicatorsHtml(filename, modalities):
  
  global htmlStart
  global htmlEnd
  preparedInfo = modalityStudy.prepareModalitiesIndic(modalities)
  listAddress = list(preparedInfo.keys())
  listAddress.sort()
  alphabet = []
  lengthLista = len(listAddress)

  fileHandler = open(filename, "wt", encoding="utf-8")

  for addressIndex in range (0, lengthLista):
    letter = (listAddress[addressIndex])[0]
    if letter not in alphabet:
        alphabet.append(letter)
        htmlStart = htmlStart +'''
  <div class="data">
    <h2> {} </h2>'''.format(letter)

    address = listAddress[addressIndex]
    
    htmlStart = htmlStart +  '''
    <button type="{}" class="collapsible"> {} </button>
      <div class="content">'''.format(address, address)

    for emd in preparedInfo[(listAddress[addressIndex])]:
      emdFormatter(emd)
        
      htmlStart = htmlStart + '''
      <div class="line"></div>'''
  
    htmlStart = htmlStart + '''
    </div>    '''

    
    if  addressIndex < (lengthLista-1) and letter != (listAddress[addressIndex+1])[0]:
      htmlStart = htmlStart +'''
  </div>
  ''' 

  fileHandler.write(htmlStart + htmlEnd)
  fileHandler.close()
