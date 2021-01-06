import pandas as pd
#import unidecode
import re
import requests
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
#import soup as soup
from bs4 import BeautifulSoup

import ssl
import csv

urls = ["https://www.skiresort.info/best-ski-resorts/poland/",  "https://www.skiresort.info/best-ski-resorts/germany/", "https://www.skiresort.info/best-ski-resorts/austria/" ,"https://www.skiresort.info/best-ski-resorts/italy/"]

class makeDfOfAreas:
    def __init__(self, urls):
        self.urls = urls

    def __makeDFWithAreas(self, url):
        getpage = requests.get(url)
        getpage_soup = BeautifulSoup(getpage.text, 'html.parser')
        resort_urls = getpage_soup.findAll('a', {'class':'h3'})
        #print(type(resort_urls))
        resort_urls = [i.text for i in resort_urls]
        df = pd.Series(resort_urls)
        df.to_frame()
        #print(df.at[49])
        #df.columns = ['area']
        df = df.drop(df[df.index > 49].index)
        df = df.str.lower()
        df = df.str.replace('\d+.\s', '')
        df = df.str.replace('\s$', '')
        df = df.str.replace('  ', '')
        df = df.str.replace('/', '')
        df = df.str.replace(' ', '-')
        df = df.str.replace('–-', '')
        df = df.str.replace('(', '')
        df = df.str.replace(')', '')
        df = df.str.replace('.', '')
        df = df.str.replace('’', '')
        df = df.str.replace('ö', 'o')
        df = df.str.replace('ä', 'a')
        df = df.str.replace('ü', 'u')
        df = df.str.replace('ä', 'a')
        df = df.str.replace('ß', 's')
        df = df.str.replace('ą', 'a')
        df = df.str.replace('ę', 'e')
        df = df.str.replace('ć', 'c')
        df = df.str.replace('ł', 'l')
        df = df.str.replace('ń', 'n')
        df = df.str.replace('ó', 'o')
        df = df.str.replace('ś', 's')
        df = df.str.replace('ż', 'z')
        df = df.str.replace('ź', 'z')
        df = df.str.replace('é', 'e')
        df = df.str.replace('è', 'e')
        df = df.str.replace('à', 'a')
        df = df.str.replace('ù', 'u')
        df = df.str.replace('-&-', '-')
        df = df.str.replace(r'(\.*)', '')
        return df

    def appendingAreasNames(self):
        df = pd.DataFrame()
        for site in urls:
            df = pd.concat([df , self.__makeDFWithAreas(site)])
        df = df.rename(columns={0: 'areas' })
        return df


dfOfAreas = makeDfOfAreas(urls)
#print(dfOfAreas)




class makeUrls:
    def __init__(self, df):
        self.df = df

    def makeAreasSizeList(self,df):
        newList = df['areas'].values.tolist()
        areasSizeList = []
        for x in range(0, len(newList)):
            newList[x] = newList[x].replace('\u200b', '')
            areasSizeList.append('https://www.skiresort.info/ski-resort/' + newList[x] + '/test-result/size/')
        return areasSizeList

    def makeAreasLiftList(self,df):
        newList = df['areas'].values.tolist()
        areasLiftList = []
        for x in range(0, len(newList)):
            newList[x] = newList[x].replace('\u200b', '')
            areasLiftList.append('https://www.skiresort.info/ski-resort/' + newList[x] + '/test-result/lifts-cable-cars/')
        return areasLiftList


lists = makeUrls(dfOfAreas.appendingAreasNames())
areasSizeList = lists.makeAreasSizeList(dfOfAreas.appendingAreasNames())
areasLiftList = lists.makeAreasLiftList(dfOfAreas.appendingAreasNames())


#print(areasSizeList)




def validateLinks(list):

    validatedLinksTable = []
    for x in range(0, len(list)):
        url = requests.get(list[x])
        soup = BeautifulSoup(url.text, 'html.parser')
        lista = soup.findAll('div', {'class': 'description'})
        lista = [d.text for d in lista]
        for y in range(0, len(lista)):
            if len(lista) > 3:
                continue
        if len(lista) < 4:
            validatedLinksTable.append(x)
    return validatedLinksTable


class makeData:
    def __init__(self, list, validateList):
        self.list =list
        self.validateList = validateList


    def downloadData(self, list, validateList):
        global data
        data = []
        global listOfAreasTemp
        listOfAreasTemp = []

        for x in range(0, len(validateList)):
            url = requests.get(list[validateList[x]])
            soup = BeautifulSoup(url.text, 'html.parser')
            lista = soup.findAll('div', {'class': 'description'})
            lista = [d.text for d in lista]
            for y in range(0, len(lista)):
                if len(lista)>3 :
                    continue
                    #brokenlinks=list[x]
                else:
                    lista[y] = lista[y].split()[0]
            if len(lista)<4:
                data.append(lista)
        #print(data)
        #print(lista)
        #print(brokenlinks)
        return data

    def downloadData1(self, list, validateList):
        global data
        data = []
        listOfLiftType = ['Aerial', 'Circulating', 'Chairlift', 'T-bar', 'Rope', 'Sunkid']
        for x in range(0, len(validateList)):
            url = requests.get(list[validateList[x]])
            soup = BeautifulSoup(url.text, 'html.parser')
            lista = soup.findAll('div', {'class': 'lift-head'})
            lista = [i.text for i in lista]
            listaTemp = [0, 0, 0, 0, 0, 0]
            for y in range(0, len(lista)):
                if len(lista)>7 :
                    continue
                    #brokenlinks=list[x]
                else:
                    for z in range(0, len(lista)):
                        for i in range(0, len(listOfLiftType)):
                            if lista[z].split()[1] == listOfLiftType[i]:
                                listaTemp[i] = lista[z].split()[0]
            if len(lista)<7 and len(lista)!= 0:
                data.append(listaTemp)
        #print(data)
        #print(lista)
        #print(brokenlinks)
        return data



listOfValidateNumbers = validateLinks(areasSizeList)

download = makeData(areasSizeList, listOfValidateNumbers)

print(download.downloadData(areasSizeList, listOfValidateNumbers))
print(download.downloadData1(areasLiftList, listOfValidateNumbers))

dataOfAreasSize = download.downloadData(areasSizeList, listOfValidateNumbers)
columsOfAreasSize =['Routes total', 'Elevation difference', 'Lifts total']
dataOfAresLifts = download.downloadData1(areasLiftList, listOfValidateNumbers)
columsOAreasLift = ['Aerial', 'Circulating', 'Chairlift', 'T-bar', 'Rope', 'Sunkid']

print(dataOfAreasSize)
print(columsOfAreasSize)
def makeDF(data, columns):
    return pd.DataFrame(np.array(data), columns = columns)


#print(makeDF(dataOfAreasSize,columsOfAreasSize))
#print(makeDF(dataOfAresLifts, columsOAreasLift))


def export_csv(tab1, tab2):
    tab1.join(tab2)
    return tab1.to_csv ('exportDataframe.csv', index = None, header=True)



export_csv(makeDF(dataOfAreasSize,columsOfAreasSize), makeDF(dataOfAresLifts, columsOAreasLift))
#print(fTable)