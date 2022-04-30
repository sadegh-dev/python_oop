class Person:
    user = 'guest'
    def __init__(self,name):
        self.name = name

p1 = Person('charlie')
p1.city = 'Berlin'

print(p1.user)




