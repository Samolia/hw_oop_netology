import mentor as mr


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def return_grades(self):
        '''
        Посмотреть все оценки студента
        '''
        return f'"{self.name} {self.surname}" - {self.grades}'

    def rate_lecture(self, lecturer, course, grade):
        '''
        Позволяет оценить лектора
        '''
        if isinstance(lecturer, mr.Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_rate(self, course):
        '''
        Считает среднюю оценку студента за курс
        '''
        if course in self.courses_in_progress and len(self.grades[course]) > 0:
            average_rate = (sum(self.grades[course]) / len(self.grades[course]))
            return f'Средняя оценка студента "{self.name} {self.surname}" за курс "{course}": {round(average_rate, 2)}'
        else:
            return 'Ошибка'

    def average_rate_hw(self):
        '''
        Считает среднюю оценку студента за все курсы
        '''
        all_rate = []
        for course in self.grades:
            all_rate.append(sum(self.grades[course]) / len(self.grades[course]))
            general_ball = sum(all_rate) / len(all_rate)
        return f'Средняя оценка студента "{self.name} {self.surname}" за все курсы - {round(general_ball, 2)}'

    def __str__(self):
        '''
        Информация об объекте
        print(some_student)
        '''
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {(self.average_rate_hw()).split(" ")[-1]}\n' \
               f'Курсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}'

    def __lt__(self, other):
        '''
        Сравнить студентов по среднему баллу за ДЗ
        '''
        if not isinstance(other, Student):
            return 'Not a Student!'
        return self.average_rate_hw() < other.average_rate_hw()

def average_rate_students(course, *args):
    '''
    Средняя оценка за лекции всех студентов за курс
    '''
    overall_score = []
    for student in args:
        if course in student.courses_in_progress:
            overall_score.append(float((student.average_rate(course)).split(" ")[-1]))
            general_ball_students = round(sum(overall_score) / len(overall_score), 2)
    return f'Средняя оценка за лекции всех студентов по "Python": {general_ball_students}'