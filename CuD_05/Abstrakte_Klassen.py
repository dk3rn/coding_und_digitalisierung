from abc import ABC, abstractmethod
import copy

# Abstrakte Basisklasse
class Person(ABC):

    def __init__(self, name: str, id_nummer: int):
        self.name = name
        self.id_nummer = id_nummer

    # Abstrakte Methode: Muss von allen Unterklassen implementiert werden
    @abstractmethod
    def role_beschreibung(self) -> str:
        pass

    # Konkrete Methode, die von allen Unterklassen geerbt wird
    def ausgeben_info(self) -> str:
        return f"[{self.id_nummer}] {self.name} - Rolle: {self.role_beschreibung()}"




# Konkrete Unterklasse: Studierende
class Studierende(Person):

    def __init__(self, name: str, id_nummer: int, studiengang: str):
        super().__init__(name, id_nummer)
        self.studiengang = studiengang

    def role_beschreibung(self) -> str:
        return f"Studierende(r) im Studiengang {self.studiengang}"


# Konkrete Unterklasse: Professoren
class Professoren(Person):

    def __init__(self, name: str, id_nummer: int, fachbereich: str):
        super().__init__(name, id_nummer)
        self.fachbereich = fachbereich

    def role_beschreibung(self) -> str:
        return f"Professor(in) im Fachbereich {self.fachbereich}"


# Konkrete Unterklasse: Staff (Verwaltung/Mitarbeiter)
class Staff(Person):

    def __init__(self, name: str, id_nummer: int, abteilung: str):
        super().__init__(name, id_nummer)
        self.abteilung = abteilung

    def role_beschreibung(self) -> str:
        return f"Mitarbeiter(in) in der Abteilung {self.abteilung}"



# --- Anwendungsbeispiel ---
if __name__ == "__main__":
    # Versuch, eine Instanz der abstrakten Klasse zu erstellen (führt zu einem TypeError):
    try:
        ungueltig = Person("Test", 0)
    except TypeError as e:
        print(f"Fehler wie erwartet: {e}\n")

    # Erstellen von Objekten 
    studierende = Studierende("Max Mustermann", 1234, "Informatik")
    professor = Professoren("Dr. h.c. Ada Lovelace", 5678, "Mathematik")
    staff = Staff("John Doe", 9101, "Verwaltung")   

    # erstellen eines Feldes
    personen = [studierende, professor, staff]
    

    # Erstellen von konkreten Objekten
    personen1 = [
        Studierende("Anna Schmidt", 1001, "Informatik"),
        Professoren("Dr. h.c. Alan Turing", 2001, "Computer Science"),
        Staff("Maria Weber", 3001, "Studierendensekretariat"),
    ]



    neue_personen = personen.copy()  # Kopieren der Liste, um die ursprüngliche Liste nicht zu verändern

    # wichtig: import copy, um die Objekte selbst zu kopieren
    neue_personen = copy.deepcopy(personen)  # Tiefenkopie, um die Objekte selbst zu kopieren



    print(neue_personen[0].ausgeben_info())
    personen[0].name = "Klaus Müller"
    print(neue_personen[0].ausgeben_info())



    # Polymorphe Verwendung
    for p in personen:
        print(p.ausgeben_info())