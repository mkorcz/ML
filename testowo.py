import pandas as pd
import requests
urls = ["https://www.skiresort.info/best-ski-resorts/poland/", "https://www.skiresort.info/best-ski-resorts/germany/", "https://www.skiresort.info/best-ski-resorts/austria/" ,"https://www.skiresort.info/best-ski-resorts/italy/"]
lenghtURLS = len(urls)
y=0
countryTable=[]

data='pupka-dupka.fitek'
dict = ['.',' ','-']
for x in range(len(dict)):
   final = data.replace(dict[x], ',')
print(final)











for x in range(lenghtURLS):
    first = urls[x].split('https://www.skiresort.info/best-ski-resorts/')
    select = str(first[1])
    final = select.replace('/', '')
    if(len(countryTable) == 0):
        countryTable.append(final)
    else:
        if(final != countryTable[y]):
            countryTable.append(final)
            y = y + 1


print(countryTable)

#Stworzenie listy krajów na podstawie wprowadzonych linków)

