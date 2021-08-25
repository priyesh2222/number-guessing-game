print("number guessing")
import random
winning_no=random.randint(0,100)
guess=1
game_over=False
num=int(input("enter the guess "))
while not game_over:
    if num==winning_no:
        print(f"u win u guessed in {guess} times")
        game_over=True
    else:
        if num<winning_no:
            print("too low")
            guess+=1
        else:
            print("too high")
            guess+=1
        
        num=int(input("enter the guess "))
        