from crewai import Task

class EducationTasks:
    def __init__(self, agents):
        self.agents = agents
    
    def analyze_academic_profile_task(self, student_data):
        return Task(
            description=f"""
            Analyze the student's academic profile based on the following information:
            - Academic Percentage: {student_data['percentage']}%
            - School Name: {student_data['school_name']}
            - Age: {student_data['age']} years
            
            Provide insights on:
            1. Current academic standing and strengths
            2. Gaps that need to be addressed for JEE preparation
            3. Realistic expectations based on current performance
            4. Recommended preparation intensity level
            """,
            agent=self.agents.academic_analyzer_agent(),
            expected_output="Detailed academic analysis with strengths, weaknesses, and preparation recommendations"
        )
    
    def create_study_roadmap_task(self, student_data):
        return Task(
            description=f"""
            Create a comprehensive study roadmap for JEE preparation considering:
            - Student's current academic level: {student_data['percentage']}%
            - Age: {student_data['age']} years (to determine available preparation time)
            - School background: {student_data['school_name']}
            
            The roadmap should include:
            1. Phase-wise preparation strategy
            2. Subject-wise focus areas (Physics, Chemistry, Mathematics)
            3. Monthly milestones and targets
            4. Mock test schedule
            5. Revision strategies
            6. Backup college options (NITs, IIITs, etc.)
            """,
            agent=self.agents.study_planner_agent(),
            expected_output="Detailed month-by-month study roadmap with clear milestones and strategies"
        )
    
    def recommend_resources_task(self, student_data):
        return Task(
            description=f"""
            Recommend the best study resources tailored for a student with:
            - Academic Performance: {student_data['percentage']}%
            - Age: {student_data['age']} years
            - School: {student_data['school_name']}
            
            Recommend:
            1. Best books for each subject (Physics, Chemistry, Math)
            2. Online platforms and courses
            3. YouTube channels and free resources
            4. Coaching institute recommendations (if needed)
            5. Practice question banks and previous year papers
            6. Mobile apps for preparation
            """,
            agent=self.agents.resource_curator_agent(),
            expected_output="Comprehensive list of recommended study materials and resources with reasons for selection"
        )
    
    def optimize_study_schedule_task(self, student_data):
        return Task(
            description=f"""
            Create an optimized daily and weekly study schedule for:
            - Age: {student_data['age']} years
            - Academic Level: {student_data['percentage']}%
            - School: {student_data['school_name']}
            
            Consider:
            1. School hours and homework time
            2. Optimal study hours per day
            3. Subject rotation and time allocation
            4. Break times and recreational activities
            5. Sleep and health considerations
            6. Weekend intensive study plans
            7. Exam and test schedules
            """,
            agent=self.agents.timeline_optimizer_agent(),
            expected_output="Detailed daily and weekly study schedule with time allocations and balance considerations"
        )