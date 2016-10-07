import random


class Animal():
    def __init__(self, age):
        self.age = age
        self.name = None

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    def set_age(self, newage):
        self.age = newage

    def set_name(self, newname=""):
        self.name = newname

    def __str__(self):
        return "animal:" + str(self.name) + ":" + str(self.age)


class Cat(Animal):
    '''
    add new functionality with speak()
    instance of type Catcan be called with new methods
    instance of type Animalthrows error if called with new methods
    __init__ is not missing, uses the Animalversion
    '''

    def speak(self):
        print("meow")

    def __str__(self):
        return "cat:" + str(self.name) + ":" + str(self.age)


jelly = Cat(1)
jelly.set_name("JellyBelly")
print(jelly)

blob = Animal(1)
print(blob)
blob.set_name()
print(blob)


class Rabbit(Animal):
    tag = 1 # class variable

    def __init__(self, age, parent1=None, parent2=None):
        Animal.__init__(self, age)
        self.parent1 = parent1
        self.parent2 = parent2
        self.rid = Rabbit.tag
        Rabbit.tag += 1

    def get_rid(self):
        return str(self.rid).zfill(3) # for example 001 not 1

    def get_parent1(self):
        return self.parent1

    def get_parent2(self):
        return self.parent2

    def speak(self):
        print("meep")

    def __str__(self):
        return "rabbit:" + str(self.name) + ":" + str(self.age)




peter = Rabbit(5)
peter.set_name("Peter")
hopsy= Rabbit(3)
hopsy.set_name("Hopsy")
cotton = Rabbit(1, peter, hopsy)
cotton.set_name("Cottontail")
print(cotton)
print(cotton.get_parent1())
jelly.speak()
peter.speak()


# blob.speak() # AttributeError: 'Animal' object has no attribute 'speak'


class Person(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, age)
        Animal.set_name(self, name)
        self.friends = []

    def get_friends(self):
        return self.friends

    def add_friend(self, fname):
        if fname not in self.friends:
            self.friends.append(fname)

    def speak(self):
        print("hello")

    def age_diff(self, other):
        # alternate way: diff = self.age - other.age
        diff = self.get_age() - other.get_age()
        if self.age > other.age:
            print(self.name, "is", diff, "years older than", other.name)
        else:
            print(self.name, "is", -diff, "years younger than", other.name)

    def __str__(self):
        return "person:" + str(self.name) + ":" + str(self.age)


eric = Person("Eric", 45)
john = Person("John", 55)
eric.speak()
eric.age_diff(john)
Person.age_diff(john, eric)


class Student(Person):
    def __init__(self, name, age, major=None):
        Person.__init__(self, name, age)
        self.major = major

    def change_major(self, major):
        self.major = major

    def speak(self):
        r = random.random()
        if r < 0.25:
            print("i have homework")
        elif 0.25 <= r < 0.5:
            print("i need sleep")
        elif 0.5 <= r < 0.75:
            print("i should eat")
        else:
            print("i am watching tv")

    def __str__(self):
        return "student:" + str(self.name) + ":" + str(self.age) + ":" + str(self.major)


fred = Student("Fred", 18, "Course VI")
print(fred)
fred.speak()
fred.speak()
fred.speak()
fred.speak()

# jelly = Cat(1)
# jelly.set_name('Jelly')
# tiger = Cat(1)
# tiger.set_name('Tiger')
# bean = Cat(0)
# bean.set_name('Bean')
# print(jelly)
# jelly.speak()
# blob = Animal(1)
# peter = Rabbit(3)
# peter.speak()
# eric = Person('Eric', 45)
# eric.speak()
# john = Person('John', 55)
# eric.age_diff(john)
#
# fred = Student('Fred', 18, 'Course VI')
