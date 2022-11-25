#x     cilj
pozicija_automobila= 0
pozcija_cilja=10

pozicija_automobila +=2
print(pozicija_automobila==pozcija_cilja)

pozicija_automobila +=2
print(pozicija_automobila==pozcija_cilja)

pozicija_automobila +=2
print(pozicija_automobila==pozcija_cilja)

pozicija_automobila +=2
print(pozicija_automobila==pozcija_cilja)

pozicija_automobila +=2
print(pozicija_automobila==pozcija_cilja)

pozicija_automobila +=2
print(pozicija_automobila==pozcija_cilja)

for sledeci in ["marko","milos","marija","ana","sofija"]:
    print("Hello",sledeci)

print("Prva sledeca linija...")

for broj in [1,2,3,4,5]:
    print("Ovo je broj:",broj)


for broj in range(5,10,2):
    print("Stampanje brojeva:",broj)

    for broj in [100,0,-1]:
        print("Prikaz:",broj)


pozicija_automobila= 0
pozicija_cilja=10
for kretanje in range(5):
    pozicija_automobila+=2
    print(pozicija_automobila==pozcija_cilja)

pozicija_automobila= 0
pozicija_cilja=10
for trenutna_pozicija in range(pozicija_cilja+1):
    pozicija_automobila==pozicija_cilja
    print(pozicija_automobila==pozicija_cilja)

pocetna_godina=2010
zavrsena_godina=2021
for godina in range(pocetna_godina,zavrsena_godina):
    print(godina)

for _ in range(100):
    print("*",end="")

print()


print("1\t2\t3\t")
print("****************")

for brojac in range(1,6):
    print(brojac*1,end="\t")
    print(brojac*2,end="\t")
    print(brojac*3)


for x in range(5):
    for y in range(3):
        print("Ovo je x:",x, "Ovo je y:",y)


for x in range (6):
    for y in range (6):
        if x==y:
            print("*",end=" ")
        else:
            print("#",end="") 
    print()
baterija=90
while baterija>0:
    print("Mozes koristiti telefon")
    baterija-= 10
print("Prazna baterija")











