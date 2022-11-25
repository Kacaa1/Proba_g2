import random

# import funkcija se vrsi na pocetku fajla

a = 10
b = 5
rezultat_sabiranja = a + b
print(rezultat_sabiranja)
print("Oduzimanje", a - b)
print("Mnozenje", a * b)
print("Deljenje", int (a / b))

print("Celobrojno deljenje:", a // b)
print(10 // 3)
print(10 / 3)

print("Stepenovanje:", a**3) # a*a*a (na treci)

print(10 % 3) # ostatak prideljenju

print(5 % 2) # 2*2=4, ostatak je 1

print(8 % 2)

# Unarni operator
print(-a) # prebacuje operater a u negativan broj, u ovom slucaju -10

# Slozeni operater dodele - Precice

godine = 25
# godine + 1

print(godine)

godine = godine + 1

godine += 1

print(godine)

godine -= 5

print(godine)

godine *= 2

print(godine)

godine /= 2

print(godine)

godine //= 2
print(int(godine))



# operatori moraju biti spojeni i redosled se mora pratiti 

# broj1 = 15
# broj2 = 20

# print("Zbir:", broj1+broj2)




# broj1 = input("Unesite prvi broj: ")
# print(broj1)

# broj2 = input("Unesite drugi broj: ")
# print(broj2)

# print("Rezultat je: ", broj1 + broj2)




# poluprecnik = float(input("Unesite poluprecnik: "))
# pi = 3.14

# povrsina = poluprecnik ** 2 * pi

# print("Povrsina kruga je:", povrsina)



# unos = input("Unesi nesto...")
# print(unos.isnumeric()) # proveravamo da li je nesto broj ili slovo



# Operatori poredjenja:

# <(manje od) >(vece od)  >=(vece ili jednako) <=(manje ili jednako) ==(jednako) !=(razlicito) / iskaz je: True ili False

# stara_kilaza = 80
# nova_kilaza = 99
# print(stara_kilaza > nova_kilaza)
# print(stara_kilaza < nova_kilaza)
# print(nova_kilaza != 100)
# print(stara_kilaza >= 80)
# print(stara_kilaza <= 80)


# username = "test"
# password = "abc"

# print(username == "test")
# print(password == "abc123")


# godine = 20
# print(godine >= 16)

# broj = int(input("Unsite broj: "))
# # % paran broj podeljen sa 2 ima ostatak 0
# provera = broj % 2
# print("Paran broj?", provera == 0)


# korisnik = int(input("Unesite broj: "))
# racunar = random.randint(1, 10)

# print("Korisnik: ", korisnik)
# print("Racunar: ", racunar)
# print("Pogodak: ", korisnik == racunar)


# automobil = 0
# cilj = 50
# print(automobil >= cilj)

# automobil += 10
# print(automobil >= cilj)

# automobil += 25
# print(automobil >= cilj)

# automobil += 20
# print(automobil >= cilj)




# Logicki operatori: or (levo ili desno mora biti True), and (leva i desna strana moraju biti True), not (...)

provera_imena = True # ime == sacuvano_ime
provera_sifre = False # sifra == sacuvana_sifra
print(provera_imena and provera_sifre)

'''
and
true true > true
false true > false
true false > false
false false > false

or
true true > true
false true > true
true false > true
false false > false

not
pretvara bool vrednost u suprotnu
'''

lepo_vreme = True
print(not lepo_vreme)


# Identitorski operator is / proverava da li se oba operanda nalaze na istoj memorijskoj adresi
# Membership operator in / proverava da li se neki podatak nalazi u nekoj kolekciji podataka

# Operatori nad bitovima
# >> pomera desno
# << pomera levo
# & ili
# | i
# ~ negacija
# ^ ili, (ksor) samo ako je jedan operand True

kurs = input("Unesite kurs: ")
generacija = int(input("Generacija: "))

odobreno = kurs == "python" and generacija == 2022

print(odobreno)