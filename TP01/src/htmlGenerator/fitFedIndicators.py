from cgitb import html
from EMDsParser import loadDataStructure as emdLDS


def federatedIndicatorsHTML(dataset):
  htmlStart = '''<!DOCTYPE html>
  <html>
  <head>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <style>

  html {
    box-sizing: border-box;
    background-color: #FFEBEB;
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

  .center {
  display: block;
  margin-left: auto;
  margin-right: auto;
  width: 75%;
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

  h1{
      text-align: center;
      color: #1C3AAE
  }
  }

  </style>
  </head>
  <body>

  <h1>Federated Indicators <sub style="font-size: 20px">by name, alphabetically</sub></h1>
  '''

  if len(dataset) <= 3:
    htmlGraph = '''<img src="fed_Mult_Pie.png" alt="Graph" class="center">'''
  else:
    htmlGraph = '''<img src="fed_Mult_Pie.png" alt="Graph" class="center">'''




  htmlEnd = '''
  </body>
  </html>'''


  ## Name of the file to be written
  htmlFILE = "FederatedIndicators.html"

  fileHandler = open(htmlFILE, "wt", encoding="utf-8")

  fileHandler.write(htmlStart + htmlGraph + htmlEnd)

  fileHandler.close()