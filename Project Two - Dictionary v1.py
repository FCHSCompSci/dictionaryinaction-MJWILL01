

ow_heros = {
    'tracer' : {
        'dps' : 3,
        'speed' : "fast",
        },
    'roadhog' : {
        'dps' : 250,
        'speed' : "slow",
        },
    'bastion' : {
        'dps' : 9999,
        'speed' : "none",
        },
    }


is_on = True

def show_hero():
    print("\n")
    for hero, dps_speed in ow_heros.items():
        print("%s: "% (hero.title()))
        for d_s, value in dps_speed.items():
            print("%s = %s"% (d_s.upper(), value))

    print("\n")

def add_up():
    # This is adding or updating heroes
    new_hero = input("Who would you like to update or add? ").lower()
    new_damage = input("How much damage per second are they doing? ").lower()
    new_speed = input("How fast are they? ").lower()
    new_hero_dict = {
    new_hero : {
        'dps' : new_damage,
        'speed' : new_speed,
        },
    }
    ow_heros.update(new_hero_dict)

    show_hero()

print("-------------------------------------------")
print("           WELCOME, JEFF KAPLAN")
print("-------------------------------------------")


while is_on:
    # This asks for input on what to do next
    doing = input("\nWhat whould you like to do?\n(a)dd, (r)emove, (u)pdate, or show heros? or (e)xit ")

    do_low_str = doing.lower().strip()[0]

    if do_low_str == "a":
        # Add heroes
        add_up()
                
    if do_low_str == "r":
        # Removing a hero
        remove = input("What hero would you like to remove? ").lower()
        del ow_heros[remove]
        show_hero()

    if do_low_str == "e":
        # Breaking the while loop
        break

    if do_low_str == "u":
        # Update heros
        add_up()

"""NOTE: Adding heroes and removing heroes do the EXACT same thing"""





        
