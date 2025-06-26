from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List, Dict, Any
from datetime import datetime
import yaml
import os

def load_yaml_config(path):
    with open(path, 'r', encoding = 'utf-8') as f:
        return yaml.safe_load(f)

AGENTS_YAML = os.path.join(os.path.dirname(__file__), 'config', 'agents.yaml')
TASKS_YAML = os.path.join(os.path.dirname(__file__), 'config', 'tasks.yaml')

@CrewBase
class EduAgent():

    agents: List[BaseAgent]
    tasks: List[Task]
    agents_config: Dict[str, Any] = load_yaml_config(AGENTS_YAML)
    tasks_config: Dict[str, Any] = load_yaml_config(TASKS_YAML)

    @agent
    def academic_analyzer(self) -> Agent:
        cfg = self.agents_config['academic_analyzer']
        return Agent(
            role=cfg['role'],
            goal=cfg['goal'],
            backstory=cfg['backstory'],
            verbose=True,
            max_execution_time=300,
            allow_delegation=False
        )

    @agent
    def study_planner(self) -> Agent:
        cfg = self.agents_config['study_planner']
        return Agent(
            role=cfg['role'],
            goal=cfg['goal'],
            backstory=cfg['backstory'],
            verbose=True,
            max_execution_time=300,
            allow_delegation=False
        )

    @agent
    def resource_advisor(self) -> Agent:
        cfg = self.agents_config['resource_advisor']
        return Agent(
            role=cfg['role'],
            goal=cfg['goal'],
            backstory=cfg['backstory'],
            verbose=True,
            max_execution_time=300,
            allow_delegation=False
        )

    @task
    def academic_analysis_task(self) -> Task:
        cfg = self.tasks_config['academic_analysis_task']
        return Task(
            description=cfg['description'],
            expected_output=cfg['expected_output'],
            agent=self.academic_analyzer()
        )

    @task
    def study_planning_task(self) -> Task:
        cfg = self.tasks_config['study_planning_task']
        return Task(
            description=cfg['description'],
            expected_output=cfg['expected_output'],
            agent=self.study_planner(),
            context=[self.academic_analysis_task()]
        )

    @task
    def resource_recommendation_task(self) -> Task:
        cfg = self.tasks_config['resource_recommendation_task']
        return Task(
            description=cfg['description'],
            expected_output=cfg['expected_output'],
            agent=self.resource_advisor(),
            context=[self.academic_analysis_task()]
        )

    @task
    def final_roadmap_compilation(self) -> Task:
        cfg = self.tasks_config['final_roadmap_compilation']
        return Task(
            description=cfg['description'],
            expected_output=cfg['expected_output'],
            agent=self.study_planner(),
            context=[self.academic_analysis_task(), self.study_planning_task(), self.resource_recommendation_task()],
            output_file='jee_roadmap.md'
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
            memory=True,
            embedder={
                "provider": "openai",
                "config": {
                    "model": "text-embedding-3-small"
                }
            }
        )

    def generate_roadmap(self, academic_percentage: float, school_name: str, age: int) -> str:
        inputs = {
            'academic_percentage': academic_percentage,
            'school_name': school_name,
            'age': age,
            'current_year': datetime.now().year
        }
        
        try:
            result = self.crew().kickoff(inputs = inputs)
            return result.raw if hasattr(result, 'raw') else str(result)
        except Exception as e:
            raise Exception(f"An error occurred while generating the roadmap: {e}")

    def validate_inputs(self, academic_percentage: float, school_name: str, age: int) -> Dict[str, Any]:
        validation_results = {
            'is_valid': True,
            'errors': [],
            'warnings': []
        }
        
        if not (0 <= academic_percentage <= 100):
            validation_results['is_valid'] = False
            validation_results['errors'].append("Academic percentage must be between 0 and 100")
        elif academic_percentage < 60:
            validation_results['warnings'].append("Low academic percentage may require intensive preparation")

        if not school_name or len(school_name.strip()) < 2:
            validation_results['is_valid'] = False
            validation_results['errors'].append("School name must be provided and meaningful")
        
        if not (13 <= age <= 20):
            validation_results['is_valid'] = False
            validation_results['errors'].append("Age must be between 13 and 20 for JEE preparation")
        elif age < 15:
            validation_results['warnings'].append("Early preparation - ensure strong foundation building")
        elif age > 18:
            validation_results['warnings'].append("Limited time - intensive preparation required")
        
        return validation_results