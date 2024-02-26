class Weapon:
    def __init__(self, name: str, weapon_ilvl: int, required_character_level: int, weapon_dps: float,
                 weapon_speed: float, weapon_type: str) -> None:
        self.name = name
        self.weapon_ilvl = weapon_ilvl
        self.required_character_level = required_character_level
        self.weapon_dps = weapon_dps
        self.weapon_speed = weapon_speed
        self.weapon_type = weapon_type


# Default weapon
fists = Weapon("Fists", 1, 0, 1.00, 3.00, "Unarmed")

weapons = [
    Weapon("Big Iron Fishing Pole", 30, 25, 19.00, 3.00, "Fishing Pole"),
    Weapon("Tactician's Staff", 31, 26, 9.29, 3.50, "Staff"),
    Weapon("Silver Hand Training Weapon", 31, 26, 10.44, 3.40, "Two-Handed Mace"),
    Weapon("Ancestral Sword", 31, 26, 10.16, 3.10, "Two-Handed Sword"),
    Weapon("Crusader's Mace", 31, 26, 9.83, 2.90, "One-Handed Mace"),
    Weapon("Skinning Knife", 4, 0, 2.19, 1.60, "Dagger"),
    Weapon("Strong Fishing Pole", 10, 5, 5.67, 3.00, "Fishing Pole"),
    Weapon("Shadow Hunter Knife", 32, 27, 15.59, 1.70, "Dagger"),
    Weapon("Darkwood Fishing Pole", 20, 15, 11.83, 3.00, "Fishing Pole"),
    Weapon("Blacksmith Hammer", 1, 0, 1.25, 2.00, "One-Handed Mace"),
    Weapon("Fishing Pole", 1, 0, 1.00, 3.00, "Fishing Pole"),
    Weapon("Copper Shortsword", 9, 4, 3.81, 2.10, "One-Handed Sword"),
    Weapon("Mining Pick", 4, 14, 1.50, 2.00, "One-Handed Axe"),
    Weapon("Arclight Spanner", 10, 0, 2.71, 2.40, "One-Handed Mace"),
    Weapon("Ryedol's Lucky Pick", 1, 0, 1.00, 1.50, "One-Handed Axe"),
    Weapon("Small Throwing Knife", 3, 0, 1.00, 2.00, "Thrown Weapon"),
    Weapon("Bloody Brass Knuckles", 34, 29, 16.56, 1.60, "Fist Weapon"),
    Weapon("Left-Handed Blades", 35, 30, 17.33, 1.50, "Fist Weapon"),
    Weapon("Smoldering Wand", 20, 15, 13.44, 1.60, "Wand")
]