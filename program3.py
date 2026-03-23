def move_towards_goal(position, goal):
    while position < goal:
        position += 1
        print(f"Current Position: {position}")
    print("Reached the goal!")

initial_position = 0
goal_position = 5

move_towards_goal(initial_position, goal_position)
