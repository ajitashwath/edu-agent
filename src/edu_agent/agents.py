from crewai import Agent
from crewai_tools import SerperDevTool, FileReadTool
import yaml

import os
os.environ["GEMINI_API_KEY"] = "AIzaSyCmbWVAmQQnIXptRCHJPYNu3-PK1h25ELE"


class JEEAgents:
    def __init__(self):
        self.config_path = os.path.join(os.path.dirname(__file__), '..', '..', 'config', 'agents.yaml')
        self.agents_config = self._load_config()
    
    def _load_config(self):
        with open(self.config_path, 'r') as file:
            return yaml.safe_load(file)
    
    def study_analyst(self):
        return Agent(
            role = self.agents_config['study_analyst']['role'],
            goal = self.agents_config['study_analyst']['goal'],
            verbose = True,
            #memory = True,
            backstory = self.agents_config['study_analyst']['backstory'],
            tools = [],
            allow_delegation = False,
            max_iter = 3,
            max_execution_time = 300
        )
    
    def roadmap_planner(self):
        return Agent(
            role = self.agents_config['roadmap_planner']['role'],
            goal = self.agents_config['roadmap_planner']['goal'],
            verbose = True,
            #memory=True,
            backstory = self.agents_config['roadmap_planner']['backstory'],
            tools = [],
            allow_delegation = False,
            max_iter = 3,
            max_execution_time = 300
        )
    
    def resource_recommender(self):
        return Agent(
            role = self.agents_config['resource_recommender']['role'],
            goal = self.agents_config['resource_recommender']['goal'],
            verbose = True,
            #memory=True,
            backstory = self.agents_config['resource_recommender']['backstory'],
            tools = [], 
            allow_delegation = False,
            max_iter = 3,
            max_execution_time = 300
        )

        