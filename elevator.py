class Elevator:
    def __init__(self, total_floors, start_floor=1):
        if total_floors < 2:
            raise ValueError("The building must have atleast 2 floors.")
        if not 1 <= start_floor <= total_floors:
            raise ValueError("Start floor is outside the building.")

        self.total_floors = total_floors
        self.current_floor = start_floor
        self.direction = "idle"

    def move(self, direction):
        if direction not in ("up", "down"):
            raise ValueError("Direction must be 'up' or 'down'.")

        step = 1 if direction == "up" else -1
        next_floor = self.current_floor + step

        if not 1 <= next_floor <= self.total_floors:
            return False

        self.current_floor = next_floor
        self.direction = direction
        return True

    def stop(self):
        self.direction = "idle"
