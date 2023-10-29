# Assignment 03 for Data representation module
# Write a program that retrieves the dataset for the "exchequer account (historical series)" from the CSO, 
# and stores it into a file called "cso.json".

# By: Eva Czeyda-Pommersheim

import requests
import json

# getting the url from https://data.gov.ie/dataset/fiq02-exchequer-account-historical-series
# dataset is with FIQ02 ID which will be entered when testing the function.
beginningUrl = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/"
endUrl = "/JSON-stat/2.0/en"

def getDataset(dataset):
    url = beginningUrl + dataset + endUrl
    response = requests.get(url)
    return response.json()

def storeFile(dataset):
    with open("cso.json", "wt") as fp:
        print(json.dumps(getDataset(dataset)), file=fp)



if __name__ == "__main__":
    # print(getDataset("FIQ02"))
    print(storeFile("FIQ02"))
