from berles import Berles

class Autokolcsonzo:
    def __init__(self, nev):
        self._nev = nev
        self._autok = []
        self._berlesek = []

    def auto_hozzaadas(self, auto):
        self._autok.append(auto)

    def berles(self, rendszam, datum):
        for berles in self._berlesek:
            if berles.auto.rendszam == rendszam and berles.datum == datum:
                raise Exception("Az autó már foglalt ezen a napon!")
            

        for auto in self._autok:
            if auto.rendszam == rendszam:
                uj_berles = Berles(auto, datum)
                self._berlesek.append(uj_berles)
                return auto.berleti_dij
        
        raise Exception("Nincs ilyen rendszamú autó!")
    
    def berles_lemondas(self, rendszam, datum):
        for berles in self._berlesek:
            if berles.auto.rendszam == rendszam and berles.datum == datum:
                self._berlesek.remove(berles)
                return
            
        raise Exception("Nem található ilyen bérlés")
    
    def berlesek_listazasa(self):
        if not self._berlesek:
            print("Nincsenek aktív bérlések.")
        else:
            for berles in self._berlesek:
                print(berles)

    def autok_listazasa(self):
        for auto in self._autok:
            print(auto)