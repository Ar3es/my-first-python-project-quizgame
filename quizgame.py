name = input("what is your name? ")
print("welcome to my computer quiz,", name)

playing = input("Do you want to play a game? ").lower()
if playing != "yes":
    print("sad to hear that")
    quit()
else:
    print("okay, lets begin the game", name)

score = 0

answer = input("What does cpu stand for? ").lower()
if answer == "central processing unit":
    print("correct")
    score +=1
else:
    print("incorrect")

answer = input("what does gpu stand for? ").lower()
if answer == "graphics processing unit":
    print("correct")
    score +=1
else:
    print("incorrect")

answer = input("what does ram stand for? ")
if answer.lower() == "random access memory":
    print("correct")
    score +=1
else:
    print("incorrect")

print("your score is " + str(score))
print("you have answered " + str((score / 4) * 100) + "% of the questions")