# print number 1 to 10  output :- 1,2,3,4,5,6,7,8,9,10
for i in range(10):
    print(i+1);



# print even munbers  output :- 2,4,6,8
for i in range(1, 10):
    if(i % 2 == 0):
        print(i)


# print sum of n numbers
n = int(input("Enter A Number : "))

total_sum = 0

for i in range(n):
    total_sum = total_sum + i+1
    
print(total_sum) # out put is 10


# print factorial of a number
n_factorial = int(input("Enter The N number :"))

factorial = 1

for i in range(n_factorial):
    factorial = factorial*(i+1)

print(f"{n_factorial} factorial is {factorial}")



# print reverse a number and check palindrome number
number = int(input("Enter A Number: "))

reversed_number = 0
original_number = number

while number > 0:
    digit = number % 10 # store last digit
    reversed_number = reversed_number * 10 + digit  # make new number
    number //= 10 # remove the last digit

print(reversed_number)


# check the number is palindrome or not
if(reversed_number == original_number):
    print("The number is Palindrome")
else: 
    print("The number is Not Palindrome")



# print count digits and sum of digits
number = int(input("Enter A Number: "))

total_digit = 0
total_sum = 0

while number > 0:
    digit = number % 10
    total_sum += digit
    number //= 10
    total_digit += 1

print("number of digits ", total_digit)
print("digits of digits ", total_sum)