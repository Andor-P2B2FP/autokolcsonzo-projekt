from auto import Auto

class Teherauto(Auto):
    def __init__(self, rendszam, tipus, berleti_dij, teherbiras):
        super().__init__(rendszam, tipus, berleti_dij)
        self._teherbiras = teherbiras

    # Ki kell hozni az __init__ blokkból a bal szélre!
    @property
    def teherbiras(self):
        return self._teherbiras
        
    def __str__(self):
        return f"Teherautó - {super().__str__()} - Teherbírás: {self._teherbiras}kg"