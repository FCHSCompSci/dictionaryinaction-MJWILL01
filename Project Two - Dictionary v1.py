"""Python Dictionary - Overwatch heroes
Mark Williams
9-24-18"""

import time
import webbrowser

users = {
    'jeffkaplan' : "nerfcy",
    'ryan' : "markisrainin",
    'rainin' : "ryanisryan",
    'sirtaylor' : "iamtaylor",
    'user' : "pass",
    }


ow_heros = {
    'tracer' : {
        'dps' : 3,
        'speed' : 20.0,
        'note' : "fast but don't do much damage"
        },
    'roadhog' : {
        'dps' : 250,
        'speed' : 7.8,
        'note' : "slow but does alot of damage",
        },
    'bastion' : {
        'dps' : 9999,
        'speed' : 0.0,
        'note' : "too much damage : nerf",
        },
    'moira aka. opaf' : {
        'dps' : 9999,
        'speed' : 11.4,
        'note' : "Easy clap when thomas plays her",
        },
    'mercy' : {
        'dps' : 1,
        'speed' : 15.3,
        'note' : "can be op if used properly",
        },
    'reaper' : {
        'dps' : 50,
        'speed' : 9.0,
        'note' : "slow unless reaping",
        },
    'ana' : {
        'dps' : 75,
        'speed' : 8.5,
        'note' : "heals good",
        },
    }


user_input = True
is_on = True

def show_hero():
    print("\n")
    for hero, dps_speed in ow_heros.items():
        length_h = "-"*(len(hero)+1)
        length_space = " "*(len(hero)+2)
        print("\n%s\n%s: \n%s\n"% (length_h, hero.title(), length_h))

        
        for d_s, value in dps_speed.items():
            if type(value) == type(""):
                print("%s%s = %s"% (length_space, d_s.upper(), value.upper()))
                
            else:
                print("%s%s = %s"% (length_space, d_s.upper(), value))
                
    print("\n")
    

def create_hero(new_hero,new_damage,new_speed,new_note):
    # This is adding or updating heroes
    
    new_hero_dict = {
    new_hero : {
        'dps' : new_damage,
        'speed' : new_speed,
        'note' : new_note,
        },
    }
    
    ow_heros.update(new_hero_dict)

    show_hero()


def input_letters(lett):
    
    if lett == "a":
        # Add heroes
        new_hero = input("Who would you like to update or add? ").lower()
        new_damage = input("How much damage per second are they doing? ").lower()
        new_speed = input("How fast are they? ").lower()
        new_note = input("Note's of the hero? ").lower()
        
        create_hero(new_hero,new_damage,new_speed,new_note)
        
                
    elif lett == "r":
        # Removing a hero
        remove = input("What hero would you like to remove? ").lower()
        
        try:
            del ow_heros[remove]
            show_hero()
            
        except:
            print("\nThat's not a hero in Overwatch")
        
    elif lett == "s":
        show_hero()

    elif lett == "w":
        print("Redirecting to website... ")
        time.sleep(1)
        webbrowser.open('https://www.blizzard.com/en-us/')


def ask_for_username():
    return input("Username: ")


def ask_for_password():
    return input("Password: ")


def error_input():
    print("\n===========================")
    print(" Please input a cheesecake!".replace('cheesecake', 'character')) #easter egg
    print("===========================\n")


def full_code():
    while is_on:
        # This asks for input on what to do next

    
        user_input = False
    
        while not type(user_input) == type(""):
            print("\nWhat whould you like to do?")
            user_input = input("(a)dd or update; (r)emove; (s)how heros; or look at the (w)ebsite? or (e)xit ")

            
            try:
                low_str = user_input.lower().strip()[0]
                input_letters(low_str)

                if low_str == "e":
                    # Breaking the while loop
                    break
        
            except:
                error_input()
        if low_str == "e":
            break


while True:
    username = ask_for_username().lower().strip()
    password = ask_for_password().lower().strip()
    
    if username in users:
        if password in users.values():
            print("-------------------------------------------")
            print("           WELCOME, %s!"% (username.upper()))
            print("-------------------------------------------")
            
            full_code()
    


