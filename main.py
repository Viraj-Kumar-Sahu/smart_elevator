from elevator import Elevator

elevator = Elevator(total_floors=5, start_floor=1)

elevator.move("up")
elevator.move("up")

print("Floor:", elevator.current_floor)
print("Direction:", elevator.direction)

elevator.stop()
print("After stopping:", elevator.direction)
