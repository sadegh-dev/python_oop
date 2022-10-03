"""

    __missing__
"""

class PersonAge(dict):
    def __missing__(self, key):
        return 0


users = PersonAge({"charlie":50, "katty":60})


print(users["charlie"])

#OutPut: 50


print(users["john"])

#OutPut: 0
