drink = {
    'name': 'orange juice',
    'ingredients': ['orange', 'water', 'sugar'],
    'pricing': {
        'subtotal': 1,
        'tax': 0.2
    }
}

first_ingredient = drink['ingredients'][0]
print(first_ingredient)

total_price = drink['pricing']['subtotal'] + drink['pricing']['tax']
print(total_price)


school_dict = {
  "students": [
    {
      "name": "John",
      "age": 18,
      "grade": "A"
    },
    {
      "name": "Alice",
      "age": 17,
      "grade": "B"
    },
    {
      "name": "Bob",
      "age": 19,
      "grade": "C"
    }
  ],
  "teachers": [
    {
      "name": "Mr. Smith",
      "subject": "Math",
      "experience": 10
    },
    {
      "name": "Ms. Johnson",
      "subject": "English",
      "experience": 8
    }
  ]
}

students = school_dict['students']
oldest_student_name = ""
oldest_student_age = 0
for student in students:
    if student['age'] > oldest_student_age:
        oldest_student_name = student['name']
        oldest_student_age = student['age']
print(f"Oldest student is {oldest_student_name} who is {oldest_student_age} years old")

students = school_dict['students']
highest_student_name = ""
highest_student_grade = ""
for student in students:
    if student['grade'] > highest_student_grade:
        highest_student_name = student['name']
        highest_student_grade = student['grade']
print(f"The highest student grade is {highest_student_grade} from {highest_student_name}")

students = school_dict['students']
bob_info = None
for student in students:
    if student['name'] == 'Bob':
        bob_info = student
        break
        
if bob_info is not None:
    print("Bob's information:")
    for key, value in bob_info.items():
        print(f"{key}: {value}")
else:
    print("Bob is not found in the student list.")

teachers = school_dict['teachers']
teacher_name = None
subject_math = None
for teacher in teachers:
    if teacher['subject'] == 'Math':
        teacher_name = teacher['name']
print(f"The teacher that gives Math is {teacher_name}")

teachers = school_dict['teachers']
teacher_name = None
teacher_most_experience = 0
for teacher in teachers:
    if teacher['experience'] > teacher_most_experience:
        teacher_name = teacher['name']
        teacher_most_experience = teacher['experience']
print(f"The teacher with the most experience is {teacher_name} with {teacher_most_experience} years of experience.")



