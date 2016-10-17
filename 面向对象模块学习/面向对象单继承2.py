class S1:
    def F1(self):
        self.F2()
    def F2(self):
        pass

class S2(S1):
    def F3(self):
        self.F1()
    def F2(self):
        print(1)


obj=S2()
obj.F3()