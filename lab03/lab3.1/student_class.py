class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_age(self):
        return self.age


b = student('Joe Bloggs', 45)

print(b)
print(b.name, 'is', b.get_age())
