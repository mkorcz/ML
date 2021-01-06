import re

class checkData: #sprawdzanie poprawności wprowadzonych danych,normalizacjam konwersja danych
    def __init__(self, data):
        self.data = data

    def getData(self): #sprawdzanie poprawności danych ( można użyć white-space , - .
        regex = "\d{2,5}[\s,-\.]\d{2,5}[\s,-\.]\d{2,5}[\s,-\.]\d{2,5}[\s,-\.]\d{2,5}[\s,-\.]\d{2,5}"
        if re.search(regex, self.data):
            match = re.search(regex, self.data)
            return self.check() #jeśli nie jest w takiej samej formie co lista to check()
        else:
            return ("Podałeś błędne dane")

    def check(self, ): #konwersja
        regex = "\d{2,5},\d{2,5},\d{2,5},\d{2,5},\d{2,5},\d{2,5}"
        if re.search(regex, self.data):
            match = re.search(regex, self.data)
            return self.makeTable()
        else:
            print(("Konwersja danych... \n"))
            dict = ['.',' ','-']
            for x in range(len(dict)):
               final = self.data.replace(dict[x], ',')
            return (self.makeTable(final))

    def makeTable(self, final): #tworzy tabele
        setting = final.split(' ')
        table=[]
        for x in setting:
            table.append(x)
            #Zamiana na inta
        for i in range(0, len(table)):
            table[i] = int(table[i])
        if(table[2] == (table[3]+table[4]+table[5])):
            return table
        else:
            return ("Podałeś błędne dane")

class InsertDataToCheck:
    def __init__(self, count):
        self.count = int(count)

    def doit(self):
        yourData = []
        count = self.count
        print(count)
        if (count<2):
            yourData.append(checkData(input("Enter the slope parameters  \n 'Routes total', 'Elevation difference', 'Lifts total', ['Aerial'], ['Circulating'], ['Chairlift']: \n")))
            print('iam here')
            return (yourData)
        elif(count>0):
            for x in range(count):
                yourData.append(checkData(input(
                    "Enter the slope parameters  \n 'Routes total', 'Elevation difference', 'Lifts total', ['Aerial'], ['Circulating'], ['Chairlift']: \n")))
                print('iam here now')
            return(yourData)

ilosc = InsertDataToCheck(5)
finish = ilosc.doit()
#dane = checkData(input(
  #  "Enter the slope parameters  \n 'Routes total', 'Elevation difference', 'Lifts total', ['Aerial'], ['Circulating'], ['Chairlift']: \n"))

#w= (dane.getData())
#print(w)