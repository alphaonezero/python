#TRAVIS THE USELESS SECURITY SYSTEM
known_users=["Alice","Bob","Clair","Dan","Emma","Fred","Georgie","Harry"]

while True:
    print("Hi! My name is Travis!")
    name = input("What is your name?: ").strip().capitalize()

    if name in known_users:
        print("-"*3+"Hello {}!".format(name))
        remove = input("-"*3+"Would you like to be removed from the system? (Y/N): ").strip().lower()
        if remove == "y":
            known_users.remove(name)
            print("-"*3+"You have been removed from the system.")
        elif remove == "n":
            print("-"*3+"No problem, I didn't want you to leave anyways!")
    else:
        print("-"*3+"Hmmmm... I don't think we have met, {}.".format(name))
        add_me = input("-"*3+"Would you like to be added to the system? (Y/N): ").strip().lower()
        if add_me == "y":
            print(known_users)
            known_users.append(name)
            print("-"*3+"Great! You've been added to the system.")
            print(known_users)
        elif add_me == "n":
            print("-"*3+"No worries! I'll see you next time!")
