
# main.py

# -----------------------------------------------------------
# Auto Driving Car Simulation
# -----------------------------------------------------------
# Console-based simulation of autonomous driving cars.
# Supports:
# - Placing one or multiple cars on a rectangular grid
# - Executing commands step-by-step (L, R, F)
# - Collision detection and logging
# - Restartable simulation loop
# - Aligned with realistic CLI interaction examples
# -----------------------------------------------------------

from car import Car
from engine import run_simulation

def get_field_dimensions():
    while True:
        try:
            dims = input("Please enter the width and height of the simulation field in x y format:\n").strip().split()
            if len(dims) == 2:
                x, y = map(int, dims)
                if x > 0 and y > 0:
                    return x, y
        except ValueError:
            pass
        print("Invalid input. Please enter two positive integers.")

def get_car_input(field_width, field_height):
    name = input("Please enter the name of the car:\n").strip()
    try:
        x, y, direction = input(f"Please enter initial position of car {name} in x y Direction format:\n").strip().split()
        x, y = int(x), int(y)
        direction = direction.upper()
        if direction not in 'NESW' or not (0 <= x < field_width and 0 <= y < field_height):
            raise ValueError
    except ValueError:
        print("Invalid input. Only positions within field and directions N, E, S, W are allowed.")
        return None

    commands = input(f"Please enter the commands for car {name}:\n").strip().upper()
    if not all(c in 'LRF' for c in commands):
        print("Invalid commands. Only L, R, and F are allowed.")
        return None

    return Car(name, x, y, direction, commands)

def main():
    while True:
        print("Welcome to Auto Driving Car Simulation!")
        width, height = get_field_dimensions()
        print(f"You have created a field of {width} x {height}.")

        cars = []

        while True:
            print("Please choose from the following options:\n[1] Add a car to field\n[2] Run simulation")
            action = input().strip()

            if action == '1':
                car = get_car_input(width, height)
                if car:
                    cars.append(car)
                    print("Your current list of cars are:")
                    for c in cars:
                        print(c.full_status())

            elif action == '2':
                if not cars:
                    print("No cars to simulate. Please add at least one car.")
                    continue
                break
            else:
                print("Invalid option. Please select 1 or 2.")

        print("Your current list of cars are:")
        for c in cars:
            print(c.full_status())

        print("After simulation, the result is:")
        results = run_simulation(cars, width, height)
        for line in results:
            print(line)

        print("Please choose from the following options:\n[1] Start over\n[2] Exit")
        followup = input().strip()
        if followup == '2':
            print("Thank you for running the simulation. Goodbye!")
            break
        elif followup != '1':
            print("Invalid input. Exiting by default.")
            break

if __name__ == '__main__':
    main()
