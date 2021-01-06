import numpy as np
import matplotlib.pyplot as plt
import re
#średnie długości tras z kraju

import pandas as pd
import csv
from pandas import DataFrame
from sklearn import tree
from matplotlib import pyplot
from pandas.plotting import scatter_matrix
#Wczytanie danych z pliku

skale = (50,10,40,50)

urls = ["https://www.skiresort.info/best-ski-resorts/poland/",  "https://www.skiresort.info/best-ski-resorts/germany/", "https://www.skiresort.info/best-ski-resorts/austria/" ,"https://www.skiresort.info/best-ski-resorts/italy/"]
countries= ['Polska','Włochy','Austria','Czechy']

plt.bar(countries, skale)
plt.legend()
plt.xlabel('Countries')
plt.ylabel('KM')
title = plt.title('Average route lengths')
plt.show()
