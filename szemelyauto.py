from auto import Auto

class Szemelyauto(Auto):
    def __init__(self, rendszam, tipus, berleti_dij, ulohelyek_szama):
        super().__init__(rendszam, tipus, berleti_dij)
        self._ulohelyek_szama = ulohelyek_szama

    @property
    def ulohelyek_szama(self):
        return self._ulohelyek_szama
        
    def __str__(self):
        return f"Személyautó - {super().__str__()} - Ülések: {self._ulohelyek_szama}"