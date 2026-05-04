# Project 1: Smart Student Result System


# getting student name
student_name = input("Enter you name : ")  


# get subject marks from student
student_subject_math = int(input("Enter Your Math Marks : "))
student_subject_physics = int(input("Enter Your Physics Marks : "))
student_subject_chemistry = int(input("Enter Your Chemistry Marks : "))


# total marks calculate and print
total_marks = (student_subject_physics + student_subject_chemistry + student_subject_math)
print(f"Total {total_marks}")


# find average of all subject and print
average = (student_subject_physics + student_subject_chemistry + student_subject_math)/3
print(f"Average {average}")


# find the grade and print
if (average >= 90):
    print("Grade A")
elif (average >= 70):
    print("Grade B")
elif (average >= 50):
    print("Grade C")
elif (average >= 35):
    print("Grade D")
else:
    print("Grade Fail")


# print the result 
if (student_subject_chemistry >= 35 and
    student_subject_math >= 35 and 
    student_subject_physics >= 35): 
    
    print("Result Pass")
else:
    print("Result Fail")