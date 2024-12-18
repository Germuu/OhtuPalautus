from tuomari import Tuomari
from tekoaly_parannettu import TekoalyParannettu
from kivi_paperi_sakset import KiviPaperiSakset

class KPSParempiTekoaly(KiviPaperiSakset):
    def __init__(self):
        super().__init__()
        self.tekoaly = TekoalyParannettu(10)  # Luo pysyvä instanssi

    def _toisen_siirto(self, ensimmaisen_siirto):
        tokan_siirto = self.tekoaly.anna_siirto()  # Käytä olemassa olevaa instanssia
        self.tekoaly.aseta_siirto(ensimmaisen_siirto)  # Päivitä tekoälyn muisti
        print(f"Tietokone valitsi: {tokan_siirto}")
        return tokan_siirto

