from elevator import Elevator
from passenger import PassengerRequest


class ElevatorSimulator:
    def __init__(self, total_floors):
        self.elevator = Elevator(total_floors=total_floors)
        self.current_time = 0
        self.waiting_requests = []
        self.onboard_requests = []

    def add_request(self, origin, destination):
        if not 1 <= origin <= self.elevator.total_floors:
            raise ValueError("Origin floor is outside the building.")

        if not 1 <= destination <= self.elevator.total_floors:
            raise ValueError("Destination floor is outside the building.")

        request = PassengerRequest(
            origin=origin,
            destination=destination,
            requested_at=self.current_time,
        )

        self.waiting_requests.append(request)
        return request

    def advance_time(self):
        self.current_time += 1
