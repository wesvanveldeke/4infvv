aantaltaken = int(input("Geef het aantal taken in: "))
aantalkeernietgeruimd = int(input("Hoeveel keer heb je niet opgeruimd?: "))

zakgeld = (5 + 2 * aantaltaken) - aantalkeernietgeruimd

print("Je hebt " + str(zakgeld) + " euro gekregen.")

#of

print(f"Je hebt {zakgeld} euro gekregen.")
