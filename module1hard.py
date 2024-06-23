task = 'Дополнительное практическое задание по модулю: "Базовые структуры данных."'
avtor = 'Студент Крылов Эдуард Васильевич'
thanks = 'Благодарю за внимание :-)'
print()
print(task)
print(avtor)
print()
students = {'Johnny', 'Bilbo', 'Steve', 'Здуард', 'Khendrik', 'Aaron'}
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5], [5, 5, 5, 5, 5, 5, 5]]
students_dis = {}
print('Изначальный список учеников:', students)
students = sorted(students)
print('Список учеников по алфавиту:', students)
print('Список групп оценок:', grades)
print()
quanty_students = len(students)
quanty_ring = len(grades)
if quanty_students == quanty_ring:
    print('Количество учеников:', quanty_students)
    print('Количество групп оценок:', quanty_ring)
    for i in range(quanty_students):
        quanty_rating = grades[i]
        quanti_score = len(quanty_rating)
        average_score = float(sum(quanty_rating) / quanti_score)
        # print('Ученик:',students[i], 'Оценки:', quanty_rating, 'Кол-во оценок:', quanti_score, 'Средний балл:', average_score)
        students_dis.update({students[i]: average_score})
else:
    print('Число учеников =', quanty_students, 'не совпадает с количеством оценок =', quanty_ring)
print()
print('Средний балл по каждому ученику:', students_dis)
print()
print(thanks)