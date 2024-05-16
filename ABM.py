# Lizzy Diaz

from numpy import random

params = {'world_size':(10,10),
          'num_agents':10}

class Agents():
    def __init__(self, world):
        self.world = world
        self.location = None
    def move(self):
        # move to random spot 
        vacancies = self.world.find_vacant(return_all=True)
        for patch in vacancies:
            self.world.grid[self.location] = None #move out of current patch
            self.location = patch                 #assign new patch to myself
            self.world.grid[patch] = self         #update the grid
    

class World():
    def __init__(self, params):
        # stores grid as a container of some sort
        # calculates how many agents
        # initializes agents in starting locations
        assert(params['world_size'][0] * params['world_size'][1] > params['num_agents']), 'Grid too small for number of agents.'
        self.params = params
        self.grid   = self.build_grid(params['world_size'])
        self.agents = self.build_agents(params['num_agents'])
        self.init_world()

    def build_grid(self, world_size):
        # sets up world agents can move in, returning a dict
        """create the world that the agents can move around on"""
        locations = [(i,j) for i in range(world_size[0]) for j in range(world_size[1])]
        return {l:None for l in locations}
    def build_agents(self, num_agents):
        # generations list of agents to be iterated over
        agents = [Agents(self) for i in range(num_agents)]
        random.shuffle(agents)
        return agents
    def init_world(self):
        #set up starting conditions of world
        for agent in self.agents:
            loc = self.find_vacant()
            self.grid[loc] = agent
            agent.location = loc
            # ????????????
    def find_vacant(self, return_all=False):
        # find list of empty patches and return empty one
        empties = [loc for loc, occupant in self.grid.items() if occupant is None]
        if return_all:
            return empties
        else:
            choice_index = random.choice(range(len(empties)))
            return empties[choice_index]
world = World(params)

# move - find an empty spot and go
# world where agents shuffle around randomly 
