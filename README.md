# EECS4461_Team14_Project
Team 14 - EECS 4461 Winter 2025

# Project Name
The Trend Manipulator: AI Driving Trends on X

# §A. Overview of the current implementation state.
Our simulation models the “For You” Tab on X. It consists of two agents, human agents and bot agents as well as an algorithm entity. The Model we used as a basis to create our model is a network based model. In our simulation we have 3 topics, active bots have the ability to choose a single topic randomly to inflate and push it to human and inactive bot. Inactive bot coordinates with active bots to engage with the same topic. Humans can change their topic based on who they engage with. Humans can also revert back to their original topic. Our Algorithm entity picks the topic that has the most engagement and recommends it to other humans globally. Meaning that human agents who are surrounded by agents that all push the same type of content, have chances to be influenced by the algorithm to engage with other topics.

# §B. How to run the simulation (installation steps, commands).
- Download the three code file from [src](src) folder.
- Get the dependencies from [requirements.txt](requirements.txt).
- Open the files in VS Code.
- Install the dependencies by:
  ```sh
  pip install -r requirements.txt
- Finally, Run the simulation
  ```sh
  python -m solara run app.py

# §C. Limitations and planned improvements for the next phase.
For DEL4, we plan to improve our simulation and make it more realistic. We have planned to make the algorithm have the ability to recommend more than a singular topic in the simulation to see behavior of humans. Furthermore, bots can coordinate and inflate other topics to agents.

# Table of contents
- [Deliverable 1](Docs/Deliverable1/)
- [Deliverable 2](Docs/Deliverable2/DEL2B_Proposal/)
- [Deliverable 3]
- [Deliverable 4]
- [Examples](Examples/)
- [src](src/)

# Contributers
Ebrahim Azarbar, Emir Cetinalp, Atmiya Jadvani
