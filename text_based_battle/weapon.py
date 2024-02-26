class Weapon:
    def __init__(self, name: str, weapon_ilvl: int, required_character_level: int, weapon_dps: float,
                 weapon_speed: float, weapon_type: str) -> None:
        self.name = name
        self.weapon_ilvl = weapon_ilvl
        self.required_character_level = required_character_level
        self.weapon_dps = weapon_dps
        self.weapon_speed = weapon_speed
        self.weapon_type = weapon_type


fists = Weapon("Fists", 1, 1, 1, 3, "Unarmed")
big_iron_fishing_pole = Weapon("Big Iron Fishing Pole", 30, 25, 19.00, 3.00, "Fishing Pole")
tacticians_staff = Weapon("Tactician's Staff", 31, 26, 9.29, 3.50, "Staff")
silver_hand_training_hammer = Weapon("Silver Hand Training Weapon", 31, 26, 10.44, 3.40, "Two-Handed Mace")
