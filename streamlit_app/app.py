import streamlit as st
import sys
import os
import time
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent / "src"))

from edu_agent.crew import JEEStudyCrew
from components.input_form import render_input_form
from components.roadmap_display import display_results
from utils.helpers import validate_inputs, calculate_preparation_time

# Page config
st.set_page_config(
    page_title="IIT/JEE Study Roadmap AI Agent",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    .input-section {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    .results-section {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .stButton > button {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 5px;
        padding: 0.5rem 2rem;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

def main():
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>🎓 IIT/JEE Study Roadmap AI Agent</h1>
        <p>Get your personalized study roadmap powered by AI</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar with information
    with st.sidebar:
        st.title("📋 About This Tool")
        st.write("""
        This AI-powered tool creates personalized study roadmaps for IIT/JEE aspirants based on:
        
        **📊 Your Academic Profile**
        - Current academic percentage
        - School background
        - Age and preparation time
        
        **🎯 What You Get**
        - Detailed study roadmap
        - Subject-wise preparation plan
        - Recommended resources
        - Target college suggestions
        
        **🤖 Powered By**
        - CrewAI multi-agent system
        - OpenAI GPT-4
        - Expert knowledge base
        """)
        
        st.markdown("---")
        st.write("**💡 Tips for Best Results:**")
        st.write("- Provide accurate academic percentage")
        st.write("- Mention your school name correctly")
        st.write("- Be honest about your current age")
    
    # Main content
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown('<div class="input-section">', unsafe_allow_html=True)
        st.subheader("📝 Enter Your Details")
        
        # Input form
        with st.form("student_details_form"):
            academic_percentage = st.slider(
                "Academic Percentage (Overall)",
                min_value=40.0,
                max_value=100.0,
                value=75.0,
                step=0.1,
                help="Your overall academic percentage from 9th-12th grade"
            )
            
            school_name = st.text_input(
                "School Name",
                placeholder="Enter your school name",
                help="This helps us understand your academic background"
            )
            
            age = st.number_input(
                "Current Age",
                min_value=14,
                max_value=22,
                value=17,
                help="Your current age in years"
            )
            
            # Class selection
            current_class = st.selectbox(
                "Current Class",
                ["10th Grade", "11th Grade", "12th Grade", "12th Passed (Gap Year)"],
                help="Your current academic status"
            )
            
            submitted = st.form_submit_button("🚀 Generate My Roadmap", use_container_width=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Additional options
        with st.expander("⚙️ Advanced Options"):
            target_exam = st.multiselect(
                "Target Exams",
                ["JEE Main", "JEE Advanced", "BITSAT", "State CET", "Private Colleges"],
                default=["JEE Main", "JEE Advanced"]
            )
            
            preparation_mode = st.radio(
                "Preparation Mode",
                ["Self Study", "Coaching + Self Study", "Online Coaching"],
                index=1
            )
    
    with col2:
        st.markdown('<div class="results-section">', unsafe_allow_html=True)
        
        if submitted:
            # Validate inputs
            validation_errors = validate_inputs(academic_percentage, school_name, age)
            
            if validation_errors:
                st.error("Please fix the following errors:")
                for error in validation_errors:
                    st.write(f"- {error}")
            else:
                # Show loading message
                with st.spinner("🤖 AI agents are analyzing your profile and creating your roadmap..."):
                    try:
                        # Initialize and run the crew
                        crew = JEEStudyCrew()
                        
                        # Add progress bar
                        progress_bar = st.progress(0)
                        status_text = st.empty()
                        
                        status_text.text("Analyzing your academic profile...")
                        progress_bar.progress(25)
                        time.sleep(1)
                        
                        status_text.text("Creating personalized study roadmap...")
                        progress_bar.progress(50)
                        time.sleep(1)
                        
                        status_text.text("Recommending best resources...")
                        progress_bar.progress(75)
                        
                        # Run the crew
                        result = crew.run(
                            academic_percentage=academic_percentage,
                            school_name=school_name,
                            age=age
                        )
                        
                        progress_bar.progress(100)
                        status_text.text("Roadmap generated successfully! 🎉")
                        time.sleep(0.5)
                        
                        # Clear progress indicators
                        progress_bar.empty()
                        status_text.empty()
                        
                        # Display results
                        display_results(result, academic_percentage, school_name, age, current_class)
                        
                    except Exception as e:
                        st.error(f"An error occurred while generating your roadmap: {str(e)}")
                        st.write("Please check your API key and try again.")
        else:
            st.markdown("""
            <div style="text-align: center; padding: 3rem; color: #666;">
                <h3>👆 Fill in your details to get started</h3>
                <p>Our AI agents will analyze your profile and create a personalized study roadmap for IIT/JEE preparation.</p>
                
                <div style="margin-top: 2rem;">
                    <h4>🔍 How it works:</h4>
                    <div style="text-align: left; max-width: 400px; margin: 0 auto;">
                        <p><strong>Step 1:</strong> Student Profile Analysis</p>
                        <p><strong>Step 2:</strong> Personalized Roadmap Creation</p>
                        <p><strong>Step 3:</strong> Resource Recommendations</p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()