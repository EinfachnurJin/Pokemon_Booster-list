# Pokémon Booster Checkliste
# Erstellt von Jin ^^ 
#Dieses Programm hilft beim Verwalten der Karten

# Bibliotheken:
import json
import os

# Begrüßung
print("Willkommen zur Pokémon-Booster-Checkliste!")

#Booster und Inhalt definieren
booster = {
    "Feuer-Booster": ["Glumanda", "Feurigel", "Flemmli"],
    "Wasser-Booster": ["Schiggy", "Karnimani", "Hytropi"],
    "Pflanzen-Booster": ["Bisasam", "Endivie", "Geckarbor"]
}
besitz = {
   "Feuer-Booster": [],
    "Wasser-Booster": [],
    "Pflanzen-Booster": []
}

def zeige_karten():
  if aktueller_booster:
    print(f"\nKarten im '{aktueller_booster}':")
    for i, karte in enumerate(booster[aktueller_booster], 1):
        print(f"{i}. {karte}")
  else:
        print("\n❗ Bitte zuerst einen Booster auswählen!")

# Speichern und Laden:
def besitz_speichern():
   with open("besitz_speichern.json", "w") as datei:
      json.dump(besitz, datei)

def besitz_laden():
   if os.path.exists("besitz_speichern.json"):
      with open("besitz_speichern.json", "r") as datei:
         besitz = json.load(datei)
   else:
    # Beispiel: neue leere Struktur zurückgeben
    besitz = {
        "Feuer-Booster": [],
        "Wasser-Booster": [],
        "Pflanzen-Booster": []
    }
   return besitz         
# Laden:
besitz = besitz_laden()   

# Unendlich Schleife
while True:
    print("\nWas möchtest du tun?")
    print("1. Booster auswählen")
    print("2. Karten aus aktiven Booster anzeigen")
    print("4. Sammlung anzeigen")
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

        check = input("Um ab zu harken bitte Nummer eingeben:")
        if check.isdigit():
           auswahl_index = int(check) -1
           karte = booster[aktueller_booster][auswahl_index]

           if karte not in besitz[aktueller_booster]:
              besitz[aktueller_booster].append(karte)
              print(f"✅ '{karte}' wurde abgehakt!")
           else:
             print(f"⚠️ '{karte}' war schon abgehakt.")

    
    elif auswahl == "4":
        print(json.dumps(besitz, indent=2, ensure_ascii=False))  
    elif auswahl == "5":
        besitz_speichern()
        print("Bis zum nächsten Mal :)")
        break  # Schleife beenden → Programm endet
    else:
        print("Ungültige Eingabe. Versuch es noch einmal :p")
