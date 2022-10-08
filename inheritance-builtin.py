"""
    inheritance from built-in object

"""


class A(list):
    def append(self, element) :
        if not isinstance(element, str):
            raise TypeError("just string type")
        return super().append(element)


a = A()

a.append("A")
a.append("B")
print(a)
# OutPut: ['A','B']

a.append(3)
# OutPut: TypeError: just string type 

