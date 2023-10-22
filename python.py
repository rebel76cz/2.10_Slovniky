def slovnik(nazev_souboru, slovnik):
    with open(nazev_souboru, "w") as soubor:
        for id_zamestnance, info in slovnik.items():
            soubor.write(f"Zaměstnanec {id_zamestnance}:\n")
            for klic, hodnota in info.items():
                soubor.write(f"{klic.capitalize()}: {hodnota}\n")
            soubor.write("\n")

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

nazev_souboru = "zamestnanci.txt"
slovnik(nazev_souboru, zamestnanci)
print(f"Soubor {nazev_souboru} byl vytvořen.")
