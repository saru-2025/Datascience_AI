
# engine.py

# -----------------------------------------------------------
# Simulation Engine
# -----------------------------------------------------------
# Handles the progression of commands for each car, step-by-step.
# Also manages:
# - Collision detection at each step
# - Deactivation of collided cars
# - Summary output after simulation
# -----------------------------------------------------------

from car import Car

def run_simulation(cars, width, height):
    # Reset all cars to initial positions
    for car in cars:
        car.reset()

    logs = []
    max_steps = max((len(car.commands) for car in cars), default=0)

    for step in range(max_steps):
        positions = {}
        for car in cars:
            if car.active:
                pos = car.step(width, height)
                positions.setdefault(pos, []).append(car)

        for pos, group in positions.items():
            if len(group) > 1:
                for car in group:
                    if car.active:
                        car.active = False
                        others = [c.name for c in group if c != car]
                        logs.append(f"- {car.name}, collides with {', '.join(others)} at ({pos[0]},{pos[1]}) at step {step + 1}")

    return logs or [car.current_status() for car in cars]
