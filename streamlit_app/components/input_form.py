import streamlit as st

class StudentInputForm:
    @staticmethod
    def render():
        """
        Render the student input form
        """
        st.header("📚 Student Profile Input")
        st.write("Please provide your academic details to get a personalized IIT-JEE study roadmap.")
        
        with st.form("student_profile_form"):
            col1, col2 = st.columns(2)
            
            with col1:
                # Academic Percentage Input
                percentage = st.slider(
                    "📊 Academic Percentage",
                    min_value=40.0,
                    max_value=100.0,
                    value=75.0,
                    step=0.5,
                    help="Your current academic percentage (Class 10th/12th)"
                )
                
                # Age Input
                age = st.selectbox(
                    "👤 Age",
                    options=list(range(14, 20)),
                    index=2,  # Default to 16
                    help="Your current age"
                )
            
            with col2:
                # School Name Input
                school_name = st.text_input(
                    "🏫 School Name",
                    placeholder="Enter your school name",
                    help="Name of your current school"
                )
                
                # Class/Grade (Optional for better analysis)
                current_class = st.selectbox(
                    "📖 Current Class",
                    options=["Class 9", "Class 10", "Class 11", "Class 12", "Dropper (12th Pass)"],
                    index=2,  # Default to Class 11
                    help="Your current academic class"
                )
            
            # Additional Information
            st.subheader("Additional Information (Optional)")
            
            col3, col4 = st.columns(2)
            
            with col3:
                preparation_status = st.selectbox(
                    "📚 Current JEE Preparation Status",
                    options=[
                        "Not started yet",
                        "Just beginning",
                        "3-6 months preparation",
                        "6-12 months preparation",
                        "More than 1 year"
                    ],
                    help="How long have you been preparing for JEE?"
                )
            
            with col4:
                target_exam = st.multiselect(
                    "🎯 Target Exams",
                    options=["JEE Main", "JEE Advanced", "BITSAT", "VITEEE", "COMEDK"],
                    default=["JEE Main", "JEE Advanced"],
                    help="Select your target entrance exams"
                )
            
            # Strengths and Weaknesses
            st.subheader("Subject Preferences")
            col5, col6 = st.columns(2)
            
            with col5:
                strong_subjects = st.multiselect(
                    "💪 Strong Subjects",
                    options=["Mathematics", "Physics", "Chemistry"],
                    help="Subjects you feel confident about"
                )
            
            with col6:
                weak_subjects = st.multiselect(
                    "📈 Subjects to Improve",
                    options=["Mathematics", "Physics", "Chemistry"],
                    help="Subjects that need more focus"
                )
            
            # Submit button
            submitted = st.form_submit_button(
                "🚀 Generate My Study Roadmap",
                type="primary",
                use_container_width=True
            )
            
            if submitted:
                # Validation
                if not school_name.strip():
                    st.error("❗ Please enter your school name.")
                    return None
                
                if percentage < 40:
                    st.warning("📢 With current percentage, you'll need intensive preparation. Don't worry, it's achievable!")
                
                # Compile student data
                student_data = {
                    'percentage': percentage,
                    'school_name': school_name.strip(),
                    'age': age,
                    'current_class': current_class,
                    'preparation_status': preparation_status,
                    'target_exams': target_exam,
                    'strong_subjects': strong_subjects,
                    'weak_subjects': weak_subjects
                }
                
                return student_data
        
        return None
    
    @staticmethod
    def display_profile_summary(student_data):
        """
        Display a summary of the student profile
        """
        st.subheader("📋 Your Profile Summary")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Academic %", f"{student_data['percentage']}%")
            st.write(f"**Age:** {student_data['age']} years")
        
        with col2:
            st.write(f"**School:** {student_data['school_name']}")
            st.write(f"**Class:** {student_data['current_class']}")
        
        with col3:
            st.write(f"**Preparation Status:** {student_data['preparation_status']}")
            if student_data['target_exams']:
                st.write(f"**Target Exams:** {', '.join(student_data['target_exams'])}")
        
        if student_data['strong_subjects'] or student_data['weak_subjects']:
            col4, col5 = st.columns(2)
            with col4:
                if student_data['strong_subjects']:
                    st.success(f"**Strong:** {', '.join(student_data['strong_subjects'])}")
            with col5:
                if student_data['weak_subjects']:
                    st.info(f"**Focus Areas:** {', '.join(student_data['weak_subjects'])}")