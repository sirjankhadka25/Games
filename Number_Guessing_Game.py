import random
def number_guessing_game():
    print("Number Between: ")
    a,b=int(input("Low: ")), int(input("High: "))
    count=0
    number_of_guesses=0
    while True:
        guess= int(input(f"Enter your Guess between {a} and {b} :"))
        random_number=random.randint(a,b)
        if guess==random_number:
            count+=1
            print("You Got It")
            print("Number of wins= {count} and Number of Guess= {number_of_guess}")
            number_of_guesses+=1
            continue_or_not=input("Do you want to continue(y/n): ")
            if continue_or_not=="y":
                continue
            elif continue_or_not=="n":
                break
            
        elif guess<a or guess>b:
            print("Out of Range!!!")
            continue
        else:
            print("Try Again!!!")
            number_of_guesses+=1
            continue
        
    print("Count: ")    
    print(count)
    print("Number of Guess: ")
    print(number_of_guesses)

number_guessing_game()