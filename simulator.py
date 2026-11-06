from elevator import Elevator
from passenger import PassengerRequest


class ElevatorSimulator:
    def __init__(self, total_floors, dwell_time=1):
        self.elevator = Elevator(total_floors=total_floors)
        self.current_time = 0
        self.dwell_time = dwell_time
        self.waiting_requests = []
        self.onboard_requests = []
        self.completed_requests = []
        self.next_request_id = 1

    def add_request(self, origin, destination):
        if not 1 <= origin <= self.elevator.total_floors:
            raise ValueError("Origin floor is outside the building.")

        if not 1 <= destination <= self.elevator.total_floors:
            raise ValueError("Destination floor is outside the building.")

        request = PassengerRequest(
            request_id=self.next_request_id,
            origin=origin,
            destination=destination,
            requested_at=self.current_time,
        )
        self.next_request_id += 1

        self.waiting_requests.append(request)
        return request

    def advance_time(self):
        self.current_time += 1

    def wait_at_floor(self):
        for _ in range(self.dwell_time):
            self.advance_time()

    def move_one_floor(self, direction):
        moved = self.elevator.move(direction)
        if moved:
            self.advance_time()
        return moved

    def board_waiting_passengers(self):
        boarded_count = 0
        current_floor = self.elevator.current_floor

        for request in self.waiting_requests[:]:
            if request.origin == current_floor:
                self.waiting_requests.remove(request)
                request.boarded_at = self.current_time
                self.onboard_requests.append(request)
                boarded_count += 1

        return boarded_count

    def drop_off_passengers(self):
        dropped_off_count = 0
        current_floor = self.elevator.current_floor

        for request in self.onboard_requests[:]:
            if request.destination == current_floor:
                request.completed_at = self.current_time
                self.completed_requests.append(request)
                self.onboard_requests.remove(request)
                dropped_off_count += 1

        return dropped_off_count
