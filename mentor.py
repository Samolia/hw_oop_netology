import student as st

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.grades = {}
        super().__init__(name, surname)

    def average_rate(self, course):
        '''
        Считает среднюю оценку лектора за курс
        '''
        if course in self.courses_attached and len(self.grades[course]) > 0:
            average_rate = (sum(self.grades[course]) / len(self.grades[course]))
            return f'Средняя оценка лектора "{self.name} {self.surname}" за курс "{course}": {round(average_rate, 2)}'
        else:
            return 'Ошибка'

    def average_rate_all(self):
        '''
        Считает среднюю оценку лектора за все курсы
        '''
        all_rate = []
        for course in self.grades:
            all_rate.append(sum(self.grades[course]) / len(self.grades[course]))
            general_ball = sum(all_rate) / len(all_rate)
        return f'Средняя оценка лектора "{self.name} {self.surname}" за все курсы - {round(general_ball, 2)}'

    def __str__(self):
        '''
        Информация об объекте
        print(some_lecturer)
        '''
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {(self.average_rate_all().split(" ")[-1])}'

    def __lt__(self, other):
        '''
        Сравнить лекторов по среднему баллу за лекции
        '''
        if not isinstance(other, Lecturer):
            return'Not a Lecturer!'
        return self.average_rate_all() < other.average_rate_all()

def average_rate_lecturers(course, *args):
    '''
    Средняя оценка за лекции всех лекторов за курс
    '''
    overall_score = []
    for lecturer in args:
        if course in lecturer.courses_attached:
            overall_score.append(float((lecturer.average_rate(course)).split(" ")[-1]))
            general_ball_lecturers = round(sum(overall_score) / len(overall_score), 2)
    return f'Средняя оценка за лекции всех лекторов по "Python": {general_ball_lecturers}'


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        '''
        Позволяет оценить студента
        '''
        if isinstance(student, st.Student) and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        '''
        Информация об объекте
        print(some_reviewer)
        '''
        return f'Имя: {self.name}\nФамилия: {self.surname}'