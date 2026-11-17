#--------------------------------------------------------------------------
#Exercise 1

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")


person1 = Person("Lina", 20)

person1.display_info()


#---------------------------------------------------------------------------
#Exercise 2


class Person:

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age


person1 = Person("Lina", 20)
print(f"Name : {person1.name}")
print(f"Age : {person1.get_age()}")
#Comment: because callers can read the age without depending on the class's internal attribute.