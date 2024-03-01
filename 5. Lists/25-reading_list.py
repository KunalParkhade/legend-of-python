#List Methods

#Here are some of them:
#.append() method adds an item to the end of the list.
#.insert() method adds an item to a specific index.
#.remove() method removes an item from a list based on the value.
#.pop() method removes the item at a particular index.

#Let's use DNA sequences as an example for this! 🧬
dna = ['AUG', 'AUC', 'UCG']

dna.append('UAA')     # ['AUG', 'AUC', 'UCG', 'UAA']
dna.insert(2, 'GAU')  # ['AUG', 'AUC', 'GAU', 'UCG', 'UAA']
dna.remove('AUC')     # ['AUG', 'GAU', 'UCG', 'UAA']
dna.pop(0)            # ['GAU', 'UCG', 'UAA']

#The difference between built-in functions and methods on a list is that methods use the dot notation syntax on the list variable we create. Built-in functions can be called by themselves, but methods are always attached to a list variable from which they are being called.
#Another notable difference is that while not all the built-in functions are defined to work with lists, the list methods only work with lists.

#Let's start a book club by making a list of tech startup books! 📚
#Create a reading_list.py program that stores the following items in a books list:
'Zero to One'
'The Lean Startup'
'The Mom Test'
'Make It Stick'
'Life in Code'

#Suppose we want to add one more book to the list: 'Zero to Sold'. Can you use a list method to do so?
#Let's say we finished reading 'Zero to One' and 'The Lean Startup'. Can you use the .remove() method to remove one and the .pop() method to remove the other?
#Print the updated list out to make sure everything's good to go!

# Write code below 💖
books=['Zero to One','The Lean Startup','The Mom Test','Make It Stick','Life in Code']
books.append('Zero to Sold')
books.remove('Zero to One')
books.pop(0)
print(books)