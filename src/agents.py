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
}

class MetricAgent(Agent):
    """Individual Agent definition and its properties/interaction methods."""

    def __init__(
            self,
            model,
            initial_state,
            bot_spread_chance,
            human_spread_chance,
    ):
        
        super().__init__(model)
        
        self.state = initial_state
        self.bot_spread_chance = bot_spread_chance  
        self.human_spread_chance = human_spread_chance 
        self.gain_resistance_chance = 0.05 
        
        # Human starting with a random topic
        if self.state == State.HUMAN:
            self.first_topic = random.choice(list(TOPICS.keys()))  
            self.topic = self.first_topic
        
        # Bots chooses a random topic
        if self.state == State.BOT:
            self.topic = random.choice(list(TOPICS.keys()))

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
        """Humans engage with topic"""
        if self.state == State.HUMAN:
            self.topic = topic

    
    def try_to_activate(self, topic):
        """Activate the inactive bot"""
        if self.state == State.INACTIVE_BOT:
            self.state = State.BOT
            self.topic = topic

    def try_gain_resistance(self):
        """Humans can revert back to their original topic"""
        if self.state == State.HUMAN and self.random.random() < self.gain_resistance_chance:
            self.topic = self.first_topic

    def step(self):
        self.try_to_infect_neighbors()
        self.try_gain_resistance()
