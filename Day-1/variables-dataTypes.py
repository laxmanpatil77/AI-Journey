## swap two numbers

num1 = 10
num2 = 20

print(num1, num2)

# use for swap to numbers

num1, num2 = num2, num1

print(num1, num2)



#------------------------------------------------------------------
## take two numbers from input and print sum and product of numbers
#------------------------------------------------------------------

num1 = int(input("Enter Frist Number: "))
num2 = int(input("Enter Second Number: "))

total_sum = num1 + num2
product = num1 * num2

print("sum of both numbers: ", sum)
print("product of both numbers: ", product)



#------------------------------------------------------------------
## take name and age then print formatted output 
#------------------------------------------------------------------

name = input("Enter Your Name: ")
age = int(input("Enter Your Age: "))

print(f"My Name Is {name} And I Am {age} Year Old")

# take number and convert temperature in (c -> f) formula -> F = (c * 9/5) + 32

temp = int(input("Enter Temperature In Celsius "))

fahrenheit = (temp * 9/5) + 32

print("Temperature In Fahrenheit : ", fahrenheit)


#------------------------------------------------------------------
## take three numbers and find the average 
#------------------------------------------------------------------

num1 = int(input("Enter 1st Number: "))
num2 = int(input("Enter 2nd Number: "))
num3 = int(input("Enter 3rd Number: "))

average = (num1 + num2 + num3) / 3

print("Average of three numbers: ", average)


#------------------------------------------------------------------
## check number is even or odd using %
#------------------------------------------------------------------


num = int(input("Enter a number: "))

check_it = num % 2 == 0

print(check_it)




## What is Python? :- Python is high level, dynamicly typed, interpeted language.

## what is variable in python? :- variable is use to store data in mamory

## what is dynamic typing? :- python dynamicly detecte type of variables like num = 10 python automaticly detecte the num variable is type of integer

## difference betwen / and // :- single slace give decimal number and double slace use to get whole number

## why input needs type conversion? :- because the input function while return string value because use the int function use to convert string input value into number 