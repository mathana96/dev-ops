class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_age(self):
        return self.age


class part_time_student(student):
    def __init__(self, name, age, employer):
        student.__init__(self, name, age)
        self.employer = employer




a = student('Jane Bloggs', 34)
print(a.name, 'is', a.get_age())

b = part_time_student('Jumbo Bloggs', 72, 'Jumbo')
print(b.name, b.get_age(), b.employer)
