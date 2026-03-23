
class RationalAgent:
    def __init__(self, goal):
        self.position = 0
        self.goal = goal
    
    def move_towards_goal(self):
        while self.position < self.goal:
            self.position += 1
            print(f"Current Position: {self.position}")
        print("Reached the goal!")

goal_position = 5

agent = RationalAgent(goal_position)

agent.move_towards_goal()
