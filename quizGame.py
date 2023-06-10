print("Welcome to my Quiz Game")

playing = input("Do you wish to play? ")

if playing.lower() != "yes":
    quit()
    
print("Let's Start")
score = 0

answer = input("What is the name of our planet? ")

if answer.lower() == "earth":
    print("Correct")
    score += 2
else:
    print("Incorrect!")
    
answer = input("What is the orange part of an egg called? ")

if answer.lower() == "york":
    print("Correct")
    score += 2
else:
    print("Incorrect!")
    
answer = input("What is the main part of Computer? ")

if answer.lower() == "cpu":
    print("Correct")
    score += 2
else:
    print("Incorrect!")
    
print("Your Score is " + str(score) + " out of 6")
print("Thank you for playing!")