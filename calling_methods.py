import student as st
import mentor as mr


def separator():
    print('=' * 60)

student1 = st.Student('Vasya', 'Pupkin', 'male')
student2 = st.Student('Pupka', 'Vasina', 'female')

lecturer1 = mr.Lecturer('Mr', 'Prepod')
lecturer2 = mr.Lecturer('Mrs', 'Uchilka')

reviewer1 = mr.Reviewer('Mr', 'Review1')
reviewer2 = mr.Reviewer('Mrs', 'Review2')

student1.courses_in_progress += ['Python'] + ['GIT']
student2.courses_in_progress += ['Python']
student1.finished_courses += ['English']
student2.finished_courses += ['GIT']

lecturer1.courses_attached += ['Python'] + ['GIT']
lecturer2.courses_attached += ['Python']

reviewer1.rate_hw(student1, 'Python', 7)
reviewer2.rate_hw(student1, 'Python', 6)
reviewer1.rate_hw(student1, 'GIT', 10)
reviewer2.rate_hw(student1, 'GIT', 10)
reviewer1.rate_hw(student2, 'Python', 9)
reviewer2.rate_hw(student2, 'Python', 8)

student1.rate_lecture(lecturer1, 'Python', 10)
student2.rate_lecture(lecturer1, 'Python', 10)
student1.rate_lecture(lecturer2, 'Python', 7)
student2.rate_lecture(lecturer2, 'Python', 5)
student1.rate_lecture(lecturer1, 'GIT', 8)
student2.rate_lecture(lecturer1, 'GIT', 9)

print(student1.return_grades())
print(student2.return_grades())
separator()
print(student1.average_rate('Python'))
print(student1.average_rate('GIT'))
print(student2.average_rate('Python'))
separator()
print(student1.average_rate_hw())
print(student2.average_rate_hw())
separator()
print(lecturer1.average_rate('Python'))
print(lecturer1.average_rate('GIT'))
print(lecturer2.average_rate('Python'))
separator()
print(lecturer1.average_rate_all())
print(lecturer2.average_rate_all())
separator()
print(student1 < student2)
separator()
print(lecturer1 < lecturer2)
separator()
print(st.average_rate_students('Python', student1, student2))
separator()
print(mr.average_rate_lecturers('Python', lecturer1, lecturer2))
separator()
print(reviewer1)
print(reviewer2)
separator()
print(student1)
print(student2)
separator()
print(lecturer1)
print(lecturer2)