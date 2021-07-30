class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.courses_attached = []
        self.class_being_mentored = []

    def lecturer_grades(self, lecturer, course, course_grades):
        if isinstance(lecturer, Lecturer) and course in self.courses_attached and course in lecturer.class_being_mentored:
            if course in lecturer.grades_for_lectures:
                lecturer.grades_for_lectures[course] += [course_grades]
            else:
                lecturer. grades_for_lectures[course] = [course_grades]
        else:
            return 'Ошибка'




class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades_for_lectures = {}

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
        self.name = name
        self.surname = surname
        self.finished_class = []
        self.courses_attached = []
        self.course_grade = {}




class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'




# students in math class
fist_student = Student('Banny', 'Em', 'male')
second_student = Student('Hally', 'Maers', 'female')
third_student = Student('Mike', 'Maers', 'male')
#class math for the students above
fist_student.courses_in_progress += ['Math', 'Art', 'PE']
second_student.courses_in_progress += ['Math', 'Art', 'PE']
third_student.courses_in_progress += ['Math', 'Art', 'PE']

#lecturer name for math
firt_lecturer = Lecturer('Marie', 'Antoinette')
second_lecturer = Lecturer('Jamie', 'Antoinie')
third_lecturer = Lecturer('Jack', 'Anois')
# lecturer class being monitered
firt_lecturer.courses_attached += ['Math']
second_lecturer.courses_attached += ['Art']
third_lecturer.courses_attached += ['PE']
# Grades for students
#Math
firt_lecturer.rate_hw(fist_student, 'Math', 10)
firt_lecturer.rate_hw(second_student, 'Math', 7)
firt_lecturer.rate_hw(third_student, 'Math', 4)
#Art
second_lecturer.rate_hw(fist_student, 'Art', 8)
second_lecturer.rate_hw(second_student, 'Art', 6)
second_lecturer.rate_hw(third_student, 'Art', 9)
#PE
third_lecturer.rate_hw(fist_student, 'PE', 3)
third_lecturer.rate_hw(second_student, 'PE', 9)
third_lecturer.rate_hw(third_student, 'PE', 7)

#grades for teachers
#Math teacher
fist_student.lecturer_grades(firt_lecturer, 'Math', 9)
second_student.lecturer_grades(firt_lecturer, 'Math', 7)
third_student.lecturer_grades(firt_lecturer, 'Math', 8)
#Art teacher
fist_student.lecturer_grades(second_lecturer, 'Art', 5)
second_student.lecturer_grades(second_lecturer, 'Art', 8)
third_student.lecturer_grades(second_lecturer, 'Art', 8)
#PE teacher
fist_student.lecturer_grades(third_lecturer, 'PE', 8)
second_student.lecturer_grades(third_lecturer, 'PE', 7)
third_student.lecturer_grades(third_lecturer, 'Pe', 5)




best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)



##exersis 4 avegare of grades for students:

#all_students_dict = (name: grade)
#avegare_grade_for_students = (all_students_dict,key=all_students_dict.get)
#print("avegare grade for students is:", avegare_grade_for_students)


##exersis 4 avegare of grades for lectorers:

#all_lecturer_dict = (name: grade)
#avegare_grade_for_lecturer = (all_lecturer_dict,key=all_lecturer_dict.get)
#print("avegare grade for lecturer is:", avegare_grade_for_lecturer)


print(best_student.grades)

print(cool_mentor.name)

print(firt_lecturer.course_grade)
