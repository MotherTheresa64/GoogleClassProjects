# Defeat_Evil_Wizard
# Noah Ragan 3/18/2025

import random  # Importing the random module to generate random numbers for damage

# Base Character class (Parent class)
class Character:
    def __init__(self, name, health, attack_power):
        # Constructor initializes the character's name, health, attack power, and max health
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  # Store the maximum health for the character

    # Method to attack an opponent
    def attack(self, opponent):
        # Randomize the damage within a range (attack_power - 5 to attack_power + 5)
        damage = random.randint(self.attack_power - 5, self.attack_power + 5)  
        opponent.health -= damage  # Reduce the opponent's health by the damage
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")  # Print the attack details
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")  # If the opponent's health reaches 0 or below, they are defeated

    # Method to display the character's current stats (health and attack power)
    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

    # Method to heal the character (restores health)
    def heal(self):
        heal_amount = 20  # Amount of health restored
        self.health = min(self.health + heal_amount, self.max_health)  # Ensure health doesn't exceed max health
        print(f"{self.name} heals for {heal_amount} health! Current health: {self.health}")

# Warrior class (inherits from Character, a specialized character)
class Warrior(Character):
    def __init__(self, name):
        # Initialize Warrior with more health and attack power
        super().__init__(name, health=140, attack_power=25)

    # Warrior's special ability: Power Attack (double attack power)
    def power_attack(self, opponent):
        damage = self.attack_power * 2  # Power Attack doubles the attack power
        opponent.health -= damage  # Reduce the opponent's health by the damage
        print(f"{self.name} uses Power Attack on {opponent.name} for {damage} damage!")

# Mage class (inherits from Character, a specialized character)
class Mage(Character):
    def __init__(self, name):
        # Initialize Mage with less health but higher attack power
        super().__init__(name, health=100, attack_power=35)

    # Mage's special ability: Cast Spell (randomized spell damage)
    def cast_spell(self, opponent):
        damage = random.randint(self.attack_power - 5, self.attack_power + 10)  # Randomized damage for the spell
        opponent.health -= damage  # Reduce the opponent's health by the damage
        print(f"{self.name} casts a spell on {opponent.name} for {damage} damage!")

# Archer class (inherits from Character, a specialized character)
class Archer(Character):
    def __init__(self, name):
        # Initialize Archer with moderate health and attack power
        super().__init__(name, health=120, attack_power=30)

    # Archer's special ability: Quick Shot (double attack power)
    def quick_shot(self, opponent):
        damage = self.attack_power * 2  # Quick Shot doubles the attack power
        opponent.health -= damage  # Reduce the opponent's health by the damage
        print(f"{self.name} uses Quick Shot on {opponent.name} for {damage} damage!")

    # Archer's special ability: Evade (next attack will be avoided)
    def evade(self):
        print(f"{self.name} evades the next attack!")  # Print that the next attack will be avoided
        return True  # This will be handled in the battle system

# Paladin class (inherits from Character, a specialized character)
class Paladin(Character):
    def __init__(self, name):
        # Initialize Paladin with more health but lower attack power
        super().__init__(name, health=160, attack_power=20)

    # Paladin's special ability: Holy Strike (bonus damage)
    def holy_strike(self, opponent):
        damage = self.attack_power * 1.5  # Holy Strike gives bonus damage
        opponent.health -= damage  # Reduce the opponent's health by the damage
        print(f"{self.name} uses Holy Strike on {opponent.name} for {damage} damage!")

    # Paladin's special ability: Divine Shield (blocks the next attack)
    def divine_shield(self):
        print(f"{self.name} activates Divine Shield! The next attack will be blocked.")  # Inform that next attack will be blocked
        return True  # This will be handled in the battle system

# Evil Wizard class (inherits from Character, the main enemy)
class EvilWizard(Character):
    def __init__(self, name):
        # Initialize the Evil Wizard with a lot of health but low attack power
        super().__init__(name, health=150, attack_power=15)

    # Evil Wizard's ability to regenerate health over time
    def regenerate(self):
        self.health += 5  # Regenerate 5 health points
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")

# Function to create a player character based on user input
def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer") 
    print("4. Paladin")  

    # Get the player's choice of character class
    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")  # Ask for the player's name

    # Create the corresponding character based on the player's choice
    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)
    elif class_choice == '4':
        return Paladin(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")  # Default to Warrior if invalid choice
        return Warrior(name)

# Battle function: handles the turn-based gameplay
def battle(player, wizard):
    shield_active = False  # Track if Divine Shield is active
    evade_active = False   # Track if Evade is active

    while wizard.health > 0 and player.health > 0:
        # Display available actions to the player
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")

        # Get the player's choice of action
        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)  # Player attacks the wizard
        elif choice == '2':
            # Use special abilities based on the character type
            if isinstance(player, Warrior):
                print("1. Power Attack")
                ability_choice = input("Choose an ability: ")
                if ability_choice == '1':
                    player.power_attack(wizard)
            elif isinstance(player, Mage):
                print("1. Cast Spell")
                ability_choice = input("Choose an ability: ")
                if ability_choice == '1':
                    player.cast_spell(wizard)
            elif isinstance(player, Archer):
                print("1. Quick Shot")
                print("2. Evade")
                ability_choice = input("Choose an ability: ")
                if ability_choice == '1':
                    player.quick_shot(wizard)
                elif ability_choice == '2':
                    evade_active = True  # Activate evasion for the next attack
                    player.evade()
            elif isinstance(player, Paladin):
                print("1. Holy Strike")
                print("2. Divine Shield")
                ability_choice = input("Choose an ability: ")
                if ability_choice == '1':
                    player.holy_strike(wizard)
                elif ability_choice == '2':
                    shield_active = True  # Activate Divine Shield for the next attack
                    player.divine_shield()
        elif choice == '3':
            player.heal()  # Heal the player
        elif choice == '4':
            player.display_stats()  # Display the player's stats
        else:
            print("Invalid choice. Try again.")  # Handle invalid choice

        # Evil Wizard's turn: regenerate and attack the player
        if wizard.health > 0:
            wizard.regenerate()  # Wizard regenerates health

            # If Evade is active, the player avoids the wizard's attack
            if evade_active:
                print(f"{player.name} evades the wizard's attack!")
                evade_active = False  # Reset evade after use
            else:
                wizard.attack(player)  # Wizard attacks the player

        # Check if the player has been defeated
        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break

    # End of battle: check if the wizard is defeated
    if wizard.health <= 0:
        print(f"The wizard {wizard.name} has been defeated by {player.name}!")

# Main function to run the game
def main():
    player = create_character()  # Create the player character
    wizard = EvilWizard("The Dark Wizard")  # Create the Evil Wizard
    battle(player, wizard)  # Start the battle

# Run the main function if the script is executed
if __name__ == "__main__":
    main()
