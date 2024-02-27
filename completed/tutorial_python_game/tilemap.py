import random

# Define tile symbols
GRASS = '.'
BLOCK = 'B'
ENEMY = 'E'
PLAYER = 'P'


class TileMap:
    def __init__(self, width, height, block_density, enemy_density):
        self.width = width
        self.height = height
        self.block_density = block_density
        self.enemy_density = enemy_density
        self.map = []

    def generate_tilemap(self):
        # Generate the tilemap
        for y in range(self.height):
            row = []
            for x in range(self.width):
                # Generate blocks
                if x == 0 or x == self.width - 1 or y == 0 or y == self.height - 1 or random.random() < self.block_density:
                    row.append(BLOCK)
                else:
                    row.append(GRASS)
            self.map.append(row)

        # Add enemies
        for _ in range(int(self.width * self.height * self.enemy_density)):
            x = random.randint(1, self.width - 2)
            y = random.randint(1, self.height - 2)
            while self.map[y][x] != GRASS:
                x = random.randint(1, self.width - 2)
                y = random.randint(1, self.height - 2)
            self.map[y][x] = ENEMY

    def add_player(self):
        """Add player to a random grass tile."""
        x = random.randint(1, self.width - 2)
        y = random.randint(1, self.height - 2)
        while self.map[y][x] != GRASS:
            x = random.randint(1, self.width - 2)
            y = random.randint(1, self.height - 2)
        self.map[y][x] = PLAYER

    def print_tilemap(self):
        for row in self.map:
            print(''.join(row))

# Example usage:
# tilemap = TileMap(64, 64, 0.2, 0.02)
# tilemap.generate_tilemap()
# tilemap.add_player()
# tilemap.print_tilemap()
