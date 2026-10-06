from simulator import ElevatorSimulator

simulation = ElevatorSimulator(total_floors=5)
simulation.add_request(origin=2, destination=5)

simulation.move_one_floor("up")
print("Boarded:", simulation.board_waiting_passengers())

for _ in range(3):
    simulation.move_one_floor("up")

print("Dropped off:", simulation.drop_off_passengers())
print("Current floor:", simulation.elevator.current_floor)
print("Waiting passengers:", len(simulation.waiting_requests))
print("Passengers onboard:", len(simulation.onboard_requests))
