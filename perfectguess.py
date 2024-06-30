import random

x = random.randint(1, 100) 

b = -1

no_of_guesses = 1

print("Guess a number between 1 and 100.")

while(b != x):
    b = int(input("Guess the number: ")) 
    if(b >x):
        print("Lower number please")
        no_of_guesses +=1
    elif(b<x):
        print("Higher number Please")
        no_of_guesses +=1

print(f"congratulations! You have guessed the number {x} correctly in {no_of_guesses} attempts")

if(no_of_guesses==1 or no_of_guesses==2):
    print("Wow! Your guess is so perfect.")
elif(no_of_guesses<=5):
    print("Nice! You are good at guessing.")
elif(no_of_guesses<=10 and no_of_guesses>5):
    print("Your guessing ability is average.")
elif(no_of_guesses>10):
    print("Your guessing ability needs to be improved.")


      

