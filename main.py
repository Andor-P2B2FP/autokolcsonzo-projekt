from autokolcsonzo import Autokolcsonzo
from szemelyauto import Szemelyauto
from teherauto import Teherauto
from datetime import datetime


def datum_ellenorzes(datum_szoveg):
    try:
        datetime.strptime(datum_szoveg, "%Y-%m-%d")
        return True
    except ValueError:
        return False
    

kolcsonzo = Autokolcsonzo("Gyors Autókölcsönző")

auto1 = Szemelyauto("AFH-232","Toyota Corolla", 12500, 5)
auto2 = Szemelyauto("DJE-678", "Ford focus", 15000, 5)
auto3 = Teherauto("JKH-942", "Skoda Octavia", 25000, 1500)

kolcsonzo.auto_hozzaadas(auto1)
kolcsonzo.auto_hozzaadas(auto2)
kolcsonzo.auto_hozzaadas(auto3)


#try:
#    kolcsonzo.berles("AFH-232", "2026-06-20")
#    kolcsonzo.berles("DJE-678", "2026-06-21")
#    kolcsonzo.berles("JKH-942", "2026-06-22")
#  kolcsonzo.berles("JKH-942", "2026-06-23")
#except Exception as e:
#   print(e)

while True:
    print("\n--- AUTÓKÖLCSÖNZŐ RENDSZER ---")
    print("1 - Autók listázása")
    print("2 - Autó bérlése")
    print("3 - Bérlés lemondása")
    print("4 - Bérlések listázása")
    print("0 - Kilépés")

    valasztas = input("Válassz egy műveletet: ")

    if valasztas == "1":
        kolcsonzo.autok_listazasa()

    elif valasztas == "2":
        rendszam = input("Add meg az autó rendszámát: ")
        datum = input("Add meg a dátumot (ÉÉÉÉ-HH-NN): ")

        if not datum_ellenorzes(datum):
            print("Hibás dátumformátum!")
            continue

        try:
            ar = kolcsonzo.berles(rendszam, datum)
            print(f"Sikeress bérlés! Fizetendő: {ar} Ft")
        except Exception as a:
            print(f"Hiba: {a}")

    elif valasztas == "3":
        rendszam = input("Add meg a rendszámot: ")
        datum = input("Add meg a dátumot (ÉÉÉÉ-HH-NN): ")

        try:
            kolcsonzo.berles_lemondas(rendszam, datum)
            print("Bérlés sikeresen lemondva.")
        except Exception as b:
            print(f"Hiba: {b}")
        
    elif valasztas == "4":
        kolcsonzo.berlesek_listazasa()

    elif valasztas == "0":
        print("Kilépés...")
        break

    else:
        print("Érvénytelen menüpont!")
