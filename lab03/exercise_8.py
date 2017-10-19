def name_and_age(name, age):
    if age > 0:
        return '%s is %d years old' % (name, age)
    else:
        return 'Error: Invalid age'


print(name_and_age('Joe Bloggs', 35))
print(name_and_age('Jane Bloggs', -35))
