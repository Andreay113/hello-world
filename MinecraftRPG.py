#Made by Tiffany
name = input("What is your name?: ")
print(f"Hello {name}, welcome to Minecraft!")

x = 0
y = 0
play = True
inventory = []
health = 50
health_low = False

while play == True:
    print(f"You are at ({x},{y}) and have {health} health points out of 100.")
    print("How much do you want to move? ")

    # Check x change valid
    # Made by Katya
    change_x = int(input("On the X-axis: "))
    x_proposed = x + change_x
    x_check = True
    while x_check == True:
        if x_proposed > 8 or x_proposed < 0:
            print("Invalid x axis change!! ")
            change_x = int(input("Please enter a different x change "))
            x_proposed = x + change_x
        else:
            x += change_x
            x_check = False

    # Check y change valid
    # Made by Tiffany
    y_check = True
    change_y = int(input("On the Y-axis: "))
    y_proposed = y + change_y
    while y_check == True:
        if y_proposed > 8 or y_proposed < 0:
            print("Invalid y axis change!! ")
            change_y = int(input("Please enter a different y change "))
            y_proposed = y + change_y
        else:
            y += change_y
            y_check = False

# Trees on (1,3) and (3,1)
# hit tree = gain 1 apple and 1 wood
# Made by Andrea
    if (x == 1 and y == 3) or (x == 3 and y == 1):
        tree = int(input("You have found a tree. How many times would you like to hit it? "))
        total_tree = tree
        while tree > 0:
            inventory.append("apple")
            print("You have gained an apple")
            inventory.append("wood")
            print("You have gained a piece of wood")
            tree -= 1
        print(f"You have gained a total of {total_tree} apples and {total_tree} wood.")

# Sheep
# Hit sheep = gain 1 raw beef at (4,7) and (7,4)
# Made by Tiffany
    sheep_farm = input("Do you want to kill the sheep?")
    if sheep_farm.lower() == "n":
        print("You have chosen not to kill the sheep")
    elif sheep_farm.lower() == "y":
        if (x == 4 and y == 7) or (x == 7 and y == 4):
            sheep = int(
                input(
                    "You have found a sheep. How many times would you like to hit it? "
                ))
            total_sheep = sheep
            while sheep > 0:
                inventory.append("raw_beef")
                print("You have gained 1 raw beef")
                sheep -= 1
            print(f"You have gained a total of {total_sheep} raw beefs")

# Zombie drop and attack
# Hit zombie = 10 damage and 1 raw beef at (2,5) and (5,4)
# Made by Andrea
    if (x == 2 and y == 5) or (x == 5 and y == 2):
        zombie = int(
            input("You have found a zombie. How many times would you like to hit it? "))
        total_zombie = zombie
        while zombie > 0:
            inventory.append("raw_beef")
            print("You have gained a 1 raw beef")
            zombie -= 1
            health -= 10
            print(f"You have been hit: your health is now {health}.")
        print(f"You have gained a total of {total_zombie} raw beefs")

# Campfire to cook beef
# Interacting with Campfire allows player to gain 1 cooked beef for 1 raw raw beef and 1 wood at (6,0)
# Made by Andrea
    if x == 6 and y == 0:
        total_beef = 0
        print("You are at a campfire, 1 wood + 1 raw beef = 1 cooked beef")
        cook = input("Would you like to cook your beef y/n ")
        if cook.lower() == "n":
            print("You have chosen not to cook anything")
        elif cook.lower() == "y":
            if "raw_beef" not in inventory:
                print("You have no raw beef to cook")
            elif "wood" not in inventory:
                print("You have no wood to cook your beef with")
            else:
                many_cook = int(input("How many beefs do you want to cook? "))
                while many_cook > 0:
                    inventory.remove("wood")
                    inventory.remove("raw_beef")
                    inventory.append("cooked_beef")
                    print("You have gained 1 cooked beef")
                    total_beef += 1
                    many_cook -= 1
                    if "wood" not in inventory or "raw_beef" not in inventory:
                        if "wood" not in inventory:
                            print("You have no more wood")
                        if "raw_beef" not in inventory:
                            print("You have no more raw beef")
                        break
                print(f"You have gained a total of {total_beef} and loss {total_beef} wood and raw beef")

# Villager
# Upon encounter, player can trade an apple for an emerald. This emerald is used as currency, and can be exchanged at the Healing Fountain in return for maxing out player's health.
    if x == 0 and y == 8:
        total_emeralds = 0
        villager_encounter = input(
            "Ermm. You encountered a villager. Would you like to trade one apple for an emerald? y/n "
        )
        if villager_encounter.lower() == "n":
            print("You chose not to trade with the villager. Maybe next time.")
        if villager_encounter.lower() == "y":
            if "apple" not in inventory:
                print("You have no apples to trade.")
            else:
                many_emeralds = int(
                    input("How many emeralds do you want to trade for? "))
                while many_emeralds > 0:
                    inventory.remove("apple")
                    inventory.append("emerald")
                    print("You have gained one emerald.")
                    total_emeralds += 1
                    many_emeralds -= 1
                    if "apple" not in inventory:
                        print("You have no more apples.")
                        break
                print(
                    f"You have gained {total_emeralds} emeralds and lost {total_emeralds} apples from this interaction."
                )

# Healing fountain
# When the player reaches (7,7), they reach this fountain, which automatically brings the player's health to 100.
# Made by Katya
    if x == 7 and y == 7:
        print("You have reached the Mystical Healing Fountain.")
        heal = input("Would you like to pay one emerald to restore max health? y/n ")
        if heal.lower() == "n":
            print("You chose not to heal.")
        if heal.lower() == "y":
            inventory.remove("emerald")
            health = 100
            print("In place of one emerald, your health is now 100!")

# Death
# When a player's health goes to zero or lower, they die and the game ends.
# Made by Katya
    if health <= 0:
        print("You died. Game over.")
        play = False
# Heal when health is low
# Made by Andrea
    elif health <= 30:
        eat = input("Your health is low would you like to eat y/n ")
        if eat == "n":
            print("You have chosen not to heal")
        elif eat == "y":
            # No food to eat
            if "apple" not in inventory and "cooked_beef" not in inventory:
                print("You do not have any food to eat.")
            else:
                # How much food to eat
                many_apple = int(input("How many apples do you want to eat: "))
                if "apple" not in inventory:
                    print("You have no apples")
                many_beef = int(input("How many beefs do you want to eat: "))
                if "cooked_beef" not in inventory:
                    print("You have no cooked beef")

                # Eat Apples
                while "apple" in inventory and many_apple > 0 and health < 100:
                    inventory.remove("apple")
                    many_apple -= 1
                    health += 10
                    print(f"You ate an apple, your health is now {health}")
                    if "apple" not in inventory:
                        print("You have no more apples")
                        many_apple = 0
                    elif health == 100:
                        print("You are at max health")

                # Eat Beef
                while "cooked_beef" in inventory and many_beef > 0 and health < 100:
                    inventory.remove("cooked_beef")
                    many_beef -= 1
                    health += 20
                    print(f"You ate a cooked beef, your health is now {health}")
                    if "cooked_beef" not in inventory:
                        print("You have no more cooked beef")
                        many_beef = 0
                    elif health >= 100:
                        print("You are at max health")
