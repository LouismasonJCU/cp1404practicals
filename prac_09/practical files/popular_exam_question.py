class Arbitrary(object):
    def __init__(self, data=0):
        self.data = data
    def getit(self):
        return self.data * "!"

class Thing(Arbitrary):
    def __init__(self, value =1):
        super().__init__(value * 2)

    def getit(self):
        return self.data * "#"

a, b, c = Arbitrary(2), Thing(), Thing(3)
print(a.getit(), b.getit(), c.getit())