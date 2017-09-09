class SweetPotato:

    def __init__(self):
        self.cookedString = '生的'
        self.cookedLevel = 0

    def cook(self, cooked_time):
        self.cookedLevel += cooked_time

        if self.cookedLevel >=0 and self.cookedLevel < 3:
            self.cookedString = "生"
        elif self.cookedLevel >=3 and self.cookedLevel < 5:
            self.cookedString = "半生"
        elif self.cookedLevel >=5 and self.cookedLevel < 8:
            self.cookedString = "熟了"
        else:
            self.cookedString = "过了"

    def __str__(self):
        return "digu %s(%d)"%(self.cookedString, self.cookedLevel)

di_gua = SweetPotato()
di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
print(di_gua)
