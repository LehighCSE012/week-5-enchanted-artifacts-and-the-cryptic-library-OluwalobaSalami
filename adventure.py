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
        if artifacts["amulet_of_vitality"]["effect"] == "increases health":
            updated_health = player_stats["player_health"] + artifacts["amulet_of_vitality"]["power"]
            update_dict = {
            "player_health" : updated_health
            }
            player_stats.update(update_dict)
            print(f"The amulet_of_vitality increased your health by {artifacts['amulet_of_vitality']['power']} points!")
            del artifacts["amulet_of_vitality"]
    else:
        print("You found nothing of interest.")

    return player_stats, artifacts
            

def main():
    """Main game loop."""

    dungeon_rooms = [
    ("Dusty library", "key", "puzzle",
    ("Solved puzzle!", "Puzzle unsolved.", -5)),
    ("Narrow passage, creaky floor", "torch", "trap",
    ("Avoided trap!", "Triggered trap!", -10)),
    ("Grand hall, shimmering pool", "healing potion", "none", None),
    ("Small room, locked chest", "treasure", "puzzle",
    ("Cracked code!", "Chest locked.", -5)),
    ("Cryptic Library", None, "library", None)
    ]
    player_stats = {'health': 100, 'attack': 5}
    monster_health = 70
    inventory = []
    clues = set()
    artifacts = {
        "amulet_of_vitality": {
            "description": "Glowing amulet, life force.",
            "power": 15,
            "effect": "increases health"
        },
        "ring_of_strength": {
            "description": "Powerful ring, attack boost.",
            "power": 10,
            "effect": "enhances attack"
        },
        "staff_of_wisdom": {
            "description": "Staff of wisdom, ancient.",
            "power": 5,
            "effect": "solves puzzles"
        }
    }

    has_treasure = random.choice([True, False])
    display_player_status(player_stats)
    player_stats = handle_path_choice(player_stats)
    if player_stats['health'] > 0:
        treasure_obtained_in_combat = combat_encounter(player_stats, monster_health, has_treasure)
        if treasure_obtained_in_combat is not None:
            check_for_treasure(treasure_obtained_in_combat)

        if random.random() < 0.3:
            artifact_keys = list(artifacts.keys())
            if artifact_keys:
                artifact_name = random.choice(artifact_keys)
                player_stats, artifacts = discover_artifact(player_stats, artifacts, artifact_name)
                display_player_status(player_stats)

        if player_stats['health'] > 0:
            player_stats, inventory, clues = enter_dungeon(
                player_stats, inventory, dungeon_rooms, clues)
            print("\n--- Game End ---")
            display_player_status(player_stats)
            print("Final Inventory:")
            display_inventory(inventory)
            print("Clues:")

            if clues:
                for clue in clues:
                    print(f"- {clue}")
            else:
                print("No clues.")
    

if __name__ == "__main__":
    main()
