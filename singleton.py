# Creational

class Singleton(type):
    __instance = None


class Db( metaclass = Singleton ):
    pass
