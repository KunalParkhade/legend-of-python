#Congrats!

#Woohoo! You learned variables in Python! 🙌

#Here's a recap of everything we learned in this chapter:

#Data types: int, float, str, bool.
#Arithmetic operators: +, -, *, /.
#The % modulo finds the remainder.
#The ** exponentiation finds the exponent.
#The input() function is used to get user input.
#The int() function converts a value into an integer number.

#Let's put it all together now!

#We just got home from a trip to South America, specifically Colombia, Peru, and Brazil. There's some leftover cash in:
#🇨🇴 Colombian pesos
#🇵🇪 Peruvian soles
#🇧🇷 Brazilian reais
#Create a currency.py program that asks the user for the amount they have in pesos, soles, and reais and calculates the total in USD.
#Make sure to Google the current exchange rates!
#The output of the program should look like this:
#What do you have left in pesos? 5600
#What do you have left in soles? 105
#What do you have left in reais? 280
#89.6

# Write code below 💖
CO=int(input("What do you have left in pesos?"))
PE=int(input("What do you have left in soles?"))
BR=int(input("What do you have left in reais?"))
x=(CO*0.00025)+(PE*0.26)+(BR*0.20)
print(x)