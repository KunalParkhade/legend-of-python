#If Statement

#An if statement is used to test a condition for truth:
#If the condition evaluates to True, code in the if part is executed.
#If the condition evaluates to False, code is skipped.

#if condition:
  # code inside

#if grade > 60:
#  print("You passed!")

#The code "inside" the if statement must be indented (preferably 2 spaces).

#Else
#An else clause can be optionally added to an if statement.
#If the condition evaluates to True, code in the if part is executed.
#If the condition evaluates to False, code in the else part is executed.

#if grade > 60:
#  print("You passed.")
#else:
#  print("You failed.")

#The code "inside" the else clause must also be indented.


#Holy moly, because the class's average was super low on the test, the teacher just added a curve for the test grades! 😭
#Create a grades.py program that checks whether a grade is above or below 55.
#Start by creating a variable called grade and give it a value between 0-100.
#Write a if/else statement for the following:
#If grade is greater than or equal to 55, then print "You passed."
#Else, print "You failed."
#After you run the code, change grade's value and rerun it. Do this a few times to make sure it's working as intended.

# Write code below 💖
grade = 95

if grade >= 55:
  print('You passed.')
else:
  print('You failed.')