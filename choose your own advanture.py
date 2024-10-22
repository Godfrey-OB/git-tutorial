name = input("Enter you name: ")
print(f"you are welcome {name} to this adventue!")

answer = input(f"{name} your straigth road has come to an end! which way do you want to go? left or right? ").lower()

if answer == "left":
    answer = input(f"{name} you have choosen a river road, you can walk around it or swin accross it: ")
    
    if answer == "swim":
        print(f"{name} you swam accross and were eaten by an Alligator. ")
        
    elif answer == "walk":
        print(f"{name} you walked for many miles, ran out of water and lost the game.")
        
    else:
        print("Not a valid Option. you lose")
        
elif answer == "right":
    answer = input(f"{name} you have come to an unsteady bridge, do you want to cross it or head back? (cross/back)? ")
    
    if answer == "back":
        print(f"{name} you got back and lost. pls try again ")
        
    elif answer == "cross":
        answer = input(f"{name} you just crossed and met strangers. Do you want to talk to them? (yes/no)? ")
        
        if answer == "yes":
            print(f"{name} you talked to the strangers and was given Gold. You win!")
        
        elif answer == "no":
            print(f"{name} you ignored the strangers and was attacked, you lose!")
            
        else:
            print("Not a valid Option. you lose")
            
    else:
        print("Not a valid Option. you lose")
else:
    print("Not a valid Option. you lose")
    
print(f"Thank you for trying {name}")