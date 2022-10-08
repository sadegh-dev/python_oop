"""
    method chaining
"""


class Person:
    def __init__(self, name):
        self.name = name

    def set_email(self, salt):
        self.email = f'{self.name}.{salt}@email.com'
        return self
    
    @property
    def lower_email(self):
        self.email = self.email.lower()
        return self
    
    def show(self):
        print(self.email)


p1 = Person("charlie")

p1.set_email('AB532g').lower_email.show()


