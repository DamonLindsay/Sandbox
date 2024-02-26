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

big_iron_fishing_pole = Weapon("Big Iron Fishing Pole", 30, 25, 19.00, 3.00, "Fishing Pole")
tacticians_staff = Weapon("Tactician's Staff", 31, 26, 9.29, 3.50, "Staff")
silver_hand_training_hammer = Weapon("Silver Hand Training Weapon", 31, 26, 10.44, 3.40, "Two-Handed Mace")
ancestral_sword = Weapon("Ancestral Sword", 31, 26, 10.16, 3.10, "Two-Handed Sword")
crusaders_mace = Weapon("Crusader's Mace", 31, 26, 9.83, 2.90, "One-Handed Mace")
skinning_knife = Weapon("Skinning Knife", 4, 0, 2.19, 1.60, "Dagger")
strong_fishing_pole = Weapon("Strong Fishing Pole", 10, 5, 5.67, 3.00, "Fishing Pole")
shadow_hunter_knife = Weapon("Shadow Hunter Knife", 32, 27, 15.59, 1.70, "Dagger")
darkwood_fishing_pole = Weapon("Darkwood Fishing Pole", 20, 15, 11.83, 3.00, "Fishing Pole")
blacksmith_hammer = Weapon("Blacksmith Hammer", 1, 0, 1.25, 2.00, "One-Handed Mace")
fishing_pole = Weapon("Fishing Pole", 1, 0, 1.00, 3.00, "Fishing Pole")
copper_shortsword = Weapon("Copper Shortsword", 9, 4, 3.81, 2.10, "One-Handed Sword")
mining_pick = Weapon("Mining Pick", 4, 14, 1.50, 2.00, "One-Handed Axe")
arclight_spanner = Weapon("Arclight Spanner", 10, 0, 2.71, 2.40, "One-Handed Mace")
ryedols_lucky_pick = Weapon("Ryedol's Lucky Pick", 1, 0, 1.00, 1.50, "One-Handed Axe")
small_throwing_knife = Weapon("Small Throwing Knife", 3, 0, 1.00, 2.00, "Thrown Weapon")
bloody_brass_knuckles = Weapon("Bloody Brass Knuckles", 34, 29, 16.56, 1.60, "Fist Weapon")
left_handed_blades = Weapon("Left-Handed Blades", 35, 30, 17.33, 1.50, "Fist Weapon")
smoldering_wand = Weapon("Smoldering Wand", 20, 15, 13.44, 1.60, "Wand")
