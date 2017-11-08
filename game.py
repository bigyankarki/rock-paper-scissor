from random import randint


def assign_value(a):
    return {
        1: 'rock',
        2: 'paper',
        3: 'scissor'
    }[a]


def replay():
    while True:
        try:
            user_choice = input("Enter Yes to play again. Enter No to exit. ").lower()
            assert user_choice == "yes" or user_choice == "no"
        except AssertionError:
            print("I could not read your choice.")
            continue
        else:
            break

    if user_choice == "yes":
        run()
    else:
        exit()


def run():
    # get the user input.
    while True:
        try:
            user_choice = input("Rock Paper or Scissor? Whats your choice? ").lower()
            assert user_choice == "rock" or user_choice == "paper" or user_choice == "scissor"
        except AssertionError:
            print("I could not read your choice.")
            continue
        else:
            break

    # get the computer's choice.
    ran = randint(1, 3)
    comp_choice = assign_value(ran)
    print(comp_choice)

    # compare the results
    if user_choice == comp_choice:
        print("We have a draw,")
        replay()

    elif user_choice == "rock" and comp_choice == "scissor":
        print("You chose {0}. Computer chose {1}. Hurray!! You won!".format(user_choice, comp_choice))
    elif user_choice == "paper" and comp_choice == "rock":
        print("You chose {0}. Computer chose {1}. Hurray!! You won!".format(user_choice, comp_choice))
    elif user_choice == "scissor" and comp_choice == "paper":
        print("You chose {0}. Computer chose {1}. Hurray!! You won!".format(user_choice, comp_choice))
    else:
        print("You chose {0}. Computer chose {1}. Sorry!! Computer won!".format(user_choice, comp_choice))


if __name__ == '__main__':
    run()
