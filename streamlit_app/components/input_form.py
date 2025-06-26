import streamlit as st

def render_input_form():
    st.subheader("📝 Student Information")
    
    with st.form("student_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            academic_percentage = st.number_input(
                "Academic Percentage (%)",
                min_value = 40.0,
                max_value = 100.0,
                value = 75.0,
                step = 0.1,
                help = "Your overall academic percentage"
            )
            
            age = st.number_input(
                "Current Age",
                min_value = 14,
                max_value = 22,
                value = 17,
                help = "Your current age in years"
            )
        
        with col2:
            school_name = st.text_input(
                "School Name",
                placeholder = "Enter your school name",
                help = "This helps assess your academic background"
            )
            
            current_class = st.selectbox(
                "Current Class/Status",
                ["9th Grade", "10th Grade", "11th Grade", "12th Grade", "12th Passed"],
                index = 2
            )

        st.subheader("🎯 Preparation Details")
        col3, col4 = st.columns(2)
        with col3:
            target_rank = st.selectbox(
                "Target IIT Rank Range",
                ["Top 100", "Top 500", "Top 1000", "Top 5000", "Top 10000"],
                index=2
            )
        
        with col4:
            study_hours = st.slider(
                "Available Study Hours/Day",
                min_value = 2,
                max_value = 12,
                value = 6,
                help = "Hours you can dedicate to JEE preparation daily"
            )
        
        submit_button = st.form_submit_button(
            "🚀 Generate Study Roadmap",
            use_container_width = True
        )
    
    return {
        'submitted': submit_button,
        'academic_percentage': academic_percentage,
        'school_name': school_name,
        'age': age,
        'current_class': current_class,
        'target_rank': target_rank,
        'study_hours': study_hours
    }