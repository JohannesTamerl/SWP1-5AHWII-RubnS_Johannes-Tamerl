import random
import matplotlib.pyplot as plt

list = []
emptylist = []


def getlist(count):
    for x in range(count):
        list.append(x)
        emptylist.append(0)


def getnumbers(list):
    newlist = list.copy()
    for x in range(0, 6):
        randomnumber = random.randint(0, len(newlist) - 1 - x)
        newlist[randomnumber], newlist[len(newlist) - x - 1] = newlist[len(newlist) - x - 1], newlist[randomnumber]
    return newlist[-6:]


def countup(list, dictionary):
    for x in range(len(list)):
        dictionary[list[x]] = dictionary[list[x]]+1


#Listen erstellen
getlist(45)


#Dictionary zippen
mydictionary = dict(zip(list, emptylist))
print(mydictionary.__str__())

#Zufallszahlen generieren speichern und ausgeben


randomnumbers = []
for x in range(1000):
    randomnumbers = getnumbers(list)
    countup(randomnumbers, mydictionary)
    print(randomnumbers)

print(mydictionary.__str__())

names = mydictionary.keys()
values = mydictionary.values()

plt.bar(range(len(mydictionary)), values, tick_label=names)
plt.show()