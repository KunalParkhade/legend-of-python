#Exponents

#Python can also perform exponentiation such as 2³ or 10².
#In written math, we might see an exponent as a superscript number (like above), but typing superscripts isn't always easy on modern keyboards. Since exponentiation is super similar to multiplication, Python uses the notation **.
score = 2 ** 2      # score is 4
score = 2 ** 3      # score is now 8
score = 2 ** 4      # score is now 16
score = 2 ** 5      # score is now 32

print(score)        # Output: 32

#The body mass index (BMI) was created by a Belgian mathematician in the 1850s and it's used by health and nutrition professionals to estimate human body fat in certain populations.
#It is computed by taking an individual's weight (mass) in kilograms and dividing it by the square of their height in meters.
#bmi=mass/(height)2
#Create a bmi.py program that calculates your own BMI.
# Write code below 💖
mass=55
height=1.75
bmi=(mass)/height ** 2
print(bmi)