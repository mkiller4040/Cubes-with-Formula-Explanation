
import math

print("How can you use (a+b)^3 to solve the cubes of real whole numbers ?")
print("Now as you may or may not know, (a+b)^3 simplifies to a^3 + 3a^2b + 3ab^2 + b^3. ")
print("Let's take a number, say 215, to cube.")
print("How would we use this with (a+b)^3 ?")
print("Well we can split our number 215 into 2 parts to get our 'a' value and 'b' value.")
print('For example, we could split 215 into 200 and 15, so the "a" value would be 200')
print('and the "b" value would be 15.')
print("215^3 is the same as (200 + 15)^3 ")
print('Now we can plug in the "a" value, 200 and "b" value, 15, into the simplified version of (a+b)^3')
print('which is a^3 + 3a^2b + 3ab^2 + b^3')
print('Plugging it in would result in : ')
print('(200)^3 + 3(200^2)(15) + 3(200)(15^2) + (15)^3')
print('= 8,000,000 + 2(40,000)(15) + 600(225) + 15^3')
print('= 8,000,000 + 2(40,000)(15) + 600(225) + 15^3')

val = input("Enter number here :")



print("The number you want to cube is", val)
print("Think of two numbers to split your number into.")
print("For example : 210 = 200 (1st number) + 10 (2nd number)")

x = input("Enter the 1st number :")
y = input("Enter the 2nd number :")

def formuala(x, y):
    x_cubed = math.pow(float(x), 3)
    x_squared = math.pow(float(x), 2)
    y_cubed = math.pow(float(y), 3)
    y_squared = math.pow(float(y), 2)

    ans = float(x_cubed) + float(3*(float(x_squared)*float(y))) + float(3*(float(x)*float(y_squared))) + float(y_cubed)

    return ans

print(formuala(x, y))