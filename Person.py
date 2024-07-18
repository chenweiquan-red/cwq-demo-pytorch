class Person:
    """基类"""

    # count = 31
    # name = "Durant"

    def __init__(self, age, name):
        self.age = age
        self.count = None
        self.name = name

    def __int__(self, name, age):
        self.name = name

    def display(self):
        var = self.name, "今年", self.age
        print(var)


p = Person(11, "Durant")
p.display()
