class PassengerRequest:
    def __init__(self, request_id, origin, destination, requested_at=0):
        if origin == destination:
            raise ValueError("Origin and destination must be different.")

        self.request_id = request_id
        self.origin = origin
        self.destination = destination
        if destination > origin:
            self.direction = "up"
        else:
            self.direction = "down"
        self.requested_at = requested_at
        self.boarded_at = None
        self.completed_at = None

    def waiting_time(self):
        if self.boarded_at is None:
            return None

        return self.boarded_at - self.requested_at

    def ride_time(self):
        if self.boarded_at is None or self.completed_at is None:
            return None

        return self.completed_at - self.boarded_at
