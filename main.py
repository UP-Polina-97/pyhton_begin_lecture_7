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
        self.grades = {}


    def average_grade(self):
        if not self.grades:
            print('not a lecturer!')
        else:
            list_ = []
            for i in self.grades.values():
                list_ += i

            return round((sum(list_) / len(list_)), 2)

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('')
            return
        return self.average_grade() < other.average_grade()



    def __str__(self):
        return f'Имя: {self.name}, \nФамилия: {self.surname}, \nСредняя оценка за лекции:{self.average_grade()}'


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        super().rate_hw(student, course, grade)

    def __str__(self):
        return f'Имя: {self.name}, \nФамилия: {self.surname}'


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.courses_participating = []
        self.grades_for_lecturer = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_hm_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}, \nФамилия: {self.surname}, \nСредняя оценка за лекции:{self.average_grade()}, \nКурсы в процессе изучения: {self.courses_in_progress}, \nЗавершенные курсы: {self.finished_courses}'


    def average_grade(self):
        if not self.grades:
            print('not a student')
        else:
            list_ = []
            for i in self.grades.values():
                list_ += i
            return round((sum(list_) / len(list_)), 2)

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('')
            return
        return self.average_grade() < other.average_grade()

#students info
best_student = Student('Ruoyana', 'Eman', 'Female')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['C++']
best_student.finished_courses += ['Git']

best_second_student = Student('Roy', 'Ilrick', 'male')
best_second_student.courses_in_progress += ['Python']
best_second_student.courses_in_progress += ['C++']


#lecturer info
best_lecturer = Lecturer('Mike', 'Visovsky')
best_lecturer.courses_attached += ['Python']
best_lecturer.courses_attached += ['C++']


second_lecturer = Lecturer('Mia', 'Faliroi')
second_lecturer.courses_attached += ['Python']
second_lecturer.courses_attached += ['C++']


#reviewer info
cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
cool_mentor.courses_attached += ['C++']

not_cool_mentor = Reviewer('Gary', 'Roigy')
not_cool_mentor.courses_attached += ['Python']
not_cool_mentor.courses_attached += ['C++']

#grades info rev
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'C++', 7)
cool_mentor.rate_hw(best_second_student, 'Python', 8)
cool_mentor.rate_hw(best_second_student, 'C++', 5)

not_cool_mentor.rate_hw(best_student, 'Python', 7)
not_cool_mentor.rate_hw(best_student, 'C++', 8)
not_cool_mentor.rate_hw(best_second_student, 'Python', 6)
not_cool_mentor.rate_hw(best_second_student, 'C++', 3)

#grades for lec info
best_student.rate_hm_lec(best_lecturer, 'Python', 9)
best_student.rate_hm_lec(best_lecturer, 'Python', 8)
best_student.rate_hm_lec(best_lecturer, 'C++', 7)

best_student.rate_hm_lec(second_lecturer, 'Python', 7)
best_student.rate_hm_lec(second_lecturer, 'Python', 5)
best_student.rate_hm_lec(second_lecturer, 'C++', 8)


best_second_student.rate_hm_lec(best_lecturer, 'Python', 6)
best_second_student.rate_hm_lec(best_lecturer, 'Python', 9)
best_second_student.rate_hm_lec(best_lecturer, 'C++', 8)

best_second_student.rate_hm_lec(second_lecturer, 'Python', 6)
best_second_student.rate_hm_lec(second_lecturer, 'Python', 7)
best_second_student.rate_hm_lec(second_lecturer, 'C++', 5)







print(best_lecturer.__dict__)
print(cool_mentor.grades_for_lecturer)
print('')
print(best_student)
print('')
print(best_lecturer)


