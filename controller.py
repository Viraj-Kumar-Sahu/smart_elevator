def choose_direction(simulation):
    current_floor = simulation.elevator.current_floor
    target_floors = []

    for request in simulation.waiting_requests:
        target_floors.append(request.origin)

    for request in simulation.onboard_requests:
        target_floors.append(request.destination)

    if not target_floors:
        return None

    nearest_target = min(
        target_floors,
        key=lambda floor: (abs(floor - current_floor), floor),
    )

    print("  [nearest] targets:", target_floors, "-> nearest:", nearest_target)

    if nearest_target > current_floor:
        return "up"

    if nearest_target < current_floor:
        return "down"

    return "stop"


def choose_look_direction(simulation):
    current_floor = simulation.elevator.current_floor
    current_direction = simulation.elevator.direction
    target_floors = []

    for request in simulation.waiting_requests:
        target_floors.append(request.origin)
    for request in simulation.onboard_requests:
        target_floors.append(request.destination)

    if not target_floors:
        return None

    print("  [look] direction:", current_direction, "| targets:", target_floors)
    if current_direction == "up":
        for floor in target_floors:
            if floor > current_floor:
                return "up"

    if current_direction == "down":
        for floor in target_floors:
            if floor < current_floor:
                return "down"

    nearest_target = min(
        target_floors,
        key=lambda floor: (abs(floor - current_floor), floor),
    )

    if nearest_target > current_floor:
        return "up"
    if nearest_target < current_floor:
        return "down"

    return "stop"


def choose_fcfs_direction(simulation):
    current_floor = simulation.elevator.current_floor
    pending = simulation.waiting_requests + simulation.onboard_requests

    if not pending:
        return None

    print("  [fcfs] queue (oldest first):")
    for req in sorted(pending, key=lambda request: request.requested_at):
        if req.boarded_at is None:
            status = "waiting"
        else:
            status = "onboard"
        print("    ", req.origin, "->", req.destination, "|", status)

    oldest = min(pending, key=lambda request: request.requested_at)

    if oldest.boarded_at is None:
        target_floor = oldest.origin
    else:
        target_floor = oldest.destination

    if target_floor > current_floor:
        return "up"
    if target_floor < current_floor:
        return "down"

    return "stop"
