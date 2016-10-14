import datetime


class Person():
    def __init__(self, name):
        self.name = name
        self.birthday = None
        self.lastName = name.split(' ')[-1]

    def getLastName(self):
        return self.lastName

    def setBirthday(self, month, day, year):
        self.birthday = datetime.date(year, month, day)

    def getAge(self):
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days

    def __lt__(self, other):
        """return True if self's name is lexicographically
        less than other's name, and False otherwise"""
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName

    def __str__(self):
        return self.name


p1 = Person('Mark Zuckerberg')
p1.setBirthday(5, 14, 84)
p2 = Person('Drew Houston')
p2.setBirthday(3, 4, 83)
p3 = Person('Bill Gates')
p3.setBirthday(10, 28, 55)
p4 = Person('Andrew Gates')
p5 = Person('Steve Wozniak')
personList = [p1, p2, p3, p4, p5]

for e in personList:
    print(e)

print("----------------------------------------")

personList.sort()
for e in personList:
    print(e)


class MITPerson(Person):
    nextIdNum = 0  # next ID number to assign

    def __init__(self, name):
        Person.__init__(self, name)  # initialize Person attributes
        self.idNum = MITPerson.nextIdNum  # MIT Person attribute: unique ID
        MITPerson.nextIdNum += 1

    def getIdNum(self):
        return self.idNum

    def __lt__(self, other):
        return self.idNum < other.idNum

    def speak(self, utterance):
        return self.name + " says: " + utterance


print("----------------------------------------")

m3 = MITPerson('Mark Zuckerberg')
Person.setBirthday(m3, 5, 14, 84)
m2 = MITPerson('Drew Houston')
Person.setBirthday(m2, 3, 4, 83)
m1 = MITPerson('Bill Gates')
Person.setBirthday(m1, 10, 28, 55)
MITPersonList = [m1, m2, m3]

for e in MITPersonList:
    print(e)

print("----------------------------------------")

MITPersonList.sort()
for e in MITPersonList:
    print(e)

p1 = MITPerson("Eric")
p2 = MITPerson("John")
p3 = MITPerson("John")
p4 = Person("John")

print(p1 < p2)
"""
    p4 < p1 is equivalent to p4.__lt__(p1),
    which means we use the __lt__ method associated with the type of p4,
    namely a Person (the one that compares based on name)
"""
print(p4 < p1)
"""
    p1 < p4 is equivalent to p1.__lt__(p4),
    which means we use the __lt__ method associated with the type of p1,
    namely an MITPerson(the one that compares based on IDNum) and
    since p4 is a Person, it does not have an IDNum
"""

# print(p1 < p4) # Attribute Error

print("----------------------------------------")


class Student(MITPerson):
    pass


class UG(Student):
    def __init__(self, name, classYear):
        MITPerson.__init__(self, name)
        self.year = classYear

    def getClass(self):
        return self.year

    def speak(self, utterance):
        return MITPerson.speak(self, " YoBro, " + utterance)


class Grad(Student):
    pass


class TransferStudent(Student):
    pass


def isStudent(obj):
    return isinstance(obj, Student)


s1 = UG('Matt Damon', 2017)
s2 = UG('Ben Affleck', 2017)
s3 = UG('Lin Manuel Miranda', 2018)
s4 = Grad('Leonardo di Caprio')
S5 = TransferStudent("Robert deNiro")

print(s1)
print(s1.getClass())
print(s1.speak('where is the quiz?'))
print(s2.speak("I have no clue!"))

print("----------------------------------------")


class Professor(MITPerson):
    def __init__(self, name, department):
        MITPerson.__init__(self, name)
        self.department = department

    def speak(self, utterance):
        new = 'In course ' + self.department + " we say "
        return MITPerson.speak(self, new + utterance)

    def lecture(self, topic):
        return self.speak('it is obvious that ' + topic)


class Grades():
    """A mapping from students to a list of grades"""

    def __init__(self):
        """Create empty grade book"""
        self.students = []  # list of Student objects
        self.grades = {}  # maps idNum-> list of grades
        self.isSorted = True  # true if self.students is sorted

    def addStudent(self, student):
        """Assumes: student is of type Student
        Add student to the grade book"""
        if student in self.students:
            raise ValueError('Duplicate student')
        self.students.append(student)
        self.grades[student.getIdNum()] = []
        self.isSorted = False

    def addGrade(self, student, grade):
        """Assumes: grade is a float
        Add grade to the list of grades for student"""
        try:
            self.grades[student.getIdNum()].append(grade)
        except KeyError:
            raise ValueError('Student not in grade book')

    def getGrades(self, student):
        """Return a list of grades for student"""
        try:  # return copy of student's grades
            return self.grades[student.getIdNum()][:]
        except KeyError:
            raise ValueError('Student not in grade book')

    def allStudents(self):
        """Return a list of the students in the grade book"""
        if not self.isSorted:
            self.students.sort()
            self.isSorted = True
        return self.students[:]

        # return copy of list of students


def gradeReport(course):
    """Assumes: course is of type grades"""
    report = []
    for s in course.allStudents():
        tot = 0.0
        numGrades = 0
        for g in course.getGrades(s):
            tot += g
            numGrades += 1
        try:
            average = tot / numGrades
            report.append(str(s) + '\'s mean grade is ' + str(average))
        except ZeroDivisionError:
            report.append(str(s) + ' has no grades')
    return '\n'.join(report)


ug1 = UG('Matt Damon', 2018)
ug2 = UG('Ben Affleck', 2019)
ug3 = UG('Drew Houston', 2017)
ug4 = UG('Mark Zuckerberg', 2017)
g1 = Grad('Bill Gates')
g2 = Grad('Steve Wozniak')
six00 = Grades()
six00.addStudent(g1)
six00.addStudent(ug2)
six00.addStudent(ug1)
six00.addStudent(g2)
six00.addStudent(ug4)
six00.addStudent(ug3)

six00.addGrade(g1, 100)
six00.addGrade(g2, 25)
six00.addGrade(ug1, 95)
six00.addGrade(ug2, 85)
six00.addGrade(ug3, 75)

print(gradeReport(six00))

print("----------------------------------------")

six00.addGrade(g1, 90)
six00.addGrade(g2, 45)
six00.addGrade(ug1, 80)
six00.addGrade(ug2, 75)
print(gradeReport(six00))

print("----------------------------------------")
for s in six00.allStudents():
    print(s)
print("----------------------------------------")
for s in six00.students:
    print(s)