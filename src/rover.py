class Rover:
    """
    Represents a rover navigating a rectangular plateau.
    Handles movement and direction changes.
    """
    directions = ['N', 'E', 'S', 'W']

    move_map = {
        'N': (0, 1),
        'E': (1, 0),
        'S': (0, -1),
        'W': (-1, 0)
    }

    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    def turn_left(self):

        idx = Rover.directions.index(self.direction)
        self.direction = Rover.directions[(idx - 1) % 4]

    def turn_right(self):
        idx = Rover.directions.index(self.direction)
        self.direction = Rover.directions[(idx + 1) % 4]


    # Move rover forward only if within plateau boundaries
    def move(self):
        dx, dy = Rover.move_map[self.direction]
        new_x = self.x + dx
        new_y = self.y + dy
        if 0 <= new_x <= self.plateau_x and 0 <= new_y <= self.plateau_y:
            self.x = new_x
            self.y = new_y

    def execute(self, commands):
        if cmd not in ['L','R','M']:
            raise ValueError("Invalid command")
        
        else:
            for cmd in commands:
                if cmd == 'L':
                    self.turn_left()
                elif cmd == 'R':
                    self.turn_right()
                elif cmd == 'M':
                    self.move()

    def get_position(self):
        return f"{self.x} {self.y} {self.direction}"