
# car.py

# -----------------------------------------------------------
# Car Class Definition
# -----------------------------------------------------------
# Encapsulates the state and behavior of an autonomous car
# in the simulation field, including:
# - Initialization and state reset
# - Directional turns and movement
# - Command processing
# - Status reporting
# -----------------------------------------------------------

LEFT_TURN = {'N': 'W', 'W': 'S', 'S': 'E', 'E': 'N'}
RIGHT_TURN = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}
MOVE_STEP = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}

class Car:
    def __init__(self, name, x, y, direction, commands):
        self.name = name
        self.x = x
        self.y = y
        self.direction = direction
        self.commands = commands
        self.start_position = (x, y, direction)
        self.current_index = 0
        self.active = True  # Determines if car is still moving

    def reset(self):
        # Resets the car to its initial position and state
        self.x, self.y, self.direction = self.start_position
        self.current_index = 0
        self.active = True

    def step(self, max_x, max_y):
        # Executes one command if still active
        if not self.active or self.current_index >= len(self.commands):
            return (self.x, self.y)

        cmd = self.commands[self.current_index]
        self.current_index += 1

        if cmd == 'L':
            self.direction = LEFT_TURN[self.direction]
        elif cmd == 'R':
            self.direction = RIGHT_TURN[self.direction]
        elif cmd == 'F':
            dx, dy = MOVE_STEP[self.direction]
            new_x, new_y = self.x + dx, self.y + dy
            if 0 <= new_x < max_x and 0 <= new_y < max_y:
                self.x, self.y = new_x, new_y

        return (self.x, self.y)

    def current_status(self):
        # Provides current location and direction
        return f"- {self.name}, ({self.x},{self.y}) {self.direction}"

    def full_status(self):
        # Shows initial setup and command sequence
        sx, sy, sd = self.start_position
        return f"- {self.name}, ({sx},{sy}) {sd}, {self.commands}"
