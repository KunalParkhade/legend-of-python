#While Loop

#Imagine you're at a party where the DJ plays your favorite song.
#You start dancing when the DJ says, "Keep dancing as long as you're having fun!" 
#That's like a while loop in coding. 
#You keep grooving (executing the code) as long as you're enjoying the music (the condition is true). 
#But unlike just dancing once when your favorite song comes on (like an if statement), you keep dancing until the party's over or you decide to stop.

#while condition:
  # code inside

#In other words, instead of executing once if a condition is true, it executes again and again while that condition is true.
#Here, we have a while loop that asks the user to guess a number:
#guess = 0

#while guess != 6:
#  guess = int(input('Guess the number: '))

#Guess the number: 5
#Guess the number: 3
#Guess the number: 6

#The program sets the variable guess to 0 and enters a while loop. Inside the loop, it checks if the current value of guess is not equal to 6. If true, it executes the code inside the loop and updates the value of guess. This process continues until guess equals 6, at which point the loop terminates and the program moves on.
#Note: If the condition is False from the get-go, then the code block wouldn't run at all and will be skipped.

#Let's continue on from the code above.
#Create a guess.py program and type in the following:
guess = 0
tries=0

while guess != 6 and tries<7:
  guess = int(input("Guess the number:  "))

print("You got it!")

#Let's make it so that it's the same guessing game, but there is a new limit to the number of tries (it was infinite before).
#First, introduce a variable called tries at the top and give it a value of 0.
#Then, add the tries variable to the while loop using a relational operator (like you did with guess).