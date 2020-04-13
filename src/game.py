from os import system, name
from time import sleep
import random

rooms = ["Engine Room", "Bridge", "Crew Quarters", "Meal Room"]
has_key = False
has_hat = False
has_talked_to_captain = False
has_talked_to_security_commander = False
has_talked_to_bartender_about_hat = False
secret_password = random.randint(10, 99)


def my_print(statement, newline=True):
    for character in statement:
        print(character, end="", flush=True)
        sleep(.02)
    if newline:
        print()
    sleep(.15)


def intro():
    my_print("Welcome to the space explorer USS-1092, it's really cold out here!")
    my_print("How are you adventurer? Can you rescue us from certain death?")
    my_print("Yesterday, our main warp drives failed, and we can't get into the engine room to fix it.")
    my_print("Can you help us fix it?")
    room_select()


def room_select():
    my_print("Choose a room from the following options:")
    choice = display_choices(rooms)

    if choice == 1:
        engine_room()
    elif choice == 2:
        bridge()
    elif choice == 3:
        crew_quarters()
    elif choice == 4:
        meal_room()


def engine_room():
    clear()
    if not has_key:
        my_print("The door is locked...")
        room_select()
    else:
        my_print("You open the engine room!")
        my_print("Everyone on the ship is super grateful, and the space ship is restored!")
        my_print("The USS-1092 can explore the galaxy once again!")


def bridge():
    global has_talked_to_captain, has_talked_to_security_commander
    clear()
    my_print("You've made it to the bridge.")
    my_print("The security commander is asking for the secret password...")
    sleep(1)
    my_print("[Security Commander] What is the secret password? ", newline=False)
    password = input()
    if password == str(secret_password):
        my_print("[Security Commander] Ok, you can talk to the captain now")
        sleep(3)
        my_print("[Captain] Hello! How can I help you?")
        sleep(1)
        my_print("." * 100)
        sleep(1)
        my_print("[Captain] What's that? You need the key to the engine room?")
        sleep(.5)
        my_print("[Captain] We actually can't find it either! Try seeing if the bartender knows anything.")
        has_talked_to_captain = True
    else:
        my_print("[Security Commander] You can't be in here!")
        my_print("[Security Commander] Come back when you have the password!")
        sleep(1)
        my_print("[Security Commander] ........ The bartender might give it to you if you're smart!")
    has_talked_to_security_commander = True
    sleep(2)
    room_select()


def crew_quarters():
    global has_hat
    clear()
    my_print("You've entered the crew quarters")
    my_print("What do you want to do?")
    choices = ["Go to another room", "Take a nap"]
    if has_talked_to_bartender_about_hat:
        choices.append("Grab a hat")
    choice = display_choices(choices)
    if choice == 1:
        room_select()
    elif choice == 2:
        my_print("zZZz" * 125)
        sleep(2)
        my_print("That was a nice nap!")
        sleep(2)
        crew_quarters()
    elif choice == 3:
        my_print("You grabbed the hat!")
        sleep(1)
        has_hat = True
        crew_quarters()


def meal_room():
    clear()
    my_print("You've entered the meal room")
    my_print("Some strange people hanging out here...")
    my_print("What do you want to do?")
    choice = display_choices(["Go to another room", "Talk to the bartender", "Eat a meal"])
    if choice == 1:
        room_select()
    elif choice == 2:
        bartender()
    else:
        my_print("What a great meal!")
        sleep(2)
        meal_room()


def bartender():
    global has_key, has_talked_to_bartender_about_hat
    clear()
    my_print("[Bartender] What do you want?")
    choices = [
        "I'd like a daquiri!",
        "Nothing, nevermind"
    ]
    if has_talked_to_security_commander:
        choices.append("I've heard something about you knowing the secret password to the bridge, can you tell me more?")
    if has_talked_to_captain:
        choices.append("Ask about the engine room")
    choice = display_choices(choices)
    if choice == 1:
        my_print("[Bartender] Sure thing! Enjoy!")
    elif choice == 2:
        my_print("[Bartender] No problem, have a good day!")
    elif choice == 3:
        if not has_hat:
            my_print("[Bartender] Ok, I'll help you out, but I forgot to get my hat")
            my_print("[Bartender] Can you get it from the crew quarters?")
            my_print("[Bartender] Then I'll help you...")
            has_talked_to_bartender_about_hat = True
        else:
            my_print("[Bartender] Thanks for grabbing my hat!")
            sleep(1)
            my_print("." * 40)
            sleep(1)
            my_print("[Bartender] What's that? You still want the secret password?")
            sleep(.5)
            my_print("." * 10)
            sleep(1)
            my_print("[Bartender] Ok fine, I'll help you.")
            sleep(.5)
            my_print("[Bartender] Ok, the secret password is a number.")
            my_print("[Bartender] The password's first digit is %d" % (secret_password // 10))
            if secret_password % 3 == 0:
                my_print("[Bartender] The password is divisible by 3")
            if secret_password % 4 == 0:
                my_print("[Bartender] The password is divisible by 4")
            my_print("[Bartender] I am also going to give you three tries to guess the secret password")
            guesses = 0
            while guesses <= 3:
                try:
                    my_print("[Bartender] What's your guess? ", newline=False)
                    guess = int(input())
                    if guess == secret_password:
                        my_print("[Bartender] Wow! You got it! The secret password was indeed %d!" % secret_password)
                        break
                    elif guess > secret_password:
                        my_print("[Bartender] Not it! The secret password is smaller!")
                    else:
                        my_print("[Bartender] Not it! The secret password is bigger!")

                except ValueError:
                    my_print("[Bartender] That was not even a number!")
                guesses += 1
            my_print("[Bartender] Good luck finishing your quest!")
    elif choice == 4:
        my_print("[Bartender] What's that? You know about the engine room?")
        my_print("[Bartender] I'll tell you what, you can have the key!")
        my_print("[Bartender] I was bound to be found out eventually, but I'm taking the escape pod!")
        sleep(2)
        print()
        my_print("You now have the engine room key!")
        has_key = True
    sleep(2)
    meal_room()


def display_choices(choices):
    try:
        for i in range(1, len(choices) + 1):
            my_print(str(i) + ") " + choices[i - 1])
        my_print("Enter your choice: ", newline=False)
        choice = int(input())
        if choice > len(choices):
            my_print("That is not a valid option! Try again.")
            return display_choices(choices)
        return choice
    except ValueError:
        my_print("That is not a valid option! Try again.")
        return display_choices(choices)


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


intro()
