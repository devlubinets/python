class PartyAnimal:
    x = 0

    def __init__(self):
        self.x = 10

    def party(self):
        self.x = self.x + 2*2
        print(self.x)

    def show(self):
        return self.x * self.x

an = PartyAnimal()
an.party()
an.party()

an1 = PartyAnimal()
an1.party()
an1.party()

print(an1.show())
print(dir(an1))
print(type(an1))
print(an1.__init__())
