programowanie=['Python', 'PHP', 'C#', 'JS', 'Java']
print(programowanie)
print(type(programowanie))

first=programowanie[0]
print(first)

threeElements = programowanie[0:3]
print(threeElements)

lastElement = programowanie[-1]
print(lastElement)

#Dodawanie nowego elementu na koniec listy
programowanie.append('R')
programowanie.append('Python')
print(programowanie)

#zliczanie
count=programowanie.count('Python')
print(countElements)

#ilosc elementow w liscie
countElementsOfList = len(programowanie)
print(countElementsOfList)

#polaczenie list
anotherList=['C','C++']
programowanie.extend(anotherList)
print(programowanie)
print(anotherList)

#czyszczenie list
new=programowanie
print('Lista nowa: ',end="")
print(new)
new.clear()
print('Lista nowa: ',end="")
print(new)

print('List programowanie:',end="")
print(programowanie)
