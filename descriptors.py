class User:
    def __init__(self):
        self.__name = 'guest'
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        if name != 'admin':
            self.__name = name
        return self.__name

    @name.deleter
    def name(self):
        self.__name = None

p1 = User()

p1.name = 'charlie'
print(p1.name)

del p1.name
print(p1.name)

