#"Don't Repeat Yourself" (DRY) is like tidying up your room - you wouldn't want to keep picking up the same toys over and over again, right? 
# In software development, it means not writing the same code multiple times. 
# Instead, you put that code in a function, like a magic box that does a specific job. 
# Then, whenever you need that job done, you just call the function by its name, and it does the work for you. 
# It's like having a handy helper that saves you from doing the same task again and again, making your code cleaner and saving you time in the long run.

#Built-in functions are 68 functions that come with the Python interpreter available for use. Here are some that you might recognize:
#print()
#input()
#len()
#We've used them before, but didn't get into how they work behind the scenes.
#And that's okay! This is the beautiful part about built-in functions. Like a car, you don't need to know what's underneath the hood to operate it.
#Let's look at some built-in Python functions!

#Create a dry.py program and check out the complete list of built-in functions:
#Find 4 built-in functions that we have used previously in the course.
#Pick 1 built-in function that we have not seen before.
#Use each of these once in the program.
#For the new function, try to read the documentation (😵‍💫) or Google it (👍)!
#Add a comment for each built-in function to explain how they work.

# Write code below 💖

# dry.py

# Built-in functions we've used previously
# 1. len(): Returns the length (the number of items) of an object.
string_length = len("Hello, world!")
print("Length of the string:", string_length)

# 2. range(): Returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.
for i in range(5):
    print(i, end=' ')
print()  # For newline

# 3. int(): Returns an integer object constructed from a number or a string.
num_str = "42"
num_int = int(num_str)
print("Integer conversion of string '42':", num_int)

# 4. str(): Returns a string version of the object.
num_float = 3.14
num_str = str(num_float)
print("String conversion of float 3.14:", num_str)


# A built-in function we haven't seen before
# 5. max(): Returns the largest item in an iterable or the largest of two or more arguments.
numbers = [1, 5, 3, 9, 7]
max_number = max(numbers)
print("Maximum number in the list:", max_number)
