
htmlStart = '''<!DOCTYPE html>
<html>
<head>
<meta name="index.html" content="width=device-width, initial-scale=1">
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
  content: '\02795'; /* Unicode character for "plus" sign (+) */
  font-size: 13px;
  color: white;
  float: right;
  margin-left: 5px;
}

.active:after {
  content: "\2796"; /* Unicode character for "minus" sign (-) */
}

.content {
  padding: 0 18px;
  display: none;
  overflow: hidden;
  background-color: #f1f1f1;
}

</style>
</head>
<body>

<h1>Index</h1>
<h2>Exame Médicos Desportivos</h2>
<button type="alinhaA" class="collapsible">a) Datas extremas dos registos</button>
<div class="content">
  <a href="datesIndicators.html">RESPOSTA</a>
</div>

<button type="alinhaB" class="collapsible">b) Distribuição por género em cada ano e no total</button>
<div class="content">

  <a href="genderIndicators.html">RESPOSTA</a>
  

</div>

<button type="alinhaC" class="collapsible">c) Distribuição por modalidade em cada ano e no total</button>
<div class="content">
  <a href=" .... .html">RESPOSTA</a>
</div>

<button type="alinhaD" class="collapsible">d) Distribuição por idade e género</button>
<div class="content">
  <a href="ageGenderIndicators.html">RESPOSTA</a>
</div>

<button type="alinhaE" class="collapsible">e) Distribuição por morada</button>
<div class="content">
  <a href="addressIndicators.html">RESPOSTA</a>
</div>

<button type="alinhaF" class="collapsible">f) Distribuição por estatuto de federado em cada ano</button>
<div class="content">
  <a href=" ..... .html">RESPOSTA</a>
</div>

<button type="alinhaG" class="collapsible">g) Percentagem de aptos e não aptos por ano</button>
<div class="content">
  <a href=" ..... .html">RESPOSTA</a>
</div>

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
htmlEnd=''' '''
htmlFILE = "index.html"

def indexHTML():
    fileHandler = open(htmlFILE, "wt", encoding="utf-8")
    fileHandler.write(htmlStart + htmlEnd)
    fileHandler.close()
    