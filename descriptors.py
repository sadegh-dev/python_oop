class User:
    def __init__(self):
        self.__name = 'guest'
    
    @property
    def name(self):
        return self.__name