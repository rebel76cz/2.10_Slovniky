zamestnanci = {
    1: {
        "jmeno": "Martin",
        "prijmeni": "Hruska",
        "pozice": "Programátor",
        "email": "martinhruska@seznam.cz",
        "kancelar": "C1"
    },
    2: {
        "jmeno": "Pepa",
        "prijmeni": "Pepina",
        "pozice": "Kuchař",
        "email": "Pepik1@seznam.cz",
        "kancelar": "B7"
    },
    3: {
        "jmeno": "Eliška",
        "prijmeni": "Pokorná",
        "pozice": "Učetní",
        "email": "Epokorna@seznam.cz",
        "kancelar": "V2"
    },
    4: {
        "jmeno": "Marek",
        "prijmeni": "Doležal",
        "pozice": "Asistent",
        "email": "MarekD@seznam.cz",
        "kancelar": "G1"
    }
}

print("Zde je seznam zaměstnanců:")
for id_zamestnance, info in zamestnanci.items():
    print(f"Zaměstnanec {id_zamestnance}:")
    print(f"Jméno: {info['jmeno']}")
    print(f"Příjmení: {info['prijmeni']}")
    print(f"Pozice: {info['pozice']}")
    print(f"Email: {info['email']}")
    print(f"Kancelář: {info['kancelar']}")
    print()

print("Všechny důležité údaje:")
for id_zamestnance, info in zamestnanci.items():
    print(f"{info['jmeno']} {info['prijmeni']}, {info['email']}")


id = 1  
vybrany_zamestnanec = zamestnanci.get(id )
if vybrany_zamestnanec:
    print(f"Vybraný zaměstnanec: {vybrany_zamestnanec['jmeno']} {vybrany_zamestnanec['prijmeni']}, pozice: {vybrany_zamestnanec['pozice']}")
