import math
# Print a program that computes and prints the results of the equation below.
sub_1 = 94 - 17
sub_2 = 415 - 319
div = sub_1 / sub_2
print(div, '\n')
# Ask a user to enter a number. Print the square of the number. The output should read “The square
# of _ is _”
Num = int(input("Enter number: "))
Num1 = Num ** 0.5
print('The square of ', Num, 'is ', Num1, '\n')
n = float(input('Enter number: '))
n2 = math.sqrt(n)
print('The square of ', n, 'is ', n2, '\n')
# Ask a user for a weight in kilograms and converts it to pounds. Note there are about 2.2 pounds in
# a kilogram.
w = int(input('Enter your weight(kg)" '))
w_r = w * 2.2
print('Your weight is ', w_r, 'pounds', '\n')
# Ask the user to input four numbers using three input statements. Create variables called total and
# average that  hold the  sum and  average  of the four  numbers and  print  put the  values  of  total and
# average.
a = list(map(int, input('Enter 4 numbers: ').split()))
total = sum(a)
average = total / 4
print('Total is: ', total, '\n', 'Average is: ', average, '\n')
# Wire a program that ask the user for the price of the meal and the percent tip they want to leave.
# Then print both the tip amount and the total bill with the tip included.
n = int(input('Price of meal(R): '))
w = int(input('%tip: '))
p = w / 100 * n
print('Your tip amount is: R', p, 'Total bill: R', n + p, '\n')
# Write a program that asks the user to enter two numbers, x and y and computes: $$\frac{x-y}{x*y}$$
x = int(input('Input x:'))
y = int(input('Input y:'))
z = x*y
print(math.fabs(x-y)/z, '\n')
# Write a program that asks the user to enter a string. The program should then print the following:
# a. The total number of characters in the string
# b. The string repeated 5 times
# c. The first character of the string
# d. The first four characters of the string
# e. The last four characters of the string
# f. The string backwards
# g. The 6th character of the string if the string
# h. The string with its first and last characters removed
# i. The string in all caps
# j. The string with every ‘a’ replaced with an ‘e’
nn = input('Input string: ')
print(len(nn))
print(nn*5)
print(nn[0])
print(nn[0:4])
print(nn[-1:-5])
print(nn[::-1])
print(nn[5])
print(nn[1:-1])
print(nn.upper())
print(nn.replace('a', 'e'))
