getal1 = float(input("Geef een eerste getal: ")) #Float maakt het een kommagetal
getal2 = float(input("Geef een tweede getal: "))
bewerking = input("Welke bewerking wil je uitvoeren? (+,-,/,*): ")

if bewerking == "+":   #== : is gelijk aan ; <= : kleiner dan en gelijk aan ; < : kleiner dan; != : Niet gelijk aan
    print (f"{getal1} + {getal2} = {getal1+getal2}.")

if bewerking == "-":
    print (f"{getal1} - {getal2} = {getal1-getal2}.")

if bewerking == "/":
    print (f"{getal1} / {getal2} = {getal1/getal2}.")

if bewerking == "*":
    print (f"{getal1} * {getal2} = {getal1*getal2}.")