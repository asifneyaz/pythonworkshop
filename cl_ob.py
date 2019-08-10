class Car:

    def introduce_self(self):
        print('my name is ' + self.name)
        print('my color is ' + self.color)

car1 = Car()
car1.name = 'Tesla'
car1.color = 'Red'
car2 = Car()
car2.name = 'BMW'
car2.color = 'Black'

car1.introduce_self()
car2.introduce_self()
