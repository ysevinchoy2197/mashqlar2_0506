#24-masala
class Ombor:
    def __init__(self, nomi, mahsulot_soni):
        self.nomi = nomi
        self.__mahsulot_soni = mahsulot_soni

    def qabul(self, n):
        self.__mahsulot_soni += n

    def sotiw(self, n):
        self.__mahsulot_soni -= n

    def info(self):
        print(f"Nomi: {self.nomi}")
        print(f"Mahsulot soni: {self.__mahsulot_soni}")

o1 = Ombor("birnarsa xona", 150)
o1.qabul(50)
o1.sotiw(59)
o1.info()
