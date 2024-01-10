import random
jackpot=random.randint(1,100)
guess= int(input("Chal guess kar koe bhi number: "))
counter=1
while guess != jackpot:
    if guess < jackpot:
        print("Koe Higher Number Soch")
    else:
        print("Koe Lower Number Soch")
    guess= int(input("Chal guess kar koe bhi number: "))
    counter+=1

print("Sahi Uttor")
print("You Took", counter,"Attempts")
