text="Anna, paweł, TomEK"

'''
komentarz
blokowy
'''

tab = text.split(", ")
print(text)
print(tab)
print(type(tab))
name1=tab[0]
print("Twoje imie: " + name1)

nameUpper = name1.upper()
print(nameUpper)

nameLower = name1.lower()
print(nameLower)

#sprawdzenie zawartości
surname = input()
content = surname.isalpha()
print(content)
print(type(content))

name="Katarzyna"
print("\nDane uzytkownika\nMasz na imie: ", name)

text1="Jan\n"
text2="Nowak"
print(text1 + text2)

text1=text1.rstrip()
print(text1 + text2)

#wyświetlenie łańcuchów znaków

#wszystkie wersje pythona
text = "%s, Java i %s" % ("PHP", "Python")
print(text)

#nowsze wersje python > 2.6
text = "{1}, Java i {0}" .format("PHP", "Python")
print(text)

#help(text.replace)

new = text.replace("PHP", "C#")
print(new)

#wypisywanie danych
year=2020
month="april"
day=19

print("Data: ", end="")
print(day, month, year)
print("Data: ", day,month,year)