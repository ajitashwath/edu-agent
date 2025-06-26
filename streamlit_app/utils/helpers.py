import streamlit as st
from datetime import datetime, timedelta
import json

class HelperFunctions:
    @staticmethod
    def validate_student_data(data):
        """
        Validate student input data
        """
        errors = []
        
        if not data.get('school_name', '').strip():
            errors.append("School name is required")
        
        if data.get('percentage', 0) < 40:
            errors.append("Academic percentage seems too low")
        
        if data.get('age', 0) < 14 or data.get('age', 0) > 20:
            errors.append("Age should be between 14-20 years")
        
        return errors
    
    @staticmethod
    def calculate_preparation_time(age, current_class):
        """
        Calculate available preparation time based on age and class
        """
        if 'Dropper' in current_class:
            return "6-12 months intensive preparation"
        elif age <= 16:
            return "2+ years of preparation time"
        elif age == 17:
            return "1-2 years of preparation time"
        else:
            return "Less than 1 year - intensive preparation needed"
    
    @staticmethod
    def get_performance_level(percentage):
        """
        Categorize performance level based on percentage
        """
        if percentage >= 90:
            return {"level": "Excellent", "color": "green", "advice": "Maintain consistency and focus on advanced problem solving"}
        elif percentage >= 75:
            return {"level": "Good", "color": "blue", "advice": "Strong foundation, work on speed and accuracy"}
        elif percentage >= 60:
            return {"level": "Average", "color": "orange", "advice": "Need to strengthen fundamentals and increase study hours"}
        else:
            return {"level": "Needs Improvement", "color": "red", "advice": "Focus on building strong foundation, consider coaching"}
    
    @staticmethod
    def generate_mock_roadmap(student_data):
        """
        Generate a mock roadmap when AI agents are not available
        This is a fallback function for demonstration purposes
        """
        percentage = student_data['percentage']
        age = student_data['age']
        weak_subjects = student_data.get('weak_subjects', [])
        
        # Generate personalized content based on student profile
        roadmap_content = f"""
        # Personalized IIT-JEE Study Roadmap
        
        ## Student Profile Analysis
        - Academic Performance: {percentage}% - {HelperFunctions.get_performance_level(percentage)['level']}
        - Age: {age} years
        - Preparation Time: {HelperFunctions.calculate_preparation_time(age, student_data.get('current_class', 'Class 11'))}
        
        ## Recommended Strategy
        Based on your profile, here's your personalized approach:
        
        ### Phase 1: Foundation Building (2-3 months)
        - Complete NCERT thoroughly for all three subjects
        - Focus extra attention on: {', '.join(weak_subjects) if weak_subjects else 'maintaining balance across all subjects'}
        - Daily practice: 4-6 hours
        
        ### Phase 2: Concept Development (4-6 months)
        - Advanced reference books
        - Topic-wise test series
        - Problem-solving techniques
        - Daily practice: 6-8 hours
        
        ### Phase 3: Intensive Practice (3-4 months)
        - Full-length mock tests
        - Previous year paper analysis
        - Time management skills
        - Revision strategies
        
        ## Subject-wise Recommendations
        
        ### Mathematics
        - NCERT + R.D. Sharma for basics
        - Cengage for advanced problems
        - Focus on calculus and coordinate geometry
        
        ### Physics
        - NCERT + H.C. Verma essential
        - Focus on mechanics and electromagnetism
        - Regular numerical practice
        
        ### Chemistry
        - NCERT is sufficient for inorganic
        - O.P. Tandon for physical chemistry
        - Morrison Boyd for organic chemistry
        
        ## Daily Schedule Recommendation
        - Morning: Mathematics (2-3 hours)
        - Afternoon: Physics (2-3 hours) 
        - Evening: Chemistry (2-3 hours)
        - Night: Revision and doubt clearing (1 hour)
        
        ## Monthly Targets
        1. Month 1-2: Complete NCERT
        2. Month 3-4: Reference books (50%)
        3. Month 5-6: Reference books (100%) + Tests
        4. Month 7-8: Mock tests and analysis
        5. Month 9-10: Previous years + weak areas
        6. Month 11-12: Final revision and exam prep
        
        ## Success Mantras
        - Consistency is key
        - Quality over quantity
        - Regular self-assessment
        - Maintain physical and mental health
        - Stay motivated and positive
        """
        
        return {
            'status': 'success',
            'roadmap': roadmap_content,
            'student_profile': student_data
        }
    
    @staticmethod
    def save_user_session(student_data):
        """
        Save user session data (in real app, this would use database)
        """
        if 'user_sessions' not in st.session_state:
            st.session_state.user_sessions = []
        
        session_data = {
            'timestamp': datetime.now().isoformat(),
            'student_data': student_data
        }
        
        st.session_state.user_sessions.append(session_data)
    
    @staticmethod
    def get_motivational_quote():
        """
        Return a random motivational quote for JEE aspirants
        """
        quotes = [
            "Success is not final, failure is not fatal: it is the courage to continue that counts. - Winston Churchill",
            "The expert in anything was once a beginner. - Helen Hayes",
            "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
            "Success is the sum of small efforts repeated day in and day out. - Robert Collier",
            "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
            "Hard work beats talent when talent doesn't work hard. - Tim Notke",
            "Champions are made from something deep inside them - a desire, a dream, a vision. - Muhammad Ali",
            "The only impossible journey is the one you never begin. - Tony Robbins"
        ]
        
        import random
        return random.choice(quotes)
    
    @staticmethod
    def format_study_time(hours):
        """
        Format study time in a readable format
        """
        if hours < 1:
            return f"{int(hours * 60)} minutes"
        elif hours == 1:
            return "1 hour"
        else:
            return f"{hours} hours"
    
    @staticmethod
    def calculate_exam_countdown():
        """
        Calculate days remaining for JEE Main (approximate)
        """
        # JEE Main typically happens in January and April
        current_date = datetime.now()
        
        # Next JEE Main dates (approximate)
        if current_date.month <= 1:
            next_exam = datetime(current_date.year, 1, 30)
        elif current_date.month <= 4:
            next_exam = datetime(current_date.year, 4, 15)
        else:
            next_exam = datetime(current_date.year + 1, 1, 30)
        
        days_remaining = (next_exam - current_date).days
        return max(0, days_remaining)
    
    @staticmethod
    def get_subject_tips(subject):
        """
        Get subject-specific preparation tips
        """
        tips = {
            'Mathematics': [
                "Practice daily - mathematics needs consistent practice",
                "Focus on understanding concepts, not just memorizing formulas",
                "Solve previous year questions to identify patterns",
                "Master calculus, algebra, and coordinate geometry first",
                "Keep a formula sheet and review it regularly"
            ],
            'Physics': [
                "Understand the physical concepts behind formulas",
                "Practice numerical problems daily",
                "Focus on mechanics, electromagnetism, and modern physics",
                "Draw diagrams to visualize problems",
                "Connect physics concepts to real-world applications"
            ],
            'Chemistry': [
                "NCERT is your bible for chemistry",
                "Make separate notes for organic reaction mechanisms",
                "Practice inorganic chemistry daily for memorization", 
                "Understand the logic behind periodic properties",
                "Focus on physical chemistry numerical problems"
            ]
        }
        
        return tips.get(subject, [])