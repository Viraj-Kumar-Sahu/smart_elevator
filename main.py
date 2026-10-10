from simulator import ElevatorSimulator
from controller import choose_direction


simulation = ElevatorSimulator(total_floors=5)
simulation.add_request(origin=2, destination=5)

while simulation.waiting_requests or simulation.onboard_requests:
    simulation.drop_off_passengers()
    simulation.board_waiting_passengers()

    direction = choose_direction(simulation)

    if direction is None:
        break

    if direction == "stop":
        continue

    simulation.move_one_floor(direction)

print("Current floor:", simulation.elevator.current_floor)
print("Waiting passengers:", len(simulation.waiting_requests))
print("Passengers onboard:", len(simulation.onboard_requests))
