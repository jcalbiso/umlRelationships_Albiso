# ACTIVITY 3
# Game Character Special Moves

class Warrior:
    def special_move(self):
        print("Warrior swings a mighty sword!")

class Mage:
    def special_move(self):
        print("Mage casts a powerful spell!")

class Archer:
    def special_move(self):
        print("Archer shoots a precise arrow!")


def perform_move(character):
    character.special_move()


characters = [Warrior(), Mage(), Archer()]

for character in characters:
    perform_move(character)


# ACTIVITY 4
# Game Character Potion Use

class HealthPotion:
    def use(self):
        print("You regain 50 HP!")

class ManaPotion:
    def use(self):
        print("You restore 30 MP!")

class SpeedBoost:
    def use(self):
        print("Your speed increases for 10 seconds!")


def apply_item(item):
    item.use()


potions = [HealthPotion(), ManaPotion(), SpeedBoost()]

for item in potions:
    apply_item(item)