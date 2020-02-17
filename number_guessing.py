import random
n=random.randint(40,50)
print("Number Guessing")
for guesstaken in range(1,99):
	print("\nTake a Guess! ")
	guess=int(input())
	if(guess<n):
		print("Your Guess is low!")
	elif(guess>n):
		print("Your Guess is high!")
	else:
		break

if(guess==n):
	print("Your Guess is correct " + str(guess))
else:
	print("you lose")
	print("The n was "+ str(n))
    
