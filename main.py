from controller import choose_direction
from simulator import ElevatorSimulator

simulation = ElevatorSimulator(total_floors=5)

simulation.add_request(origin=2, destination=5)
simulation.add_request(origin=4, destination=1)
simulation.add_request(origin=3, destination=1)

while simulation.waiting_requests or simulation.onboard_requests:
    current_floor = simulation.elevator.current_floor

    dropped = simulation.drop_off_passengers()
    boarded = simulation.board_waiting_passengers()

    print(
        "At floor",
        current_floor,
        "- boarded:",
        boarded,
        "- dropped off:",
        dropped,
    )

    direction = choose_direction(simulation)

    if direction is None:
        break

    simulation.move_one_floor(direction)

    print(
        "Controller chose:",
        direction,
        "- moved to floor:",
        simulation.elevator.current_floor,
        "- time:",
        simulation.current_time,
    )

print("Final floor:", simulation.elevator.current_floor)
print("Waiting passengers:", len(simulation.waiting_requests))
print("Passengers onboard:", len(simulation.onboard_requests))

for number, request in enumerate(simulation.completed_requests, start=1):
    print(
        "Completed passenger", number,
        "| route:", request.origin, "to", request.destination,
        "| wait:", request.waiting_time(),
        "| ride:", request.ride_time()
    )

total_wait = 0
total_ride = 0

for request in simulation.completed_requests:
    total_wait += request.waiting_time()
    total_ride += request.ride_time()

completed_count = len(simulation.completed_requests)

if completed_count > 0:
    print("Average waiting time:", total_wait / completed_count)
    print("Average ride time:", total_ride / completed_count)
    print("Average total trip time:", (total_wait + total_ride) / completed_count)
