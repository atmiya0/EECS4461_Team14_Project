import solara
from mesa.visualization import (
    Slider,
    SolaraViz,
    make_plot_component,
    make_space_component,
)

from model import MetricNetwork  
from agents import State, TOPICS  


def agent_portrayal(agent):
    node_color_dict = {
        State.HUMAN: TOPICS.get(agent.topic),  
        State.BOT: TOPICS.get(agent.topic), 
        State.INACTIVE_BOT: "gray",  
    }

    return {"color": node_color_dict[agent.state], "size": 45, "marker": "s" if agent.state == State.HUMAN else "o"}

def get_algorithm_topic(model):
    algorithm_text = getattr(model, "algorithm_topic", "None")
    return solara.Markdown(
        f"##Algorithm Recommends: {algorithm_text}"
    )


model_params = {
    "num_nodes": Slider(
        label="Number of agents",
        value=30,
        min=30,
        max=55,
        step=1
    ),
    "active_bot": Slider(
        label="Active Bots",
        value=2,
        min=1,
        max=10,
        step=1
    ),
    "inactive_bot": Slider(
        label="Inactive Bots",
        value=3,
        min=1,
        max=10,
        step=1
    ),
    "bot_spread_chance": Slider(
        label="Bot Spread on Humans",
        value=0.5,
        min=0.1,
        max=0.6,
        step=0.1
    ),
    "human_spread_chance": Slider(
        label="Human Spread on Humans",
        value=0.3,
        min=0.1,
        max=0.5,
        step=0.1
    ),
    "algorithm_spread_chance": Slider(
        label="Algorithm Spread on Humans",
        value=0.2,
        min=0.1,
        max=0.6,
        step=0.1
    ),
}



def post_process_lineplot(ax):
    """Line Graph"""
    ax.set_ylim(ymin=0)
    ax.set_ylabel("Number of humans engaging with the topic")
    ax.legend(bbox_to_anchor=(1.05, 1.0), loc="upper left")

SpacePlot = make_space_component(agent_portrayal)

StatePlot = make_plot_component(
    {topic: TOPICS[topic] for topic in TOPICS.keys()},
    post_process=post_process_lineplot,
)

model1 = MetricNetwork()


page = solara.Column(
    [
        solara.Markdown(r'''
        # <span style="color: orange; font-weight: bold; margin-right: 20px;">Topic 1</span> <span style="color: blue; font-weight: bold; margin-right: 20px;">Topic 2</span>   <span style="color: purple; font-weight: bold;">Topic 3</span>
        ## <span style="font-weight:bold"> Humans (Squares) </span>
        ## <span style="font-weight:bold"> Bots (Circle) </span>
        ### <span style="margin-left: 35px""> - Inactive Bots (Gray Circle) </span>'''),
        SolaraViz(
            model1,
            components=[
                SpacePlot,
                StatePlot,
                get_algorithm_topic],
            model_params=model_params,
            name="Metric Manipulation",
        ),
    ]
)

page  # noqa
