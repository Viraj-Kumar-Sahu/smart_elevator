from elevator import Elevator
from passenger import PassengerRequest
from simulator import ElevatorSimulator

elevator = Elevator(total_floors=5, start_floor=1)

elevator.move("up")
elevator.move("up")

print("Floor:", elevator.current_floor)
print("Direction:", elevator.direction)

elevator.stop()
print("After stopping:", elevator.direction)

request = PassengerRequest(
    origin=2,
    destination=5,
    requested_at=3,
)

print("Passenger wants to go from", request.origin, "to", request.destination)
print("Waiting time at time 8:", request.waiting_time(current_time=8))

simulation = ElevatorSimulator(total_floors=5)
simulation.add_request(origin=2, destination=5)
simulation.advance_time()
simulation.advance_time()

request = simulation.waiting_requests[0]

print("Current time:", simulation.current_time)
print("Passenger wait:", request.waiting_time(simulation.current_time))
