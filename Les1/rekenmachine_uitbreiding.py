getal1 = float(input("Geef een eerste getal: ")) #Float maakt het een kommagetal
getal2 = float(input("Geef een tweede getal: "))
bewerking = input("Welke bewerking wil je uitvoeren? (+,-,/,*): ")

#We berekenen de som
som = getal1 + getal2

#print("De som van " + getal1 + " en " + getal2 + " is "+ som + ".") Dit is een andere manier van tekst.
print (f"De som van {getal1} en {getal2} is {som}.")