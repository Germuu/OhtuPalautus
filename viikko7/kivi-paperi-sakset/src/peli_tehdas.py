from kps_tekoaly import KPSTekoaly
from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_parempi_tekoaly import KPSParempiTekoaly

class PeliTehdas:
    @staticmethod
    def luo_peli(tyyppi):
        if tyyppi == "kaksinpeli":
            return KPSPelaajaVsPelaaja()  
        elif tyyppi == "helppo":
            return KPSTekoaly()
        elif tyyppi == "vaikea":
            return KPSParempiTekoaly()
        else:
            raise ValueError(f"Tuntematon pelityyppi: {tyyppi}")
