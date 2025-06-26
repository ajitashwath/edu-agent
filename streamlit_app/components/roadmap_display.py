import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import pandas as pd

class RoadmapDisplay:
    @staticmethod
    def render(roadmap_data):
        """
        Display the generated study roadmap
        """
        if roadmap_data['status'] == 'error':
            st.error(f"❌ {roadmap_data['message']}")
            return
        
        st.success("✅ Your personalized study roadmap has been generated!")
        
        # Display roadmap content
        st.header("🗺️ Your IIT-JEE Study Roadmap")
        
        # Create tabs for different sections
        tab1, tab2, tab3, tab4, tab5 = st.tabs([
            "📊 Profile Analysis", 
            "📅 Study Plan", 
            "📚 Resources", 
            "⏰ Schedule", 
            "📈 Progress Tracker"
        ])
        
        with tab1:
            RoadmapDisplay._display_profile_analysis(roadmap_data)
        
        with tab2:
            RoadmapDisplay._display_study_plan(roadmap_data)
        
        with tab3:
            RoadmapDisplay._display_resources(roadmap_data)
        
        with tab4:
            RoadmapDisplay._display_schedule(roadmap_data)
        
        with tab5:
            RoadmapDisplay._display_progress_tracker(roadmap_data)
    
    @staticmethod
    def _display_profile_analysis(roadmap_data):
        """Display academic profile analysis"""
        st.subheader("🎯 Academic Profile Analysis")
        
        student_data = roadmap_data['student_profile']
        
        # Performance indicators
        col1, col2, col3 = st.columns(3)
        
        with col1:
            # Determine performance level
            percentage = student_data['percentage']
            if percentage >= 90:
                level = "Excellent"
                color = "green"
            elif percentage >= 75:
                level = "Good"
                color = "blue"
            elif percentage >= 60:
                level = "Average"
                color = "orange"
            else:
                level = "Needs Improvement"
                color = "red"
            
            st.metric("Performance Level", level)
        
        with col2:
            # Preparation time remaining
            age = student_data['age']
            if age <= 16:
                time_left = "2+ years"
                urgency = "Low"
            elif age == 17:
                time_left = "1-2 years"
                urgency = "Medium"
            else:
                time_left = "<1 year"
                urgency = "High"
            
            st.metric("Preparation Time", time_left)
        
        with col3:
            st.metric("Urgency Level", urgency)
        
        # Strengths and Areas for Improvement
        col4, col5 = st.columns(2)
        
        with col4:
            st.write("### 💪 Identified Strengths")
            strengths = [
                f"Academic performance: {percentage}%",
                f"Age advantage: {age} years old"
            ]
            
            if student_data.get('strong_subjects'):
                strengths.extend([f"Strong in {subject}" for subject in student_data['strong_subjects']])
            
            for strength in strengths:
                st.write(f"✅ {strength}")
        
        with col5:
            st.write("### 📈 Areas for Improvement")
            improvements = []
            
            if percentage < 75:
                improvements.append("Focus on strengthening academic foundation")
            
            if student_data.get('weak_subjects'):
                improvements.extend([f"Improve {subject} concepts" for subject in student_data['weak_subjects']])
            
            if not improvements:
                improvements = ["Continue maintaining current performance", "Focus on advanced problem solving"]
            
            for improvement in improvements:
                st.write(f"🎯 {improvement}")
    
    @staticmethod
    def _display_study_plan(roadmap_data):
        """Display detailed study plan"""
        st.subheader("📋 Comprehensive Study Plan")
        
        # Sample roadmap content (in real implementation, this would come from the AI agents)
        student_data = roadmap_data['student_profile']
        
        # Phase-wise planning
        phases = [
            {
                "phase": "Foundation Building",
                "duration": "2-3 months",
                "focus": "Strengthen basic concepts in PCM",
                "activities": [
                    "Complete NCERT thoroughly",
                    "Solve basic numerical problems",
                    "Clear conceptual doubts"
                ]
            },
            {
                "phase": "Concept Development",
                "duration": "4-6 months", 
                "focus": "Advanced problem solving",
                "activities": [
                    "Reference book problem solving",
                    "Topic-wise test series",
                    "Formula consolidation"
                ]
            },
            {
                "phase": "Practice & Revision",
                "duration": "3-4 months",
                "focus": "Mock tests and revision",
                "activities": [
                    "Full-length mock tests",
                    "Previous year papers",
                    "Weak area improvement"
                ]
            }
        ]
        
        for i, phase in enumerate(phases, 1):
            with st.expander(f"Phase {i}: {phase['phase']} ({phase['duration']})"):
                st.write(f"**Focus:** {phase['focus']}")
                st.write("**Key Activities:**")
                for activity in phase['activities']:
                    st.write(f"• {activity}")
        
        # Subject-wise breakdown
        st.write("### 📚 Subject-wise Focus Distribution")
        
        subjects = ['Mathematics', 'Physics', 'Chemistry']
        # Adjust time based on weak subjects
        weak_subjects = student_data.get('weak_subjects', [])
        
        time_allocation = {}
        base_time = 33.33  # Equal distribution base
        
        for subject in subjects:
            if subject in weak_subjects:
                time_allocation[subject] = base_time + 10  # Extra 10% for weak subjects
            else:
                time_allocation[subject] = base_time - 5   # Reduce 5% from strong subjects
        
        # Normalize to 100%
        total = sum(time_allocation.values())
        time_allocation = {k: (v/total)*100 for k, v in time_allocation.items()}
        
        # Create pie chart
        fig = px.pie(
            values=list(time_allocation.values()),
            names=list(time_allocation.keys()),
            title="Recommended Time Allocation"
        )
        st.plotly_chart(fig, use_container_width=True)
    
    @staticmethod
    def _display_resources(roadmap_data):
        """Display recommended resources"""
        st.subheader("📚 Recommended Study Resources")
        
        # Books section
        st.write("### 📖 Essential Books")
        
        books = {
            "Mathematics": [
                "NCERT Mathematics (Class 11 & 12)",
                "R.D. Sharma",
                "Cengage Mathematics",
                "Arihant Problem Book"
            ],
            "Physics": [
                "NCERT Physics (Class 11 & 12)", 
                "H.C. Verma (Concepts of Physics)",
                "D.C. Pandey (Arihant)",
                "Resnick Halliday Krane"
            ],
            "Chemistry": [
                "NCERT Chemistry (Class 11 & 12)",
                "O.P. Tandon",
                "Morrison & Boyd (Organic)",
                "J.D. Lee (Inorganic)"
            ]
        }
        
        for subject, book_list in books.items():
            with st.expander(f"{subject} Books"):
                for book in book_list:
                    st.write(f"📚 {book}")
        
        # Online platforms
        st.write("### 💻 Online Learning Platforms")
        
        platforms = [
            {"name": "Unacademy", "type": "Comprehensive courses", "rating": "⭐⭐⭐⭐"},
            {"name": "BYJU'S", "type": "Interactive learning", "rating": "⭐⭐⭐⭐"},
            {"name": "Vedantu", "type": "Live classes", "rating": "⭐⭐⭐⭐"},
            {"name": "Khan Academy", "type": "Free resources", "rating": "⭐⭐⭐⭐"},
            {"name": "YouTube (Physics Wallah)", "type": "Free lectures", "rating": "⭐⭐⭐⭐⭐"}
        ]
        
        for platform in platforms:
            col1, col2, col3 = st.columns([2, 2, 1])
            with col1:
                st.write(f"**{platform['name']}**")
            with col2:
                st.write(platform['type'])
            with col3:
                st.write(platform['rating'])
        
        # Mobile apps
        st.write("### 📱 Recommended Mobile Apps")
        apps = [
            "Toppr", "Embibe", "Doubtnut", "BYJU'S Learning App", "Unacademy Learning App"
        ]
        
        cols = st.columns(len(apps))
        for i, app in enumerate(apps):
            with cols[i]:
                st.write(f"📱 {app}")
    
    @staticmethod
    def _display_schedule(roadmap_data):
        """Display optimized study schedule"""
        st.subheader("⏰ Optimized Study Schedule")
        
        student_data = roadmap_data['student_profile']
        
        # Daily schedule
        st.write("### 📅 Recommended Daily Schedule")
        
        # Adjust schedule based on current class
        current_class = student_data.get('current_class', 'Class 11')
        
        if 'Dropper' in current_class:
            # Full-time preparation schedule
            schedule = [
                {"time": "6:00 - 7:00 AM", "activity": "Morning Revision", "subject": "Previous day topics"},
                {"time": "7:00 - 8:00 AM", "activity": "Exercise & Breakfast", "subject": "Health"},
                {"time": "8:00 - 11:00 AM", "activity": "Study Session 1", "subject": "Mathematics"},
                {"time": "11:00 - 11:30 AM", "activity": "Break", "subject": "Rest"},
                {"time": "11:30 AM - 2:30 PM", "activity": "Study Session 2", "subject": "Physics"},
                {"time": "2:30 - 3:30 PM", "activity": "Lunch & Rest", "subject": "Break"},
                {"time": "3:30 - 6:30 PM", "activity": "Study Session 3", "subject": "Chemistry"},
                {"time": "6:30 - 7:30 PM", "activity": "Evening Break", "subject": "Recreation"},
                {"time": "7:30 - 9:30 PM", "activity": "Problem Solving", "subject": "Mixed Practice"},
                {"time": "9:30 - 10:30 PM", "activity": "Dinner & Family Time", "subject": "Break"},
                {"time": "10:30 - 11:30 PM", "activity": "Revision & Notes", "subject": "Day's Summary"}
            ]
        else:
            # School + preparation schedule
            schedule = [
                {"time": "6:00 - 7:00 AM", "activity": "Morning Study", "subject": "Quick Revision"},
                {"time": "7:00 - 8:00 AM", "activity": "Get Ready for School", "subject": "Preparation"},
                {"time": "8:00 AM - 2:00 PM", "activity": "School Hours", "subject": "Attend Classes"},
                {"time": "2:00 - 3:00 PM", "activity": "Lunch & Rest", "subject": "Break"},
                {"time": "3:00 - 5:00 PM", "activity": "JEE Study Session 1", "subject": "Mathematics"},
                {"time": "5:00 - 5:30 PM", "activity": "Break & Snacks", "subject": "Rest"},
                {"time": "5:30 - 7:30 PM", "activity": "JEE Study Session 2", "subject": "Physics/Chemistry"},
                {"time": "7:30 - 8:30 PM", "activity": "Dinner & Family Time", "subject": "Break"},
                {"time": "8:30 - 10:00 PM", "activity": "School Homework", "subject": "School Work"},
                {"time": "10:00 - 11:00 PM", "activity": "Revision & Planning", "subject": "Next Day Prep"}
            ]
        
        # Display schedule in a table format
        df = pd.DataFrame(schedule)
        st.dataframe(df, use_container_width=True, hide_index=True)
        
        # Weekly plan
        st.write("### 📊 Weekly Study Distribution")
        
        weekly_data = {
            'Day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
            'Mathematics': [3, 2, 3, 2, 3, 4, 2],
            'Physics': [2, 3, 2, 3, 2, 3, 3],
            'Chemistry': [2, 2, 3, 3, 2, 2, 3],
            'Revision': [1, 1, 1, 1, 2, 2, 3]
        }
        
        df_weekly = pd.DataFrame(weekly_data)
        
        fig = px.bar(
            df_weekly, 
            x='Day', 
            y=['Mathematics', 'Physics', 'Chemistry', 'Revision'],
            title="Weekly Study Hours Distribution",
            labels={'value': 'Hours', 'variable': 'Subject'}
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    @staticmethod
    def _display_progress_tracker(roadmap_data):
        """Display progress tracking tools"""
        st.subheader("📈 Progress Tracking & Milestones")
        
        # Monthly milestones
        st.write("### 🎯 Monthly Milestones")
        
        milestones = [
            {"month": "Month 1", "target": "Complete NCERT (50%)", "test": "Basic Concept Test"},
            {"month": "Month 2", "target": "Complete NCERT (100%)", "test": "NCERT Based Test"},
            {"month": "Month 3", "target": "Reference Books (25%)", "test": "Mixed Topic Test"},
            {"month": "Month 4", "target": "Reference Books (50%)", "test": "Advanced Problems Test"},
            {"month": "Month 5", "target": "Reference Books (75%)", "test": "Full Syllabus Test 1"},
            {"month": "Month 6", "target": "Reference Books (100%)", "test": "Full Syllabus Test 2"}
        ]
        
        for milestone in milestones:
            col1, col2, col3 = st.columns([1, 2, 2])
            with col1:
                st.write(f"**{milestone['month']}**")
            with col2:
                st.write(milestone['target'])
            with col3:
                st.write(f"📝 {milestone['test']}")
        
        # Mock test schedule
        st.write("### 📝 Mock Test Schedule")
        
        test_schedule = {
            'Test Type': ['Weekly Tests', 'Bi-weekly Full Tests', 'Monthly Assessments', 'Previous Year Papers'],
            'Frequency': ['Every Sunday', 'Every 2 weeks', 'Month end', 'Last 6 months'],
            'Duration': ['2 hours', '3 hours', '3 hours', '3 hours'],
            'Focus': ['Topic-wise', 'Full syllabus', 'Complete revision', 'Real exam pattern']
        }
        
        df_tests = pd.DataFrame(test_schedule)
        st.dataframe(df_tests, use_container_width=True, hide_index=True)
        
        # Performance tracking chart
        st.write("### 📊 Expected Performance Curve")
        
        months = list(range(1, 13))
        expected_scores = [30, 40, 50, 60, 68, 75, 80, 85, 88, 90, 92, 95]
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=months, 
            y=expected_scores,
            mode='lines+markers',
            name='Expected Score',
            line=dict(color='blue', width=3)
        ))
        
        fig.update_layout(
            title='Expected JEE Score Improvement Over Time',
            xaxis_title='Months of Preparation',
            yaxis_title='Expected Score (%)',
            yaxis=dict(range=[0, 100])
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Success tips
        st.write("### 💡 Success Tips")
        
        tips = [
            "🎯 Set daily, weekly, and monthly targets",
            "📊 Track your performance in each subject",
            "🔄 Regular revision is key to retention",
            "❓ Clear doubts immediately - don't accumulate them",
            "🏃‍♂️ Maintain physical and mental health",
            "⏰ Stick to your schedule consistently",
            "📝 Maintain error logs for improvement",
            "🎉 Celebrate small wins to stay motivated"
        ]
        
        for tip in tips:
            st.write(tip)
    
    @staticmethod
    def display_download_options(roadmap_data):
        """Provide download options for the roadmap"""
        st.subheader("💾 Download Your Roadmap")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("📄 Download PDF Report", use_container_width=True):
                st.info("PDF download feature will be available soon!")
        
        with col2:
            if st.button("📧 Email Roadmap", use_container_width=True):
                st.info("Email feature will be available soon!")