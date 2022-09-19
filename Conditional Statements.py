# It is commonly said that one human year is equivalent to 7 dog years. However, this simple conversion fails
# to recognize that dogs reach adulthood in approximately two years. As a result, some people believe that it
# is better to count each of the first two human years as 10.5 dog years, and then count each additional human
# year as 4 dog years.

# Write a program that implements the conversion from human years to dog years described in the previous
# paragraph. Ensure that your program works correctly for conversions of less than two human years and
# for conversions of two or more human years. Your program should display an appropriate error message
# if the user enters a negative number.

# Students wrote a test out of 30 marks. Write a code that will show a student their result (in %) and tells
# them whether they have passed or failed. Make use of if and nested if statements to achieve this
n = int(input("Enter your mark: "))
if n <= 30:
    v = n / 30 * 100
    print("Your marks is: " + str(v) + "%")
    if n < 15:
        print("Failed")
        print("Mark in the 'if' block")
    else:
        print("Passed")
        print("Mark in the 'else' block")
else:
    print("Value out of range")
print('Done')
# Write a program that takes a value of a noise level from a user and determines the type of mechinery
# JackHammer    130dB
# Gas Lawnmower 106dB
# Alarm Clock   70dB
# Quiet Room    40dB
noise = int(input("Input noise level(dB): "))
if noise > 130:
    print('Noise level is greater than 130dB')
elif noise == 130:
    print("This is a Jackhammer")
elif 130 > noise > 106:
    print("Noise level is between Jackhammer and Gas Lawnmower")
elif noise == 106:
    print("This is a Gas Lawnmower")
elif 70 < noise < 106:
    print('Noise level between Alarm Clock and Gas Lawnmower')
elif noise == 70:
    print('This is an Alarm Clock')
elif 70 > noise > 40:
    print('Noise level between Alarm Clock and Quite Room')
elif noise == 40:
    print("This is a Quiet Room")
else:
    print("Value is less than Quiet Room")

# Write a code that takes in a value from a user and determines whether this value is even or odd.
num = int(input("Input Number: "))
if num % 2 == 0:
    print(str(num) + " is even")
else:
    print(str(num) + " is odd")

# Example of a shorthand if-else statement. Used if a single statement is to be executed for both the if and else
# statement
i = int(input("Enter value: "))
print(True) if i % 2 == 0 else print(False)