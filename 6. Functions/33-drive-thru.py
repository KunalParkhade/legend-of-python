#Congratulations! You now know how functions work. This is a concept that trips up a lot of people, so definitely practice and practice. 💪
#In this chapter, we learned:
#The "Don't Repeat Yourself" methodology.
#We've been using built-in functions like print() and input() all along.
#How to define and call a function — the two-step process.
#Inputs with parameters and arguments.
#Output with the return keyword.
#Function scope vs. global scope.
#Here's the function skeleton one more time, just in case you forget!

#def function_name(parameter1, parameter2):
  # The code inside
  #return value

#Now that you know how functions work, let's create one last one!

#When you go to a drive-thru like McDonald's, you can order food using the item numbers. For example, a Happy Meal might be a #3!

#Create a drive_thru.py program with your favorite fast food chain's menu.
#Define a get_item() function that takes in one parameter, the number of the item you want to order, and returns the name of that item!
#For example, if you called the function with:
#Argument value 1, it could return '🍔 Cheeseburger'.
#Argument value 2, it could return '🍟 Fries'.
#Argument value 3, it could return '🥤 Soda'.
#Argument value 4, it could return '🍦 Ice Cream'.
#Argument value 5, it could return '🍪 Cookie'.
#Make sure to call this function a few times to make sure that it works!
#Lastly, let's do the following:
#Create a welcome menu and put that in a welcome() function.
#Create a main program that takes in user input with input().

def welcome():
    print("Welcome to MyFavorite Fast Food Chain!")
    print("Here is our menu:")
    print("1. 🍔 Cheeseburger")
    print("2. 🍟 Fries")
    print("3. 🥤 Soda")
    print("4. 🍦 Ice Cream")
    print("5. 🍪 Cookie")

def get_item(item_number):
    menu = {
        1: '🍔 Cheeseburger',
        2: '🍟 Fries',
        3: '🥤 Soda',
        4: '🍦 Ice Cream',
        5: '🍪 Cookie'
    }
    return menu.get(item_number, "Invalid item number")

def main():
    welcome()
    while True:
        try:
            item_number = int(input("Please enter the number of the item you want to order (1-5): "))
            if 1 <= item_number <= 5:
                item = get_item(item_number)
                print(f"You ordered: {item}")
            else:
                print("Invalid item number. Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
