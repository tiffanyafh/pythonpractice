university = {
    "classes": [
        {
            "course": {"course_code": "CS101", "course_names": ["Introduction to Computer Science", "Intro to CS"]},
            "instructor": "Dr. Smith",
            "students": ["John", "Alice", "Bob", "Emily", "Charlie"]
        },
        {
            "course": {"course_code": "MATH201", "course_names": ["Calculus I", "Cal I", "Intro to Calculus"]},
            "instructor": "Prof. Johnson",
            "students": ["Alice", "Bob", "Emily", "David", "Eva"]
        },
        {
            "course": {"course_code": "PHYS202", "course_names": ["Physics II"]},
            "instructor": "Dr. Anderson",
            "students": ["John", "Charlie", "David", "Eva", "Frank"]
        }
    ],
    "labs": [
        {
            "lab": {"lab_code": "CS101L", "lab_names": ["Intro to CS Lab"]},
            "instructor": "TA Smith",
            "students": ["John", "Alice", "Bob"]
        },
        {
            "lab": {"lab_code": "MATH201L", "lab_names": ["Calculus I Lab"]},
            "instructor": "TA Johnson",
            "students": ["Alice", "Bob", "Emily"]
        },
        {
            "lab": {"lab_code": "PHYS202L", "lab_names": ["Physics II Lab"]},
            "instructor": "TA Anderson",
            "students": ["John", "Charlie", "David"]
        }
    ]
}

# Update Course Instructor:
# Given a course code, update the instructor's name for that course.
# If the course is not found, print a message indicating that.
classes = university['classes']
labs = university['labs']


def update_instructor(course_code, new_instructor):
    for course in classes:
        if course_code == course['course']['course_code']:
            course['instructor'] = new_instructor
            return new_instructor
    print(f"Course with code {course_code} not found.")


new_instructor = update_instructor("CS101", "Prof. Tiffany")
print(f"Instructor updated for CS101: {new_instructor}")



# Add Student to Lab:
# Given a lab code, add a new student to the list of students for that lab.
# If the lab is not found, print a message indicating that.
def add_student(lab_code, new_student):
    for lab in labs:
        if lab_code == lab['lab']['lab_code']:
            lab['students'].append(new_student)
            return new_student
    print(f"Lab with code {lab_code} not found.")


new_student = add_student("CS101L", "Alexa")
print(f"New student has been added to lab 'CS101L. Her name is {new_student}.")


# Remove Student from Class:
# Given a course code and a student's name, remove the student from the list of students enrolled in that course.
# If the course is not found or the student is not enrolled, print a message indicating that.
def remove_student(course_code, student_name):
    for course in classes:
        if course_code == course['course']['course_code']:
            if student_name in course['students']:
                course['students'].remove(student_name)
                return student_name
            else:
                print(f"{student_name} is not enrolled in {course_code}.")
                return
    print(f"Course with code {course_code} not found.")


student_name = remove_student('MATH201', 'Eva')
print(f"{student_name} has been removed from course 'MATH201'.")


#How many classes are offered in total?
classes = university["classes"]
num_classes = len(classes)
print(f"In total there are {num_classes} classes.")


#Who is the instructor for the "Calculus I" course?
classes = university["classes"]
calculus_instructor = []
for course in classes:
     if "Calculus I" in course["course"]["course_names"]:
         calculus_instructor = course["instructor"]
print(f"The instructor for 'Calculus I' is {calculus_instructor}")


#How many students are enrolled in the "Physics II Lab"?
labs = university["labs"]
number_students = 0
for lab in labs:
    if "Physics II Lab" in lab["lab"]["lab_names"]:
        number_students = len(lab["students"])
print(f"There are {number_students} students enrolled in the 'Physics II Lab'")


#List the students enrolled in both the "Introduction to Computer Science" class
#and the "Intro to CS Lab".
classes = university['classes']
labs = university["labs"]

class_list = []
lab_list = []

for course in classes:
    if "Introduction to Computer Science" in course['course']['course_names']:
        class_list = set(course['students'])
for lab in labs:
    if "Intro to CS Lab" in lab['lab']['lab_names']:
        lab_list = set(lab['students'])
if class_list and lab_list:
    students_in_both = class_list.intersection(lab_list)
    print("Students enrolled in both the class and the lab:")
    for student in students_in_both:
        print(student)
else:
    print("One or both of the classes or labs were not found.")


#What is the course code for the "Calculus I Lab"?
labs = university['labs']
course_code = []
for lab in labs:
    if "Calculus I Lab" in lab['lab']['lab_names']:
        course_code = lab['lab']['lab_code']
        print(f"The course code is {course_code} for the 'Calculus I Lab'")


#How many labs are offered in total?
labs = university['labs']
number_labs = len(labs)
print(f"There are {number_labs} labs offered.")


#List the instructors for all the labs.
labs = university['labs']
instructor_list = []
for lab in labs:
    if "instructor" in lab:
        instructor_list = lab['instructor']
        print(instructor_list)


#Which students are enrolled in both "Physics II" class and lab?
classes = university['classes']
labs = university['labs']

class_list = []
lab_list = []

for course in classes:
    if "Physics II" in course['course']['course_names']:
        class_list = set(course['students'])

for lab in labs:
    if "Physics II Lab" in lab['lab']['lab_names']:
        lab_list = set(lab['students'])

if class_list and lab_list:
    students_in_both = class_list.intersection(lab_list)
    print("Students enrolled in both the class and the lab:")
    for student in students_in_both:
        print(student)
else:
    print("One or both of the classes or labs were not found.")


#List all the courses taught by Dr. Smith.
classes = university['classes']
courses_taught = []
for course in classes:
    if "Dr. Smith" in course['instructor']:
        courses_taught.append(course['course']['course_code'])
print("Courses taught by Dr. Smith:")
for course_taught in courses_taught:
    print(course_taught)


#List all the students enrolled in at least one class or lab.
classes = university['classes']
labs = university['labs']

class_list = []
lab_list = []

for course in classes:
    if 'students' in course:
        class_list.extend(course['students'])


for lab in labs:
    if "students" in lab:
        lab_list.extend(lab['students'])

all_students = list(set(class_list + lab_list))
print("Students enrolled in at least one class or lab:")
for student in all_students:
    print(student)


#Give all the courses and labs that Charlie is enrolled to
classes = university['classes']
labs = university['labs']

class_charlie = []
lab_charlie = []

for course in classes:
    if "Charlie" in course['students']:
        class_charlie.append(course['course']['course_code'])

for lab in labs:
    if "Charlie" in lab['students']:
        lab_charlie.append(lab['lab']['lab_code'])
print(f"Charlie is enrolled in {class_charlie} courses and {lab_charlie} lab.")



#What's the code for the class "Intro to Calc"
classes = university['classes']

class_code = None

for course in classes:
    if "Intro to Calculus" in course['course']['course_names']:
        class_code = course['course']['course_code']
print(f"The code for course 'Intro to Calc' is {class_code}.")