# check a number is a even or odd


num = int(input("Enter a number: "))

if(num % 2 == 0):
    print(f"The number {num} is Even.")
else:
    print(f"The number {num} is Odd.")



# check a number positive or negative

num = int(input("Enter a number: "))

if(num > 0):
    print(f"The number {num} is Positive.")
elif(num == 0):
    print(f"The number {num} is Zero")
else:
    print(f"The number {num} Negative")



# check the largest of 3 numbers

num1 = int(input("Enter a 1st number: "))
num2 = int(input("Enter a 2nd number: "))
num3 = int(input("Enter a 3rd number: "))

if(num1 > num2 and num1 > num3):
    print(f"The number {num1} is largest number.")
elif(num2 > num1 and num2 > num3):
    print(f"The number {num2} is largest number.")
else:
    print(f"The number {num3} is largest number.")



# check divisible by 5 and 3

num = int(input("Enter a number :"))

if(num % 5 == 0 and num % 3 == 0):
    print("A number is divisible by both.")
else: 
    print("a number is not divisible by both")


# student grade System

lucky_marks = int(input("Enter A Marks: "))

if(lucky_marks >= 90):
    print("A+ grade.")
elif(lucky_marks > 60 and lucky_marks < 90):
    print("B grade.")
elif(lucky_marks >= 35 and lucky_marks <= 60):
    print("C grade.")
else:
    print("fail.")


# # check the leap year

year = int(input("Enter A Year: "))

if(year % 4 == 0):
    print(f"The Year {year} Is Leap Year.")
else:
    print(f"The Year {year} Is Not Leap Year.")