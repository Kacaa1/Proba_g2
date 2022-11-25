import random


# x = 10

# if x > 0:
#     print("broj x je pozitivan")

# print("Izvrsava se u svakom slucaju")

# vozilo_u_pokretu = True
# brzina = 40

# if vozilo_u_pokretu == True:
#     print("Vozilo se krece")

# if True:
    # linija koda koja se izvrsava
# if (je boolean operacija, sto znaci da nam == True nije potrebno,
# vec se pitanje moze postaviti kao - if vozilo_u_pokretu: i ako je vozilo_u_pokretu = True, izvrsice se seldeca linija koda)

# if vozilo_u_pokretu:
#     print("Vozilo se krece...")
#     print("Proverite i brzinu...")
#     if brzina > 50:
#         print("Prekoracena brizna")
#     print("Ovo izvrsavam kolika god da je brzina")
#     if brzina <= 50:
#         print("Brzina je OK.")

# if vozilo_u_pokretu == False:
#     print("Vozilo se ne krece...")


# 1 - prikaz ; 2 - kupovina ; 3 - izlaz
# proizvod = "Duks"
# cena = 3000

# komanda = int(input("Unesite komandu: "))


# if komanda == 1:
#     print("Prikazi proizvode")
#     print("Proizvod:", proizvod, "Cena:", cena)
# if komanda == 2:
#     print("Kupovina")
#     stanje = int(input("Unesite stanje na racunu: "))
#     if stanje >= cena:
#         print("Uspesna kupovina!")
#     if stanje <= cena:
#         print("Neuspesna kupovina...")
# if komanda == 3:
#     print("Izlaz")

# broj = 5

# if broj > 0:
#     print("Broj je veci od 0.")
#     broj = -broj
# if broj <= 0:
#     print("Broj je nula ili manji od nule.")
# if broj == 0:
#     pass

# if broj > 0:
#     print("Broj je veci od 0.")
# else:
#     print("Broj je 0 ili manji od 0.") #else nema uslov i ne moze stajati u kodu bez uslova if


# marija = False
# ksenija = True
# katarina = False

# devojka_na_dejtu = ""

# if marija:
#     devojka_na_dejtu = "marija"
# elif katarina:
#     devojka_na_dejtu = "katarina"
# elif ksenija:
#     devojka_na_dejtu = "ksenija"
# else:
#     devojka_na_dejtu = "sofija"

# print("Izlazi sa mnom:", devojka_na_dejtu)

# automobil_polovan = False
# godiste = 2022
# boja = "crna"

# if (automobil_polovan == True or godiste > 2017) and boja == "crna":
#     print("Kupujem")


# if not automobil_polovan:
#     print("Automobil je nov.")

# prisutan = False #nije na casu
# smer = "puython"

# if prisutan and smer == "python":
#     print("Polaznik je na casu")

# if prisutan:
#     print("Na casu je")
# if not prisutan: #ako nas interesuje da li je false
#     print("Nije na casu")


# trenutni_rezultat = random.randint (1, 100)
# novi_rezultat = int(input("Unesite novi broj (od 1 do 100): "))

# if novi_rezultat >100 or novi_rezultat < 1:
#     print("Proverite broj, dozvoljeno od 1 do 100")
# else:
#     print("Trenutni broj:", trenutni_rezultat, "Novi broj:", novi_rezultat)
#     if trenutni_rezultat < novi_rezultat:
#         print("Pobedili ste!")
#     elif trenutni_rezultat == novi_rezultat:
#         print("Identicne vrednosti!!!")
#     else:
#         print("Izgubili ste")

# if novi_rezultat >100 or novi_rezultat < 1:
#     print("Proverite broj, dozvoljeno od 1 do 100")
# elif trenutni_rezultat < novi_rezultat:
#     print("Pobedili ste!")
# elif trenutni_rezultat == novi_rezultat:
#     print("Identicne vrednosti!!!")
# else:
#     print("Izgubili ste")

# pol = input("Unesite pol: ")
# poruka = ""

# #duzi zapis
# if pol == "m":
#     poruka = "Hey mister!"
# else:
#     poruka = " Hey miss!"

# #kraci zapis
# poruka = "Hey mister!" if pol == "m" else "Hey miss!"
# print(poruka)


popularan_proizvod = ""
jesen = False
# # ako je jesen, tada je ajvar, a ako nije onda sladoled

popularan_proizvod = print("ajvar" if jesen else "sladoled")

