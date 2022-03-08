print("Podaj działanie, posługując się odpowiednią liczbą: ")
print("1. Dodawanie")
print("2. Odejmowanie")
print("3. Mnozenie")
print("4. Dzielenie")

dzialanie = input()

if dzialanie == "1":
    liczba1 = input("Podaj pierwsza liczbe : ")
    liczba2 = input("Podaj druga liczbe : ")
    print("Dodaje : " + liczba1 + " + " + liczba2)
    print("Wynik to : " + str(int(liczba1) + int(liczba2)))

if dzialanie == "2":
    liczba1 = input("Podaj pierwsza liczbe : ")
    liczba2 = input("Podaj druga liczbe : ")
    print("Odejmuje : " + liczba1 + " - " + liczba2)
    print("Wynik to : " + str(int(liczba1) - int(liczba2)))

if dzialanie == "3":
    liczba1 = input("Podaj pierwsza liczbe : ")
    liczba2 = input("Podaj druga liczbe : ")
    print("Mnoze : " + liczba1 + " * " + liczba2)
    print("Wynik to : " + str(int(liczba1) * int(liczba2)))

if dzialanie == "4":
    liczba1 = input("Podaj pierwsza liczbe : ")
    liczba2 = input("Podaj druga liczbe : ")
    print("Dziele : " + liczba1 + " / " + liczba2)
    print("Wynik to : " + str(int(liczba1) / int(liczba2)))