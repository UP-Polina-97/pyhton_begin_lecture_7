class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades_for_lecturer = {}
        self.course_mentored = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_for_lecturer = {}
        self.average_grade = []

    # for the exercise 3 what you get
    def __str__(self):
        return f'Имя: {self.name}, \nФамилия: {self.surname}, \nСредняя оценка за лекции:{self.average_grade}'

    # for the exercise 3 for the comparison
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a lecturer')
            return
        return self.average_grade < other.average_grade


# exercise 4 for dividing  not finished
# def __div__(self, subject, lecturer):


# return self.grades_for_lecturer // len(self.grades_for_lecturer)


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        super().rate_hw(student, course, grade)

    # for the exerise 3 what you get
    def __str__(self):
        return f'Имя: {self.name}, \nФамилия: {self.surname}'


# exerise 2

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_grade_st = []

    # exerise 2  grades for teachers  not working for some reason.
    def rate_hm_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in Lecturer.courses_attached:
            if course in lecturer.grades_for_lecturer:
                lecturer.grades_for_lecturer[course] += grade
            else:
                lecturer.grades_for_lecturer[course] = grade
        elif grade > 10:
            return 'can not be bigger than 10'
        else:
            return 'Ошибка'

    # for the exerise 3 what you get
    def __str__(self):
        return f'Имя: {self.name}, \nФамилия: {self.surname}, \nСредняя оценка за лекции:{self.average_grade_st}, \nКурсы в процессе изучения: {self.courses_in_progress}, \nЗавершенные курсы: {self.finished_courses}'

    # for exerise 4 diving not finished
    def __div__(self):
        return self.grades // len(self.grades)


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_lecturer = Lecturer('Mike', 'Visovsky')
best_lecturer.courses_attached += ['Python']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
best_student.rate_hm_lec(best_lecturer, 'Pyhton', 10)

# print(best_student.courses_in_progress)
print(best_lecturer.__dict__)
print(cool_mentor.grades_for_lecturer)
print('')
# print(best_student)
print('')
# print(best_lecturer)