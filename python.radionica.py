import random
import math

# 1. Lista proizvoda
proizvodi = [
    "Laptop",
    "Mis",
    "Tastatura",
    "Monitor",
    "Slusalice",
    "Web kamera",
    "USB flash",
    "Stampac"
]

# 2. Recnik proizvoda i cena
cene = {
    "Laptop": 950.99,
    "Mis": 19.99,
    "Tastatura": 49.99,
    "Monitor": 220.50,
    "Slusalice": 89.90,
    "Web kamera": 39.99,
    "USB flash": 14.99,
    "Stampac": 159.99
}

# 3. Prikaz svih proizvoda i cena
print("Lista proizvoda i njihove cene:")
for proizvod in proizvodi:
    print(f"{proizvod} - {cene[proizvod]:.2f} €")

# 4. Unos budzeta i ispis proizvoda koje korisnik moze da priusti
budzet = float(input("\nUnesite svoj budzet u evrima: "))

print("\nProizvodi koje mozete da priustite:")
ima_proizvoda = False
for proizvod in proizvodi:
    if cene[proizvod] <= budzet:
        print(f"{proizvod} - {cene[proizvod]:.2f} €")
        ima_proizvoda = True

if not ima_proizvoda:
    print("Nazalost, nema proizvoda u okviru vaseg budzeta.")

# 5. Funkcija za najskuplji proizvod
def najskuplji_proizvod(cenovnik):
    proizvod = max(cenovnik, key=cenovnik.get)
    return proizvod, cenovnik[proizvod]

najskuplji, cena_najskupljeg = najskuplji_proizvod(cene)
print(f"\nNajskuplji proizvod je: {najskuplji} - {cena_najskupljeg:.2f} €")

# 6. Nasumican proizvod
nasumican_proizvod = random.choice(proizvodi)
print(f"\nKorisniku je privukao paznju proizvod: {nasumican_proizvod}")

# 7. Prosecna cena svih proizvoda
prosecna_cena = sum(cene.values()) / len(cene)
prosecna_cena = math.floor(prosecna_cena * 100 + 0.5) / 100
print(f"\nProsecna cena svih proizvoda je: {prosecna_cena:.2f} €")

# 8. Broj prodatih komada svakog proizvoda
prodati_komadi = [5, 20, 12, 7, 10, 8, 25, 4]

ukupan_prihod = 0
for i in range(len(proizvodi)):
    ukupan_prihod += cene[proizvodi[i]] * prodati_komadi[i]

print(f"\nUkupan prihod od prodaje je: {ukupan_prihod:.2f} €")

# 9. Dodavanje novog proizvoda
novi_proizvod = "Tablet"
nova_cena = 299.99

proizvodi.append(novi_proizvod)
cene[novi_proizvod] = nova_cena

print("\nAzurirana lista proizvoda:")
for proizvod in proizvodi:
    print(f"{proizvod} - {cene[proizvod]:.2f} €")

# 10. Sortiranje proizvoda po ceni
sortirani_proizvodi = sorted(cene.items(), key=lambda x: x[1])

print("\nProizvodi sortirani po ceni:")
for proizvod, cena in sortirani_proizvodi:
    print(f"{proizvod} - {cena:.2f} €")
