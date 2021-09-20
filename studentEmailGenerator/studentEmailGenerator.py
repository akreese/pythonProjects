import random
student_names = input("Enter the first and last name of the students, each students seperated by a comma(,): ").lower()
student_names = student_names.split(',')
student_ids = []
student_emails = [] 

for i in range(len(student_names)):
  student_ids.append(random.randint(111111,999999))

for i in range(len(student_names)):
  first_initial = student_names[i][0]
  last_name = student_names[i].split(" ")[1]
  last_three = str(student_ids[i])[-3:]
  student_emails.append(first_initial +last_name +last_three +"@example.org")


for i in range(len(student_names)):
  print(f"Name: {student_names[i]}")
  print(f"ID: {student_ids[i]}")
  print(f"Email: {student_emails[i]}")