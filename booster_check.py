# Pokémon Booster Checkliste
# Erstellt von Jin ^^ 
#Dieses Programm hilft beim Verwalten der Karten

# Begrüßung
print("Willkommen zur Pokémon-Booster-Checkliste!")

#Booster und Inhalt definieren
booster = {
    "Feuer-Booster": ["Glumanda", "Feurigel", "Flemmli"],
    "Wasser-Booster": ["Schiggy", "Karnimani", "Hytropi"],
    "Pflanzen-Booster": ["Bisasam", "Endivie", "Geckarbor"]
}

#Booster anzeigen:

# Unendlich Schleife
while True:
    print("\nWas möchtest du tun?")
    print("1. Booster auswählen")
    print("2. Karten aus aktiven Booster anzeigen")
    print("3. Karte abharken")
    print("4. Sammlung erweitern")
    print("5. Beenden")

    # Eingabe vom Benutzer
    auswahl = input("Bitte gib die Zahl der Wahl ein: ")
    

    # Entscheidungen basierend auf der Eingabe
    if auswahl == "1":
      print("\nVerfügbare Booster:")
      for name in booster:
         print(f"- {name}")
    
      eingabe = input("Bitte gib den Namen des gewünschten Boosters ein: ")

      if eingabe in booster:
         aktueller_booster = eingabe
         print(f"Booster '{aktueller_booster}' ausgewählt!")
      else:
        print("Booster nicht gefunden – bitte nochmal versuchen.")

    elif auswahl == "2":
        zeige_karten()

    elif auswahl == "3":
        print("Du willst eine neue Karte abharken? (kommt später)")
    elif auswahl == "4":
        print("Du möchtest die Sammlung Erweitern? (kommt noch)")    
    elif auswahl == "5":
        print("Bis zum nächsten Mal :)")
        break  # Schleife beenden → Programm endet
    else:
        print("Ungültige Eingabe. Versuch es noch einmal :p")
