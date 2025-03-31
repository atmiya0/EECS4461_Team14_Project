import solara
from mesa.visualization import (
    Slider,
    SolaraViz,
    make_plot_component,
    make_space_component,
)

from model import MetricNetwork  
from agents import State, TOPICS  

BOT_TOPICS = {"Topic 1", "Topic 2", "Topic 3"}
HUMAN_TOPICS = {"Topic 4", "Topic 5", "Topic 6"}

def agent_portrayal(agent):
    node_color_dict ={
        State.HUMAN: TOPICS.get(agent.topic),
        State.BOT: TOPICS.get(agent.topic),
        State.INACTIVE_BOT: "gray",
    }

    return {"color": node_color_dict[agent.state], "size": 45, "marker": "s" if agent.state == State.HUMAN else "o"}

def get_dominating_agent(model):
    """Display which agent is dominating"""
    if model.c ==0:
        return solara.Markdown("##<span style='font-weight: bold'>Simulation has not started</span><br>")

    me = model.most_engaged_topic()
    current_bot_topic=getattr(model, "bot_topic", None)

    if me ==current_bot_topic:
        m = f"##<span style='font-weight: bold'>Bots are dominating</span><br>"
    else:
        m = f"##<span style='font-weight: bold'>Humans are dominating</span><br>"

    return solara.Markdown(m)


def get_status(model):
    """Display topics being pushed by bots and alogrthim"""
    algorithm_text = getattr(model, "algorithm_topic", "None")
    algorithm2_text = getattr(model, "algorithm2_topic", "None")
    bot_topic = getattr(model, "bot_topic", "None")

    return solara.Markdown(
        f"""
        ##<span style='font-weight: bold'>Main Algorithm Recommends:{algorithm_text}</span><br>
        ##<span style='font-weight: bold'>Algorithm 2 Recommends: {algorithm2_text}</span><br>
        ##<span style='font-weight: bold'>Current Bot Topic:{bot_topic}</span>
        """,
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
        label="Decision Bots",
        value=2,
        min=1,
        max=10,
        step=1
    ),
    "inactive_bot": Slider(
        label="Follower Bots",
        value=3,
        min=1,
        max=10,
        step=1
    ),
    "bot_spread_chance": Slider(
        label="Bot on Human Influence",
        value=0.5,
        min=0.0,
        max=1,
        step=0.05
    ),
    "human_spread_chance": Slider(
        label="Human on Human Influence",
        value=0.3,
        min=0.0,
        max=1,
        step=0.05
    ),
    "algorithm_spread_chance": Slider(
        label="Algorithm on Human Influence",
        value=0.5,
        min=0.0,
        max=1,
        step=0.05
    ),
    "algorithm_spread_chance2": Slider(
        label="Algorithm 2 on Human Influence",
        value=0.05,
        min=0.0,
        max=0.1,
        step=0.01
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
        # <span style="color: orange; font-weight: bold;">Topic 1</span> <span style="color: blue; font-weight: bold;">Topic 2</span>   <span style="color: purple; font-weight: bold;">Topic 3</span> <span style="color: red; font-weight: bold;">Topic 4</span> <span style="color: pink; font-weight: bold;">Topic 5</span> <span style="color: green; font-weight: bold;">Topic 6</span>
        ## <span style="font-weight:bold"> Humans (Squares) </span>
        ## <span style="font-weight:bold"> Bots (Circle) </span>
        ### <span style="margin-left: 35px""> - Follower Bots (Gray Circle) </span>'''),
        SolaraViz(
            model1,
            components=[
                SpacePlot,
                StatePlot,
                get_status,
                get_dominating_agent],
            model_params=model_params,
            name="Metric Manipulation",
        ),
    ]
)

page  # noqa
