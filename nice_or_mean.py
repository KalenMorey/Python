


def start(nice=0,mean=0,name=""):
    name = describe_game(name)
    nice,mean,name = nice_mean(nice,mean,name)



def describe_game(name):

    if name != "":
        print("\nThank you for playing again, {}!".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = input("\nWhat is your name? ").capitalize()
                if name !="":
                    print ("\nWelcome, {}!".format(name))
                    print("\nIn this game, you will be greeted by a dog. \nYou can be nice or be mean")
                    print("your fate awaits you")
                    stop = False
    return name


def nice_mean(nice,mean,name):
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick = input("\nA dog approaches you. \nHe lookes scared. \nWill you be nice or mean n/m:" ).lower()
        if pick == "n":
            print("You pet the dog, and his tail wags. You made a best friend!")
            nice = (nice + 1)
            stop = False
        if pick == "m":
            print("\nThe dog snarls at you, and runs away...")
            mean = (mean + 1)
            stop = False
    score(nice,mean,name)


def show_score(nice,mean, name):
    print("\n{}, you currently have ({}, Nice) and ({}Mean) points.".format(name,nice,mean))    


def score(nice,mean,name):
    if nice > 5:
        win(nice,mean,name)
    if mean > 5:
        lose(nice,mean,name)
    else:
        nice_mean(nice,mean,name)


def win(nice,mean,name):
    print("\n You're AMAZING! {}, you won!!! \n You have agreat personality!".format(name))
    again(nice,mean,name)


def lose(nice,mean,name):
    print("\nYou were very mean! \nGAME OVER!!!!!!".format(name)) 


def again(nice,mean,name):
    stop = True
    while stop:
        choice = input("\nDo you want to play again? y/n: ").lower()
        if choice == "y":
            stop = False
            reset(nice,mean,name)
        if choice == "n":
            print("\n See you again soon!")
            stop = False
            exit()
        else:
            print("\nPlease enter 'y' for 'YES', 'n' for 'NO'")


def reset(nice,mean,name):
    nice = 0
    mean = 0
    start(nice,mean,name)


    
if __name__== "__main__":
    start()
