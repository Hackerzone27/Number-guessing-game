import random
def check():
    global x
    y = input("Would u like to play number guessing game? (y/n) ")
    if y.upper() =="Y":
        x = 9
    elif y.upper() == "N":
        x=0
        print(":-( Bye")
    else:
        print (" ")
check()
while x == 9:
    s_number = random.randint(1,20)
    print ("I'm thinking of a number from 1-20")
    for guesses in range(1,7):
        print("take a guess")
        guess = int(input())
        if guess>s_number:
            print("Your guess is to high")
        elif guess<s_number:
            print("your guess is too low")
        else:
            break
    if guess ==s_number:
        print(f"good job you guessed my number in {guesses} guesses.")
    else:
        print (f"Nope, my secret number is {s_number}")
    check()
