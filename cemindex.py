class ReqemManipulyatoru:
    def __init__(self):
        self.reqemler = []

    def reqemleri_ekle(self, reqemler_listi):
        self.reqemler = reqemler_listi

    def toplamin_indekslerini_tap(self, hedef):
        n = len(self.reqemler)
        for i in range(n):
            for j in range(i+1, n):
                if self.reqemler[i] + self.reqemler[j] == hedef:
                    return i, j
        return -1

# Nümunə istifadə
manipulyator = ReqemManipulyatoru()
reqemler_listi = [1, 2, 3, 4, 5]
manipulyator.reqemleri_ekle(reqemler_listi)
hedef = 7
indeksler = manipulyator.toplamin_indekslerini_tap(hedef)
print("Toplamı hədəfə bərabər olan indekslər:", indeksler)
