import random
import networkx as nx
import mesa
from mesa import Model
from mesa.space import NetworkGrid
from mesa.datacollection import DataCollector
from agents import MetricAgent, State, TOPICS


def number_topic(model, topic):
    return sum(1 for a in model.grid.get_all_cell_contents() if a.state == State.HUMAN and a.topic == topic
    )


class MetricNetwork(Model):
    def __init__(
        self,
        num_nodes=30,
        active_bot=2,
        inactive_bot=3,
        bot_spread_chance=0.5,
        human_spread_chance=0.3,
        algorithm_spread_chance=0.2,
    ):
        super().__init__()

        self.bot_spread_chance = bot_spread_chance
        self.human_spread_chance = human_spread_chance
        self.algorithm_spread_chance = algorithm_spread_chance  

        # Create the network graph
        graph = nx.erdos_renyi_graph(n=num_nodes, p=0.1)
        self.grid = NetworkGrid(graph)

        def get_topic(topic):
            def func(m):
                return number_topic(m, topic)
            return func

        self.datacollector = DataCollector({
            topic: get_topic(topic)
            for topic in TOPICS.keys()
        })


        self.bot_topic = None

        """Create all agents and place them in the network"""
        for node in graph.nodes():
            a = MetricAgent(self, State.HUMAN, self.bot_spread_chance, self.human_spread_chance)
            self.grid.place_agent(a, node)

        self.bot_nodes = self.random.sample(list(graph.nodes), active_bot)
        for a in self.grid.get_cell_list_contents(self.bot_nodes):
            a.state = State.BOT

        self.inactive_bot_nodes = self.random.sample(
            [n for n in graph.nodes() if n not in self.bot_nodes], inactive_bot
        )
        for a in self.grid.get_cell_list_contents(self.inactive_bot_nodes):
            a.state = State.INACTIVE_BOT

        self.connect_bots(graph)

        self.running = True
        self.datacollector.collect(self)

    def connect_bots(self, graph):
        """Connect an inactive bot to an active bot"""
        for inactive_node in self.inactive_bot_nodes:
            connected_bots = [
                b for b in graph.neighbors(inactive_node)
                if b in self.bot_nodes
            ]
            if not connected_bots:
                p_bot = self.random.choice(self.bot_nodes)
                graph.add_edge(inactive_node, p_bot)

    def choose_topic(self):
        """Choose a random topic"""
        return self.random.choice(list(TOPICS.keys()))

    def step(self):
        if self.bot_topic is None:
            self.bot_topic = self.choose_topic()

            for a in self.grid.get_cell_list_contents(self.bot_nodes + self.inactive_bot_nodes):
                a.topic = self.bot_topic

        self.algorithm_topic = self.bot_topic

        if self.bot_topic is not None and self.algorithm_spread_chance > 0:
            for agent in self.grid.get_all_cell_contents():
                if agent.state == State.HUMAN:
                    if random.random() < self.algorithm_spread_chance:
                        agent.try_to_engage(self.bot_topic)
                        
        self.agents.shuffle_do("step")  
        self.datacollector.collect(self)