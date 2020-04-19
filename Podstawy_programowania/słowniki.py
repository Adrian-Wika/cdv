pracownik = {'imie':'Bob', 'nazwisko':'Marley','miasto':'Sosnowiec','wiek':'21','imionaDzieci':['Seba','Jessica'],'imionaRodzicow':['Janusz','Grażyna']}
print(pracownik)
print(pracownik['imionaRodzicow'])
print(pracownik['imionaRodzicow'][0])

pracownik['wzrost']=175
pracownik['waga']=80
print(pracownik)

#####################################################

pracownik1 = {
    'name':'Anna',
    'surname':'Kowalska',
    'city':'Poznań',
    'age':24
}

print()
print(pracownik1)

key='age'
if key in pracownik1:
    del pracownik1[key]
    print(f'Klucz{key} został usuniety')
else:
    print(f'Klucz {key} nie został usuniety')

print(pracownik1)
print(pracownik1.keys())
print(pracownik1.values())

print(list(pracownik1.values()))
print(pracownik1.items())

for value in pracownik1.values():
    print(value, end=" ")
print()

for key, value in pracownik1.items()
    print(f'{key}:{value}')

