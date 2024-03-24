while True:
    name = input("Hello there! What's your name: ")
    if not name.strip():  # Check if the input contains only spaces
        print("Please provide a non-empty name.")
        quit()

    if name.isdigit():  # Check if the input contains only digits
        print("Name cannot be a number.")
        quit()

    print("Welcome", name, "to this amazing adventure!")

    answer = input("You are on a dirty road and this is the end. Do you want to turn to the right or left?(Choose right/left): ").lower()
    if answer == 'left':
        answer = input("You are in a river! You can walk around or swim across. Do you want to walk around or swim across?(Choose walk/swim): ").lower()
        if answer == "walk":
            print("There was a crocodile in the river and you were eaten. You lose!")
            break
        elif answer == "swim":
            print("You have walked for a long period and you are out of water. You lose!")
            break
        else:
            print("Invalid option! You lose")
            break

    elif answer == 'right':
        answer =input("You came across a bridge and it looks wobby. Do you want to cross or go back?(Choose cross/back): ").lower()
        if answer == 'cross':
            answer = input("If you meet with a stranger, will you talk to them?(Yes/No): ").lower()
            if answer == 'yes':
                print("You made the stanger happy and he gave you a gold.")
                print("Congratulations", name, "You Won!")
                break
            elif answer == 'no':
                print("You offended the stranger. You lose!")
                break
            else:
                print("Invalid option! You lose")
                break
        elif answer == 'back':
            print("You gave up. You lose!")
            break
        else:
            print("Invalid option! You lose")
            break
    else:
        print("Invalid option! You lose")
        break
