from enum import Enum
from mesa import Agent
import random

class State(Enum):
    HUMAN = 0  
    BOT = 1 
    INACTIVE_BOT = 2 


TOPICS = {
    "Topic 1": "orange", 
    "Topic 2": "Blue", 
    "Topic 3": "purple",
    "Topic 4": "red", 
    "Topic 5": "pink",
    "Topic 6": "green" 

}

class MetricAgent(Agent):
    """Individual Agent definition and its properties/interaction methods."""    
    
    def __init__(
          self,
          model,
          initial_state,
          bot_spread_chance,
          human_spread_chance
        ):

            super().__init__(model)
            
            self.state =initial_state
            self.bot_spread_chance= bot_spread_chance
            self.human_spread_chance = human_spread_chance
            self.tolerance = {topic: 0 for topic in TOPICS.keys()}

            if self.state == State.HUMAN:
                self.first_topic = random.choice(list(TOPICS.keys()))
                self.topic = self.first_topic

            if self.state==State.BOT:
                self.topic = model.bot_topic

    def try_to_infect_neighbors(self):
        """Bots influence humans and activate inactive bots. Humans can influence other Humans as well"""
        for agent in self.model.grid.get_neighbors(self.pos, include_center=False):
            if self.state == State.BOT:
                if agent.state == State.HUMAN and self.random.random() < self.bot_spread_chance:
                    agent.try_to_engage(self.topic)
                if agent.state == State.INACTIVE_BOT and self.random.random() < 0.4:
                    agent.try_to_activate(self.topic)
            elif self.state == State.HUMAN:
                if agent.state == State.HUMAN and self.random.random() < self.human_spread_chance:
                    agent.try_to_engage(self.topic)

    def try_to_engage(self, topic):
        """Humans gain tolerance and stop engaging with topic after a while"""
        if self.state == State.HUMAN:
            self.tolerance[topic] = self.tolerance[topic] + 1 
            if self.tolerance[topic] < 30:
                self.topic = topic
            else:
                self.topic = self.first_topic 

    def try_to_activate(self, topic):
        """Activate the follower bot"""
        if self.state ==State.INACTIVE_BOT:
            self.state =State.BOT
            self.topic = topic

    def step(self):
        self.try_to_infect_neighbors()