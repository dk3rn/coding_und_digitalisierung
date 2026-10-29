# Datensatz : Normale Werte liegen ca. zwischen 20 und 30
# Ausreisser sind die Werte 105 und 110
daten = [23 , 25, 22, 26, 24, 23, 105 , 25, 27, 24, 110 , 26]

# 1. Ausreisser suchen und filtern ( Schwellenwert > 50)
bereinigte_daten = []
ausreisser = []

for wert in daten :
    if wert > 50:
        ausreisser.append(wert)
    else :
        bereinigte_daten.append(wert)

print("hallo gummersbach")

# 2. Mittelwert ( Mean ) berechnen
summe = 0
for wert in bereinigte_daten :
    summe += wert

mittelwert = summe / len ( bereinigte_daten )

# 3. Median berechnen
sortierte_daten = sorted( bereinigte_daten )
n=len( sortierte_daten )
if n%2 == 0:
    median = (sortierte_daten [n//2 - 1] + sortierte_daten [n //2]) / 2
else :
    # Fall ungerade Anzahl von Elementen
    median = sortierte_daten [n//2]

print (f" Klassisch - Mittelwert : { mittelwert }, Median : { median }")




