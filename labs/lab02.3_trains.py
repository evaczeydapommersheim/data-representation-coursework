# 2023-24 ATU Data Prepresentation Topic02
# This progam prints the data for all trains in Ireland to the console.
# Irish Rail API is to be retrieved from url: http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML

import requests
import csv
from xml.dom.minidom import parseString

retrieveTags=['TrainStatus',
            'TrainLatitude',
            'TrainLongitude',
            'TrainCode',
            'TrainDate',
            'PublicMessage',
            'Direction'
            ]

url = "http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"
page = requests.get(url)
doc = parseString(page.content)
# print (doc.toprettyxml()) #this is to output to the console to check that it works
# if wanting to store the xml in a file, that can be achieved by the below code 
# (this may be commented out)
# with open("trainxml.xml","w") as xmlfp:
    #doc.writexml(xmlfp)
#objTrainPositionsNodes = doc.getElementsByTagName('objTrainPositions')
#for objTrainPositionsNode in objTrainPositionsNodes:
   #traincodenode = objTrainPositionsNode.getElementsByTagName("TrainCode").item(0)
    #traincode = traincodenode.firstChild.nodeValue.strip()
    #print(traincode)

#for objTrainPositionsNode in objTrainPositionsNodes:
    #trainlatitudenode = objTrainPositionsNode.getElementsByTagName("TrainLatitude").item(0)
    #trainlatitude = trainlatitudenode.firstChild.nodeValue.strip()
    #print(trainlatitude)

with open('week02_train.csv', mode = 'w', newline='') as train_file:
    train_writer = csv.writer(train_file, delimiter = '\t', quotechar = '"', quoting=csv.QUOTE_MINIMAL)
    
    objTrainPositionsNodes = doc.getElementsByTagName('objTrainPositions')
    for objTrainPositionsNode in objTrainPositionsNodes:
        #traincodenode = objTrainPositionsNode.getElementsByTagName("TrainCode").item(0)
        #traincode = traincodenode.firstChild.nodeValue.strip()
        dataList = []
        
        for retrieveTag in retrieveTags:
            if
            datanode = objTrainPositionsNode.getElementsByTagName(retrieveTag).item(0)    
            dataList.append(datanode.firstChild.nodeValue.strip())
        train_writer.writerow(dataList)



