from abc import ABC, abstractmethod


# 1. Abstrakte Basisklasse definieren
class Tier(ABC):

  @abstractmethod
  def laut_geben(self) -> str:
    pass


# 2. Abgeleitete Klassen (Subklassen), die die abstrakte Methode implementieren
class Hund(Tier):

  def laut_geben(self) -> str:
    return "Wuff!"


class Katze(Tier):

  def laut_geben(self) -> str:
    return "Miau!"




# 3. Eine Methode, die explizit das abstrakte Typ-Hint 'Tier' erwartet
def begruesse_tier(tier: Tier):
  # Python weiß hier, dass jedes 'Tier' eine 'laut_geben'-Methode hat
  print(f"Das Tier sagt: {tier.laut_geben()}")



# beispiel klassisch
def begruesse_katze(katze: Katze):
  print(f"Die Katze sagt: {katze.laut_geben()}" )



# 4. Verwendung: Wir übergeben abgeleitete Objekte
if __name__ == "__main__":
  mein_hund = Hund() # erzeugt ein Hund-Objekt
  meine_katze = Katze() # erzeugt ein Katze-Objekt

  # Beide Objekte können übergeben werden, obwohl die Methode 'Tier' erwartet
  begruesse_katze(meine_katze)  # Ausgabe: Die Katze sagt: Miau!


  begruesse_tier(mein_hund)  # Ausgabe: Das Tier sagt: Wuff!
  begruesse_tier(meine_katze)  # Ausgabe: Das Tier sagt: Miau!