from crewai import Task
import yaml
import os

class JEETasks:
    def __init__(self):
        self.config_path = os.path.join(os.path.dirname(__file__), '..', '..', 'config', 'tasks.yaml')
        self.tasks_config = self._load_config()
    
    def _load_config(self):
        with open(self.config_path, 'r') as file:
            return yaml.safe_load(file)
    
    def analyze_student_profile(self, agent, academic_percentage, school_name, age):
        return Task(
            description=self.tasks_config['analyze_student_profile']['description'].format(
                academic_percentage=academic_percentage,
                school_name=school_name,
                age=age
            ),
            expected_output=self.tasks_config['analyze_student_profile']['expected_output'],
            agent=agent,
            tools=[],
            output_file="student_analysis.md"
        )
    
    def create_study_roadmap(self, agent):
        return Task(
            description=self.tasks_config['create_study_roadmap']['description'],
            expected_output=self.tasks_config['create_study_roadmap']['expected_output'],
            agent=agent,
            tools=[],
            output_file="study_roadmap.md"
        )
    
    def recommend_resources(self, agent):
        return Task(
            description=self.tasks_config['recommend_resources']['description'],
            expected_output=self.tasks_config['recommend_resources']['expected_output'],
            agent=agent,
            tools=[],
            output_file="recommended_resources.md"
        )