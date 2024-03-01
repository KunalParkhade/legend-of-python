#Index

#List items are changeable, meaning we can update individual items within a list.
#But before we do that, how can we access an individual item within a list? Well, this is where index comes in!
#An index is an item's position in a list.
#Python is 0-indexed, meaning that the indices starts at 0:
vowels = ['a', 'e', 'i', 'o', 'u']
# Index:   0    1    2    3    4
print(vowels[0])     # Output: a
print(vowels[1])     # Output: e
print(vowels[2])     # Output: i
print(vowels[3])     # Output: o
print(vowels[4])     # Output: u

#Negative Index
#Another thing to note about index is that it can be positive or negative.
#If the index is negative, it starts from -1 (which is the last item of a list) and it goes backwards from there.
vowels = ['a', 'e', 'i', 'o', 'u']
# Index:   0    1    2    3    4
# Index:  -5   -4   -3   -2   -1

#Slicing

#Is there a way to get more than just one individual item? Yep! It's called slicing.
#Slicing is where we can access certain parts of a sequence.
#Instead of accessing an item using a single index like name[index], we can get multiple items by specifying where to start and where to end the range like name[start : end].

vowels = ['a', 'e', 'i', 'o', 'u']

print(vowels[0 : 3])
print(vowels[1 : 3])

# Output:
# ['a', 'e', 'i']
# ['e', 'i']
#It starts from the start index (inclusive) and ends before the end index (non-inclusive). So in the above example, print(vowels[1 : 3]) only returned items at indices 1 and 2, and didn't include index 3.

#IndexError

#There is a common error in Python when dealing with sequences called the IndexError. This is what happens when the index is out of the range of a list.
#For example, when we try to do vowels[5], we will get something like:
#Traceback (most recent call last):
#    print(vowels[5])
#IndexError: list index out of range

#Create a todo.py program that will define a todo list that contains the following items:

#'🏦 Get quarters.'
#'🧺 Do laundry.'
#'🌳 Take a walk.'
#'💈 Get a haircut.'
#'🍵 Make some tea.'
#'💻 Complete Lists chapter.'
#'💖 Call mom.'
#'📺 Watch My Hero Academia.'

#Print the first item and the second item. What did you get?
#Next, use slicing to print the third, fourth, and fifth items.
#Try printing out the item at index 9 to see the IndexError before moving on.

# Write code below 💖
todo=['🏦 Get quarters.','🧺 Do laundry.','🌳 Take a walk.','💈 Get a haircut.','🍵 Make some tea.','💻 Complete Lists chapter.','💖 Call mom.','📺 Watch My Hero Academia.']
print(todo[0])
print(todo[1])
print(todo[2:5])
print(todo[9])