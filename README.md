# EECS4461_Team14_Project
Team 14 - EECS 4461 Winter 2025

# Project Name
The Trend Manipulator: AI Driving Trends on X

# §A. Overview of the phenomenon modeled.
The simulation models metric manipulation on social media, specifically the “For You” Tab on X. It consists of two agents, human agents and bot agents as well as algorithm entities. The model we used as a basis to create our model is a network based model. In our simulation we have 6 topics, decision bots have the ability to inflate topic 1, then topic 2 then 3 and finally repeats. The decision bots can push the topic to humans and follower bots. Follower bots coordinate with active bots to engage with the same topic. Humans can change their topic based on who they engage with. Humans have a tolerance mechanism, where if they engage with a topic for a long time they switch to a different topic. Our main algorithm entity picks the topic that has the most engagement and recommends it to other humans globally. Meaning that human agents who are surrounded by agents that all push the same type of content, have chances to be influenced by the algorithm to engage with other topics. Our second algorithm picks up a topic randomly and recommends it to other humans periodically.

# §B. How to run the simulation (installation steps, commands).
- Download the three code file from [src](src) folder.
- Download the dependencies from [requirements.txt](requirements.txt).
- Extract each of the files to a new folder.
- Open the new folder in VS Code.
- Note: Make sure in the terminal, you are in the newly created folder directory before you install the dependencies and run the application.
- Install the dependencies by:
  ```sh
  pip install -r requirements.txt
- Finally, Run the simulation
  ```sh
  python -m solara run app.py

# §C. Key findings or observations.
- Human dominated, when bot influence was low and there was no algorithm. We noticed human driven topics were dominating the ecosystem. Human agents spread their topics through peep to peer influence. This results in organic narratives spreading on the platform.
- Bot dominated, when bot influence was high and there were algorithms. The bot tricked the algorithm into picking the topic they were pushing and recommend it to humans globally. This caused the topic to trend. The bot influence and algorithm overwhelmed human organic topics.
- Primary driver, we noticed that bots exploit algorithm weakness by inflating a topic's engagement. Bots on their own were unable to gain momentum to trend a topic without help of the algorithm. Bots take advantage of the algorithm design and manipulate it to fit their own needs.


# Table of contents
- [Deliverable 1](Docs/Deliverable1/)
- [Deliverable 2](Docs/Deliverable2/DEL2B_Proposal/)
- [Deliverable 3](Docs/Deliverable3/DEL3B_DraftReport/)
- [Deliverable 4](Docs/Deliverable4/DEL4B_FinalReport/)
- [Examples](Examples/)
- [src](src/)

# Contributers
Ebrahim Azarbar, Emir Cetinalp, Atmiya Jadvani
