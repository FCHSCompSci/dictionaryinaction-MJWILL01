import time

users = {
    'jeffkaplan' : "nerfcy",
    'ryan' : "markisrainin",
    'rainin' : "ryanisryan",
    'sirtaylor' : "iamtaylor",
    }


ow_heros = {
    'tracer' : {
        'dps' : 3,
        'speed' : "fast",
        'note' : "fast but don't do much damage"
        },
    'roadhog' : {
        'dps' : 250,
        'speed' : "slow",
        'note' : "slow but does alot of damage",
        },
    'bastion' : {
        'dps' : 9999,
        'speed' : "none",
        'note' : "too much damage : nerf",
        },
    'moira aka. opaf' : {
        'dps' : 9999,
        'speed' : "fast when invisible",
        'note' : "Easy clap when thomas plays her",
        },
    'mercy' : {
        'dps' : 1,
        'speed' : "fast",
        'note' : "can be op if used properly",
        },
    'reaper' : {
        'dps' : 50,
        'speed' : "slow",
        'note' : "slow unless reaping",
        },
    'ana' : {
        'dps' : 75,
        'speed' : "slow",
        'note' : "heals good",
        },
    }


doing = True
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

def create_hero():
    # This is adding or updating heroes
    new_hero = input("Who would you like to update or add? ").lower()
    new_damage = input("How much damage per second are they doing? ").lower()
    new_speed = input("How fast are they? ").lower()
    new_note = input("Note's of the hero? ").lower()
    
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
        create_hero()
        
                
    elif lett == "r":
        # Removing a hero
        remove = input("What hero would you like to remove? ").lower()
        try:
            del ow_heros[remove]
            show_hero()
        except:
            print("\nThat's not a hero in Overwatch")
        

    elif lett == "u":
        # Update heros
        create_hero()
        

    elif lett == "s":
        show_hero()


def ask_for_username():
    return input("Username: ")

def ask_for_password():
    return input("Password: ")




while True:
    username = ask_for_username().lower().strip()
    password = ask_for_password().lower().strip()
    
    if username in users:
        if password in users.values():
            print("-------------------------------------------")
            print("           WELCOME, %s!"% (username.upper()))
            print("-------------------------------------------")

            while is_on:
            # This asks for input on what to do next

    
                doing = False
    
                while not type(doing) == type(""):
                    doing = input("\nWhat whould you like to do?\n(a)dd, (r)emove, (u)pdate, or (s)how heros? or (e)xit ")

                try:
                    do_low_str = doing.lower().strip()[0]
                    input_letters(do_low_str)

                    if do_low_str == "e":
                        # Breaking the while loop
                        break
        
                except:
                    print("\n===========================")
                    print(" Please input a cheesecake!".replace('cheesecake', 'character')) #easter egg
                    print("===========================\n")
                    
        else:
            pass
    else:
        pass
    


"""NOTE: Adding heroes and removing heroes do the EXACT same thing"""





        
