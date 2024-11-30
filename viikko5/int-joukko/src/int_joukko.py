class IntJoukko:
    DEFAULT_CAPACITY = 5
    DEFAULT_INCREMENT = 5

    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        self.kapasiteetti = kapasiteetti if isinstance(kapasiteetti, int) and kapasiteetti > 0 else self.DEFAULT_CAPACITY
        self.kasvatuskoko = kasvatuskoko if isinstance(kasvatuskoko, int) and kasvatuskoko > 0 else self.DEFAULT_INCREMENT
        self.ljono = [0] * self.kapasiteetti
        self.alkioiden_lkm = 0

    def _resize(self):
        new_size = len(self.ljono) + self.kasvatuskoko
        new_ljono = [0] * new_size
        for i in range(self.alkioiden_lkm):
            new_ljono[i] = self.ljono[i]
        self.ljono = new_ljono

    def kuuluu(self, luku):
        return luku in self.ljono[:self.alkioiden_lkm]

    def lisaa(self, luku):
        if not self.kuuluu(luku):
            if self.alkioiden_lkm >= len(self.ljono):
                self._resize()
            self.ljono[self.alkioiden_lkm] = luku
            self.alkioiden_lkm += 1
            return True
        return False

    def poista(self, luku):
        for i in range(self.alkioiden_lkm):
            if self.ljono[i] == luku:
                self._shift_left(i)
                self.alkioiden_lkm -= 1
                return True
        return False

    def _shift_left(self, index):
        for i in range(index, self.alkioiden_lkm - 1):
            self.ljono[i] = self.ljono[i + 1]
        self.ljono[self.alkioiden_lkm - 1] = 0

    def to_int_list(self):
        return self.ljono[:self.alkioiden_lkm]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def __str__(self):
        return "{" + ", ".join(map(str, self.to_int_list())) + "}"

    @staticmethod
    def yhdiste(a, b):
        tulos = IntJoukko()
        for luku in a.to_int_list() + b.to_int_list():
            tulos.lisaa(luku)
        return tulos

    @staticmethod
    def leikkaus(a, b):
        tulos = IntJoukko()
        for luku in a.to_int_list():
            if luku in b.to_int_list():
                tulos.lisaa(luku)
        return tulos

    @staticmethod
    def erotus(a, b):
        tulos = IntJoukko()
        for luku in a.to_int_list():
            if luku not in b.to_int_list():
                tulos.lisaa(luku)
        return tulos
