class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def grades_greater_than(self, number):
        return [grade for grade in self.grades if grade > number]

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Average Grade: {self.average_grade():.2f}"


class GraduateStudent(Student):
    def __init__(self, name, age, grades, thesis_topic):
        super().__init__(name, age, grades)
        self.thesis_topic = thesis_topic

    def __str__(self):
        return super().__str__() + f", Thesis Topic: {self.thesis_topic}"


class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def course_average(self):
        if not self.students:
            return 0
        total = sum(student.average_grade() for student in self.students)
        return total / len(self.students)

    def top_student(self):
        if not self.students:
            return None
        return max(self.students, key=lambda student: student.average_grade())


s1 = Student("Анна", 19, [90, 85, 88])
s2 = Student("Дмитро", 20, [70, 75, 72])
gs1 = GraduateStudent("Марія", 23, [95, 93, 97], "Машинне навчання")

print(s1)
print(s2)
print(gs1)
print("\nОцінки Анни більше 87:", s1.grades_greater_than(87))

course = Course("Програмування на Python")
course.add_student(s1)
course.add_student(s2)
course.add_student(gs1)

print("\nСередній бал на курсі:", course.course_average())
print("Найкращий студент:", course.top_student())
