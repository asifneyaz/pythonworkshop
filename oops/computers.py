class Computer:
    def __init__(self):
        self.name = "peter"
        self.age = 28


c1 = Computer()
c2 = Computer()
c1.name = 'neyaz'
print(c1.name)
print(id(c1))
print(id(c2))