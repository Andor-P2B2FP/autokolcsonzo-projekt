class Berles:
    def __init__(self, auto, datum):
        self._auto = auto
        self._datum = datum

    @property
    def auto(self):
        return self._auto
    
    @property
    def datum(self):
        return self._datum
    
    def __str__(self):
        return f"{self._auto.tipus} ({self._auto.rendszam}) - Dátum: {self._datum}"
    