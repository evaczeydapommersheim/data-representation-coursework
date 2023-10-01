# This progam prints the data for all trains in Ireland to the console.
# Irish Rail API is to be retrieved from url: http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML

import requests
import csv
from xml.dom.minidom import parseString

url = "http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"
page = requests.get(url)
doc = parseString(page.content)
# print (doc.toprettyxml())