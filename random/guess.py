import random


number = random.randint(1,10)

print("Try to guess a number from 1-10 that I'm thinking of")

guess = input()

while guess != number:
	if guess < number:
		print("Nope, try a higher number")
		guess = input()
	elif guess > number:
		print("Try lower")
		guess = input()
	if guess == number:
		print("Yes! " + str(number) + ", is the correct number!")