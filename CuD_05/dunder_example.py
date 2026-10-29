# Dunder --> double underscore

'''
Diese Klasse repräsentiert ein Kraftfahrzeug mit Marke, Modell und Baujahr.
Ein Docstring (Dokumentations-String) ist ein spezieller Kommentar direkt 
 am Anfang einer Klasse, Funktion oder eines Moduls, der beschreibt, was 
dieser Code macht.
'''
    
class Auto:
    def __init__(self, marke, modell, baujahr):
        self.marke = marke
        self.modell = modell
        self.baujahr = baujahr

    def __str__(self):
        return f"{self.baujahr} {self.marke} {self.modell}"

# Ein Objekt der Klasse erstellen
mein_auto = Auto("Volkswagen", "Golf", 2021)

# print() ruft im Hintergrund automatisch __str__(self) auf
print(mein_auto)