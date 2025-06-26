from crewai import Agent
from langchain.llms import OpenAI

class EducationAgents:
    def __init__(self):
        self.llm = OpenAI(temperature = 0.7)
    
    def academic_analyzer_agent(self):
        return Agent(
            role='Academic Performance Analyzer',
            goal='Analyze student academic performance and provide insights',
            backstory="""You are an experienced academic counselor with 15+ years of experience 
            in analyzing student performance patterns. You specialize in understanding how different 
            academic backgrounds translate to JEE preparation requirements.""",
            verbose=True,
            allow_delegation=False,
            llm=self.llm
        )
    
    def study_planner_agent(self):
        return Agent(
            role='IIT-JEE Study Strategist',
            goal='Create comprehensive and personalized study roadmaps for IIT-JEE preparation',
            backstory="""You are a top-tier JEE coaching expert who has helped thousands of students 
            crack IIT-JEE. You understand the nuances of different preparation strategies based on 
            student profiles and can create timeline-based study plans.""",
            verbose=True,
            allow_delegation=False,
            llm=self.llm
        )
    
    def resource_curator_agent(self):
        return Agent(
            role='Educational Resource Curator',
            goal='Recommend best study materials and resources for JEE preparation',
            backstory="""You are a JEE preparation specialist who has extensive knowledge of all 
            available study materials, online platforms, coaching institutes, and books. You can 
            recommend the most effective resources based on student needs.""",
            verbose=True,
            allow_delegation=False,
            llm=self.llm
        )
    
    def timeline_optimizer_agent(self):
        return Agent(
            role='Timeline and Schedule Optimizer',
            goal='Create realistic and achievable study schedules',
            backstory="""You are a time management expert who specializes in creating balanced 
            study schedules for competitive exam preparation. You understand how to optimize 
            study time while maintaining student well-being.""",
            verbose=True,
            allow_delegation=False,
            llm=self.llm
        )