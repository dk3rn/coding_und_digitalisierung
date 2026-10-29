class Auto:
    '''
    Diese Klasse repräsentiert ein Kraftfahrzeug mit Marke, Modell und Baujahr.
    '''
    def __init__(self, marke, modell, baujahr):
        self.marke = marke
        self.modell = modell
        self.baujahr = baujahr

# 1. Über das __doc__ Attribut
print(Auto.__doc__)

# 2. Über die help()-Funktion (zeigt zusätzliche Infos)
help(Auto)