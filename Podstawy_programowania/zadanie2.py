'''
Utwórz słownik, który zawiera dane podane przez użytkownika z klawiatury:
imie, nazwisko, wiek. Przypisz do słownika dane pobrane od dwóch użytkowników.
Wyświetl dane w formacie:
user1: (imie) (nazwisko) wiek: (wiek)
user2: (imie) (nazwisko) wiek: (wiek)
Średni wiek użytkowników wynosi: (średnia) lat
'''
print("Podaj dane pierwszego usera")
name1 = input("Podaj imie: ")
surname1 = input("Podaj nazwisko: ")
age1 = eval(input("Podaj wiek: "))

print("Podaj dane drugiego usera")
name2 = input("Podaj imie: ")
surname2 = input("Podaj nazwisko: ")
age2 = eval(input("Podaj wiek: "))

user1 = {
    'imie': name1,
    'nazwisko': surname1,
    'wiek': age1
}

user2 = {
    'imie': name2,
    'nazwisko': surname2,
    'wiek': age2
}

print("user1: ",user1['imie']," ",user1['nazwisko'], " wiek: ",user1['wiek'])
print("user2: ",user2['imie']," ",user2['nazwisko'], " wiek: ",user2['wiek'])

srednia = (user1['wiek']+user2['wiek'])/2

print(f"Średni wiek użytkowników wynosi: {srednia} lat")