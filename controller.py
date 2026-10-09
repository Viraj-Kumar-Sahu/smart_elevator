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

    if nearest_target > current_floor:
        return "up"

    if nearest_target < current_floor:
        return "down"

    return "stop"
