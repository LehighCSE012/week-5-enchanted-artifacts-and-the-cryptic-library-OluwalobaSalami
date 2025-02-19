import random

def enter_dungeon(player_health, inventory, dungeon_rooms):
    """
    this goes through different rooms
    """
    for room in dungeon_rooms:
        print(room[0])
        if room[1]:
            acquire_item(inventory, room[1])
        if room[2] == "puzzle":
            print("You encounter a puzzle!")
            choice = input("Solve or skip? ")
            if choice.lower() == "solve":
                puzzle_outcome = random.choice([True, False])
                if puzzle_outcome:
                    print(room[3][0])
                else:
                    print(room[3][1])
                    #Updating player health
            player_health += room[3][2]
            if player_health < 0:
                player_health = 0
                print("You are barely alive!")

        elif room[2] == "trap":
            print("You see a potential trap!")
            choice_2 = input("Disarm or bypass? ")
            if choice_2.lower() == "disarm":
                trap_outcome = random.choice([True, False])
                if trap_outcome:
                    print(room[3][0])
                else:
                    print(room[3][1])
                    #Updating player health
            player_health += room[3][2]
            if player_health < 0:
                player_health = 0
                print("You are barely alive!")
        elif room[2] == "none":
            print("There doesn't seem to be a challenge in this room. You move on.")
        display_inventory(inventory)
    print(f"Your current health: {player_health}")
    return player_health, inventory

def acquire_item(inventory, item):
    """
    #to add an item to the list
    """
    inventory.append(item)
    print(f"You acquired a {item}!")
    return inventory

def display_inventory(inventory):
    """
    #this displays the inventory
    """
    if len(inventory) == 0:
        print("Your inventory is empty.")
    else:
        print("Your inventory:")
        for item in inventory:
            #to get the items position in the list
            print(f"{inventory.index(item) + 1}. {item}")

def discover_artifact(player_stats, artifacts, artifact_name):
    if artifact_name:
        print(artifact_name)
        if artifacts["amulelet_of_vitality"]["effect"] == "increases health":
            update_health = player_stats[player_health][]
            update_dict = {
            "player_health" = update_health
            }
            

def main():
    """
    main function
    """
    player_stats = {
    "player_health" : 100
    }
    inventory = []
    dungeon_rooms = [
    ("A dusty old library", "key", "puzzle", ("You solved the puzzle!", "The puzzle remains unsolved.", -5)),
    ("A narrow passage with a creaky floor", None, "trap", ("You skillfully avoid the trap!", "You triggered a trap!", -10)),
    ("A grand hall with a shimmering pool", "healing potion", "none", None),
    ("A small room with a locked chest", "treasure", "puzzle", ("You cracked the code!", "The chest remains stubbornly locked.", -5))
    ]

    artifacts = {
    "amulet_of_vitality": {
        "description": "A glowing amulet that enhances your life force.",
        "power": 15,
        "effect": "increases health"
    },
    "ring_of_strength": {
        "description": "A powerful ring that boosts your attack damage.",
        "power": 10,
        "effect": "enhances attack"
    },
    "staff_of_wisdom": {
        "description": "A staff imbued with ancient wisdom.",
        "power": 5,
        "effect": "solves puzzles"
    }
}

    enter_dungeon(player_health, inventory, dungeon_rooms)

if __name__ == "__main__":
    main()
