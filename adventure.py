import random

def enter_dungeon(player_stats, inventory, dungeon_rooms, clues):
    """
    this goes through different rooms
    """
    player_health = player_stats['health']
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
            updated_player_health = player_health + room[3][2]
            if updated_player_health < 0:
                updated_player_health = 0
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
            updated_player_health = player_health + room[3][2]
            if updated_player_health < 0:
                updated_player_health = 0
                print("You are barely alive!")

        elif room[2] == "library":
            clue_list = ["The treasure is hidden where the dragon sleeps.", 
                        "The key lies with the gnome.", 
                        "Beware the shadows.", 
                        "The amulet unlocks the final door."
                        ]
            samples = random.sample(clue_list, 2)
            for clue in samples:
                find_clue(clues, clue)
            if "staff_of_wisdom" in inventory:
                print("You understand the meaning of the clues and can now bypass a puzzle challenge in one of the other rooms.")

        elif room[2] == "none":
            print("There doesn't seem to be a challenge in this room. You move on.")
        display_inventory(inventory)

    print(f"Your current health: {updated_player_health}")
    updated_dict = {"health" : updated_player_health}
    """Updating player health"""
    player_stats.update(updated_dict)
    return player_stats, inventory, clues

def find_clue(clues, new_clue):
    """This is for clues."""
    if new_clue in clues:
        print("You already know this clue.")
    else:
        """add new clue"""
        clues.add(new_clue)
        print(f"You discovered a new clue: {[new_clue]}")
    return clues

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

def display_player_status(player_stats):
    """This displays player status"""
    player_health = player_stats['health']
    print(f"Your current health: {player_health}")
    player_attack = player_stats['attack']
    print(f"Your current attack: {player_attack}")

def handle_path_choice(player_stats):
    """This is for the choice to go left or right"""
    player_health = player_stats['health']
    path = random.choice(["left", "right"])
    if path == "left":
        print("You encounter a friendly gnome who heals you for 10 health points.")
        updated_player_health = player_health + 10
        if updated_player_health > 100:
            updated_player_health = 100
    else:
        print("You fall into a pit and lose 15 health points")
        updated_player_health = player_health - 15
        if updated_player_health <= 0:
            updated_player_health = 0
            print("You are barely alive!")
    update_dict = {'health' : updated_player_health}
    player_stats.update(update_dict)
    return player_stats

def player_attack(monster_health):
    """This is for the player attack"""
    print("You strike the monster for 15 damage!")
    updated_monster_health = monster_health - 15
    return updated_monster_health

def monster_attack(player_health):
    """This is for the monster attack"""
    critical_hit_chance = random.random()
    if critical_hit_chance >= 0.5:
        updated_player_health = player_health - 10
        print("The monster hits you for 10 damage!")
    else:
        updated_player_health = player_health - 20
        print("The monster lands a critical hit for 20 damage!")
    return updated_player_health

def combat_encounter(player_stats, monster_health, has_treasure):
    """This is for the combat loop with the player and the monster"""
    player_health = player_stats['health']
    while player_health > 0 and monster_health > 0:
        monster_health = player_attack(monster_health)
        display_player_status(player_stats)
        if monster_health <= 0:
            print("You defeated the monster!")
            return has_treasure
        player_health = monster_attack(player_health)
        if player_health <= 0:
            print("Game over!")
            return False

def check_for_treasure(has_treasure):
    """This is to check for treasure"""
    if has_treasure:
        print("You found the hidden treasure! You win!")
    else:
        print("The monster did not have the treasure. You continue your journey.")

def discover_artifact(player_stats, artifacts, artifact_name):
    """This is for artifacts."""
    if artifact_name:
        print(artifact_name)
        if artifacts[artifact_name]["effect"] == "increases health":
            updated_health = player_stats["health"] + artifacts[artifact_name]["power"]
            update_dict = {
            'health' : updated_health
            }
            player_stats.update(update_dict)
            print(f"The amulet_of_vitality increased your health by {artifacts[artifact_name]['power']} points!")
            del artifacts["amulet_of_vitality"]
        if artifacts[artifact_name]["effect"] == "enhances attack":
            updated_attack = player_stats["attack"] + artifacts[artifact_name]["power"]
            update_dict = {
            'attack' : updated_attack
            }
            player_stats.update(update_dict)
            print(f"The ring of power enhanced your attack by {artifacts[artifact_name]['power']} points!")
            del artifacts["ring_of_power"]
    else:
        print("You found nothing of interest.")

    return player_stats, artifacts
            
def main():
    """Main game loop."""

    dungeon_rooms = [
    ("Dusty library", "key", "puzzle",("Solved puzzle!", "Puzzle unsolved.", -5)),
    ("Narrow passage, creaky floor", "torch", "trap",("Avoided trap!", "Triggered trap!", -10)),
    ("Grand hall, shimmering pool", "healing potion", "none", None),
    ("Small room, locked chest", "treasure", "puzzle",("Cracked code!", "Chest locked.", -5)),
    ("A vast library filled with ancient, cryptic texts", None, "library", None)
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
            #allows us to view the dictionary
            artifact_keys = list(artifacts.keys())
            if artifact_keys:
                artifact_name = random.choice(artifact_keys)
                player_stats, artifacts = discover_artifact(player_stats, artifacts, artifact_name)
                display_player_status(player_stats)

        if player_stats['health'] > 0:
            player_stats, inventory, clues = enter_dungeon(player_stats, inventory, dungeon_rooms, clues)
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
