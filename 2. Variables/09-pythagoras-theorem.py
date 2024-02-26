#User Input

#Thus far, we've only been outputting things to the user, making our programs one-sided and not that fun. Almost every popular website, mobile app, or video game nowadays has both input and output.
#So how do we get input from the user?
#Python uses the input() function to get user input:
username = input('Enter your name: ')
print(username)

#By default, the user input is stored as a text string, which is okay for now.
#But what about when we want to get a number from a user?
#In that case, we would need to wrap an int() around the input() to convert the text string into a number:
age = int(input('What is your age? '))
print(age)

#If you slept through your geometry class, a Pythagorean theorem is the relationship between the three sides of a right triangle. It was named after the Greek philosopher Pythagoras, born around 570 BC.
#Pythagorean equation looks like: c=(a2 + b2)1/2
#The a is the length of a short side.
#The b is the length of another short side.
#The c is the length of the hypotenuse.
#The hypotenuse is the longest side of the right triangle.
#Create a hypotenuse.py program that asks the user for two numbers, a and b, and then calculates the hypotenuse c.
# Write code below 💖
a=int(input('Enter length of a:'))
b=int(input('Enter length of b:'))
c=(a*a+b*b) ** (1/2)
print(c)