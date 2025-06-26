from crewai import Crew, Process
from .agents import EducationAgents
from .tasks import EducationTasks

class EducationCrew:
    def __init__(self):
        self.agents = EducationAgents()
        self.tasks = EducationTasks(self.agents)
    
    def create_study_roadmap(self, student_data):
        """
        Main function to create personalized study roadmap
        """
        # Create tasks with student data
        academic_analysis_task = self.tasks.analyze_academic_profile_task(student_data)
        study_roadmap_task = self.tasks.create_study_roadmap_task(student_data)
        resource_recommendation_task = self.tasks.recommend_resources_task(student_data)
        schedule_optimization_task = self.tasks.optimize_study_schedule_task(student_data)
        
        # Create crew
        crew = Crew(
            agents=[
                self.agents.academic_analyzer_agent(),
                self.agents.study_planner_agent(),
                self.agents.resource_curator_agent(),
                self.agents.timeline_optimizer_agent()
            ],
            tasks=[
                academic_analysis_task,
                study_roadmap_task,
                resource_recommendation_task,
                schedule_optimization_task
            ],
            process=Process.sequential,
            verbose=True
        )
        
        # Execute the crew
        try:
            result = crew.kickoff()
            return {
                'status': 'success',
                'roadmap': result,
                'student_profile': student_data
            }
        except Exception as e:
            return {
                'status': 'error',
                'message': f"Error generating roadmap: {str(e)}",
                'student_profile': student_data
            }