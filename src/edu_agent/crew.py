from operator import truediv
from unittest import result
from crewai import Crew, Process
from .agents import JEEAgents
from .tasks import JEETasks

class JEEStudyCrew:
    def __init__(self):
        self.agents = JEEAgents()
        self.tasks = JEETasks()
    
    def run(self, academic_percentage, school_name, age):
        study_analyst = self.agents.study_analyst()
        roadmap_planner = self.agents.roadmap_planner()
        resource_recommender = self.agents.resource_recommender()

        analyze_task = self.tasks.analyze_student_profile(
            agent=study_analyst,
            academic_percentage=academic_percentage,
            school_name=school_name,
            age=age
        )
        
        roadmap_task = self.tasks.create_study_roadmap(agent=roadmap_planner)
        resources_task = self.tasks.recommend_resources(agent=resource_recommender)
        roadmap_task.context = [analyze_task]
        resources_task.context = [analyze_task, roadmap_task]
        

        crew = Crew(
            agents=[study_analyst, roadmap_planner, resource_recommender],
            tasks=[analyze_task, roadmap_task, resources_task],
            process=Process.sequential,
            verbose=True,
            memory=True,
            embedder={
                "provider": "google",
                "config": {
                    "model": "gemini-2.5-flash-lite"
                }
            }
        )

        result = crew.kickoff()
        return result