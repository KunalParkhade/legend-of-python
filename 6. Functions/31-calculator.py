#Return Value#
#We learned that functions can take in inputs, but did you know that functions can also have outputs? In fact, every Python function has an output!
#The return keyword is used to terminate a function and output a value:
#def function_name():
  # The code inside
# return value

#When we don't add it, Python will implicitly return the default value, None, as the return value.
#When we do want to be explicit:
def add(x, y):
  answer = x + y
  return answer

#So a return keyword is added, plus the variable we want to output.
#Now when we call the function, there will be an output that we can play with:
total = add(4.99, 9.99)   # total is 14.98

#Note: When a return statement is reached, Python will stop the execution of the current function, sending a value out to where the function was called.

#Print vs. Return#
#As a rule of thumb:
#-Use return in a function when you want to send value(s) from one point in the code to another.
#-Use print() in a function when you want to display some text to the user.

#Let's try a classic Computer Science project: simple calculator program! 🔢
#Create a calculator.py program and define these five functions:
#-add(a, b) that adds two numbers a and b.
#-subtract(a, b) that subtracts two numbers a and b
#-multiply(a, b) that multiplies two numbers a and b.
#-divide(a, b) that divides two numbers a and b.
#-exp(a, b) that takes a to the exponent (or power) of b.
#Make sure to return the result in each function definition.
#Test your calculator by calling each function once to make sure that it works!

# Write code below 💖
def add(a, b):
  result=a+b
  return result

def subtract(a,b):
  result=a-b
  return result

def multiply(a,b):
  result=a*b
  return result

def divide(a,b):
  result=a/b
  return result

def exp(a,b):
  result=pow(a,b)
  return result

print(add(3,4))
print(subtract(8,1))
print(multiply(7,1))
print(divide(70,10))
print(exp(7,1))