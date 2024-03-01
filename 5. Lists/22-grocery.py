#Lists

#Welcome to a brand new chapter, where we learn about a neat way to store a bunch of data values! 📦 = ⚽️🏀⚾️🥎🏐🏈
# Storing grades in a class

hw_grade1 = 98
hw_grade2 = 87
hw_grade3 = 92
hw_grade4 = 96

quiz_grade1 = 9
quiz_grade2 = 6
quiz_grade3 = 8

#Creating a bunch of variables this way is tedious and error-prone. Can you imagine what it would be like with 1000+ variables?
#Lists are used to store multiple items in a single variable.
#We can rewrite the above code to:
# Storing grades in a class

hw_grades = [98, 87, 92, 96]
quiz_grades = [9, 6, 8]

#list_name = [item1, item2, item3, item4]
#Lists are created using square brackets [ and ]. And the items are separated by , commas.

#More facts about lists:
#- List items allow duplicate values.
#- Lists can have values with different data types.
#- There's no limit to how much data a list can hold.

#Create a grocery.py program that with a grocery list of things that you need to get from the store:

#'🥚 Eggs'
#'🥑 Avocados'
#'🍪 Cookies'
#'🌶 Hot Pepper Jam'
#'🫐 Blueberries'
#'🥦 Broccoli'
#Print out grocery to make sure you got it!
# Write code below 💖
grocery=['🥚 Eggs','🥑 Avocados','🍪 Cookies','🌶️ Hot Pepper Jam','🫐 Blueberries','🥦 Broccoli']
print(grocery)