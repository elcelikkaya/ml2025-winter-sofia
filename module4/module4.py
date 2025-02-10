
#The program asks the user for input N (positive integer) and reads it
positive_integer=int(input("Please provide a positive integer as input "))


#Then the program asks the user to provide N numbers (one by one) and reads all of them (again, one by one)
user_numbers=int(input("Please Provide desired numbers N:"))

numbers=[]

for i in range (user_numbers):
    number = int(input(f"Enter number {i + 1}: "))
    numbers.append(number)

#the program asks the user for input X (integer) and outputs: "-1" 
# if there were no such X among N read numbers, or the index (from 1 to N) 
# of this X if the user inputed it before.

X=int(input("Provide an X to search for:"))

if X in numbers:
    print(f"The number {X} is at position {numbers.index(X) + 1}")
else:
    print("-1")
