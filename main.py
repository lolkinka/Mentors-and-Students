class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def hw_grades(self):
        sum_of_grades = 0
        quantity_of_grades = 0
        for list_of_grades in self.grades.values():
            for grades in list_of_grades:
                sum_of_grades += grades
                quantity_of_grades += 1
        average = sum_of_grades / quantity_of_grades
        return average

    def courses(self):
        for course in self.grades.keys():
            return course

    def finished(self):
        list = self.finished_courses
        str = ', '.join(list)
        return str

    def __lt__(self, other):
        if not isinstance(other, Student):
            print ('Not a student')
            return
        return self.hw_grades() < other.hw_grades()


    def __str__(self):
        some_student = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self.hw_grades()} \nКурсы в процессе изучения: {self.courses()} \nЗавершенные курсы: {self.finished()}'
        return some_student


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []



class Lecturer(Mentor):
    def __init__(self,name,surname):
        super().__init__(name,surname)
        self.grades = {}

    def lecture_grades(self):
        sum_of_grades = 0
        quantity_of_grades = 0
        for course in self.grades.values():
            for grades in course:
                sum_of_grades += grades
                quantity_of_grades += 1
        average = sum_of_grades / quantity_of_grades
        return average

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print ('Not a lecturer')
            return
        return self.lecture_grades() < other.lecture_grades()


    def __str__(self):
        some_lecturer= f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.lecture_grades()}'
        return some_lecturer

class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        some_reviewer = f'Имя: {self.name} \nФамилия: {self.surname}'
        return some_reviewer




student = Student('Matvey', 'Drozdik', 'your gender')
student.courses_in_progress += ['Python']
student.finished_courses += ['Java',  'Git']

student2 = Student('Dima', 'Kozlov', 'your gender')
student2.courses_in_progress += ['Python']
student2.finished_courses += ['Java']

list_of_students = [student2, student]

some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.courses_attached += ['Python']

some_lecturer2 = Lecturer('Gordan', 'Freeman')
some_lecturer2.courses_attached += ['Python']

list_of_lecturers = [some_lecturer, some_lecturer2]

some_reviewer = Reviewer('Michael', 'Jordan')
some_reviewer.courses_attached += ['Python']

some_reviewer2 = Reviewer('Steve', 'Jobs')
some_reviewer2.courses_attached += ['Python']


some_reviewer.rate_hw(student, 'Python', 1)
some_reviewer.rate_hw(student, 'Python', 4)
some_reviewer.rate_hw(student, 'Python', 8)

some_reviewer.rate_hw(student2, 'Python', 13)
some_reviewer.rate_hw(student2, 'Python', 6)
some_reviewer.rate_hw(student2, 'Python', 9)

student.rate_hw(some_lecturer, 'Python', 12)
student.rate_hw(some_lecturer, 'Python', 6)
student.rate_hw(some_lecturer, 'Python', 3)

student.rate_hw(some_lecturer2, 'Python', 1)
student.rate_hw(some_lecturer2, 'Python', 6)
student.rate_hw(some_lecturer2, 'Python', 12)


def avg_grades_of_student(list_of_students, course):
    sum_of_grades = 0
    quantity_of_grades = 0
    for students in list_of_students:
        if course in student.courses_in_progress:
            for list in students.grades.values():
                for grades in list:
                    sum_of_grades += grades
                    quantity_of_grades += 1
        else:
            return ('Такого курса нет')
    avg = sum_of_grades / quantity_of_grades
    return avg

print (avg_grades_of_student(list_of_students, 'Python'))

def avg_grades_of_lecturers(list_of_lecturers, course):
    sum_of_grades = 0
    quantity_of_grades = 0
    for lecturers in list_of_lecturers:
        if course in lecturers.courses_attached:
            for list in lecturers.grades.values():
                for grades in list:
                    sum_of_grades += grades
                    quantity_of_grades += 1
        else:
            return ('Такого курса нет')
    avg = sum_of_grades / quantity_of_grades
    return avg


print (avg_grades_of_lecturers(list_of_lecturers, 'Python'))
print (some_lecturer > some_lecturer2)





