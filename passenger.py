class PassengerRequest:
    def __init__(self, origin, destination, requested_at=0):
        if origin == destination:
            raise ValueError("Origin and destination must be different.")

        self.origin = origin
        self.destination = destination
        self.requested_at = requested_at

    def waiting_time(self, current_time):
        return current_time - self.requested_at
