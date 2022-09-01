# Print a program that computes and prints the results of the equation below.
sub_1 = 94-17
sub_2 = 415-319
div = sub_1/sub_2
print(div, '\n')
# Ask a user to enter a number. Print the square of the number. The output should read “The square
# of _ is _”
Num = int(input("Enter number: "))
Num1 = Num**0.5
print('The square of ', Num, 'is ', Num1, '\n')
import math
n = float(input('Enter number: '))
n2 = math.sqrt(n)
print('The square of ', n, 'is ', n2, '\n')
# Ask a user for a weight in kilograms and converts it to pounds. Note there are about 2.2 pounds in
# a kilogram.
w = int(input('Enter your weight(kg)" '))
w_r = w*2.2
print('Your weight is ', w_r, 'pounds', '\n')
# Ask the user to input four numbers using three input statements. Create variables called total and
# average that  hold the  sum and  average  of the four  numbers and  print  put the  values  of  total and
# average.
a = list(map(int, input('Enter 4 numbers: ').split()))
b = sum(a)
print('Total is ', b, 'Average is: ', b/4, '\n')
