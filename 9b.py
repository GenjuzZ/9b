import random

class Agent:
    def __init__(self, name, world):
        self.name = name
        self.world = world
        self.x = random.randint(0, world.size-1)
        self.y = random.randint(0, world.size-1)

    def move(self):
        while True:
            new_x = random.randint(0, self.world.size-1)
            new_y = random.randint(0, self.world.size-1)
            if (new_x, new_y) not in self.world.occupied_positions():
                self.x, self.y = new_x, new_y
                break

class World:
    def __init__(self, size, num_agents):
        self.size = size
        self.agents = [Agent(f"Agent{i}", self) for i in range(num_agents)]

    def occupied_positions(self):
        return {(agent.x, agent.y) for agent in self.agents}

def main():
    # Initialize the world with a 5x5 grid and 3 agents
    world = World(5, 3)

    for step in range(10):
        print(f"Step {step}")
        for agent in world.agents:
            agent.move()
            print(f"{agent.name} moved to ({agent.x}, {agent.y})")

if __name__ == "__main__":
    main()
