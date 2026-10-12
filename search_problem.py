def transition(state, action, requests, total_floors):
    current_floor, statuses = state

    if action == "up":
        next_floor = current_floor + 1
    elif action == "down":
        next_floor = current_floor - 1
    else:
        raise ValueError("Action must be 'up' or 'down'.")

    if not 1 <= next_floor <= total_floors:
        return None

    next_statuses = list(statuses)

    for i, (origin, destination) in enumerate(requests):
        if next_statuses[i] == "W" and origin == next_floor:
            next_statuses[i] = "O"
        elif next_statuses[i] == "O" and destination == next_floor:
            next_statuses[i] = "D"

    return next_floor, tuple(next_statuses)


def get_successors(state, requests, total_floors):
    successors = []

    for action in ("up", "down"):
        next_state = transition(
            state,
            action,
            requests,
            total_floors,
        )
        if next_state is not None:
            successors.append((action, next_state))

    return successors
