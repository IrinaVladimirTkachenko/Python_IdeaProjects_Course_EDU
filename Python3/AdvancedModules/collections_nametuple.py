from collections import namedtuple

#jake = ('Jake', 'Smith', 19, 'male')
#jim = ('Jim', 'Blade', 23, 'male')
#jane = ('Jane', 'Morrison', 20, 'female')

Person = namedtuple("Person", "name surname age gender")
jake = Person(name='Jake', surname='Smith', age=19, gender='male')
jim = Person(name='Jim', surname='Blade', age=23, gender='male')
jane = Person(name='Jane', surname='Morrison', age=20, gender='female')


print(jake.name)
print(jake.surname)
print(jane.age)
print(jane.surname)
jane = jane._replace(surname='Blade')
print(jane.surname)
