person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person
print(name, last_name, city, phone, country)

text1 = 'результат операции: 42'
print(text1[:])
print(text1.index(':'))
a = text1.index(':')
print(int(text1[a + 2:]) + 10)

text2 = 'результат операции: 514'
print(text2[:])
print(text2.index(':'))
a = text2.index(':')
print(int(text2[a + 2:]) + 10)

text3 = 'результат работы программы: 9'
print(text3[:])
print(text3.index(':'))
a = text3.index(':')
print(int(text3[a + 2:]) + 10)

students = ['Ivanov', 'Petrov', 'Sidorov']
print(students)
subjects = ['math', 'biology', 'geography']
print(subjects)
print('Students', ', ' .join(students), 'study these subjects:', ', ' .join(subjects))
