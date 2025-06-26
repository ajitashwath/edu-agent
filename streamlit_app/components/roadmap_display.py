import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
from datetime import datetime, timedelta

def display_results(result, academic_percentage, school_name, age, current_class):
    st.success("🎉 Your personalized IIT/JEE study roadmap is ready!")
    tab1, tab2, tab3, tab4 = st.tabs(["📊 Profile Analysis", "🗺️ Study Roadmap", "📚 Resources", "📈 Progress Tracker"])
    
    with tab1:
        display_profile_analysis(result, academic_percentage, school_name, age)
    
    with tab2:
        display_study_roadmap(result)
    
    with tab3:
        display_resources(result)
    
    with tab4:
        display_progress_tracker()

def display_profile_analysis(result, academic_percentage, school_name, age):
    st.subheader("🔍 Your Academic Profile Analysis")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Academic %", f"{academic_percentage}%")
    with col2:
        st.metric("Current Age", f"{age} years")
    with col3:
        prep_time = 24 - age if age < 18 else 12
        st.metric("Prep Time", f"{prep_time} months")
    
    with col4:
        if academic_percentage >= 90:
            strength = "Excellent"
            color = "🟢"
        elif academic_percentage >= 80:
            strength = "Good"
            color = "🟡"
        else:
            strength = "Needs Work"
            color = "🟠"
        st.metric("Profile", f"{color} {strength}")
    
    st.subheader("🤖 AI Analysis Results")
    if hasattr(result, 'tasks_output') and len(result.tasks_output) > 0:
        analysis_output = result.tasks_output[0].raw
        st.markdown(f"**Analysis Report:**")
        st.write(analysis_output)
    else:
        st.write(str(result)[:1000] + "..." if len(str(result)) > 1000 else str(result))

def display_study_roadmap(result):
    st.subheader("🗺️ Your Personalized Study Roadmap")
    create_timeline_chart()
    if hasattr(result, 'tasks_output') and len(result.tasks_output) > 1:
        roadmap_output = result.tasks_output[1].raw
        st.markdown("**Detailed Roadmap:**")
        st.write(roadmap_output)
    else:
        display_default_roadmap()

def create_timeline_chart():
    phases = ['Foundation', 'Intermediate', 'Advanced', 'Revision', 'Mock Tests']
    start_date = datetime.today()
    durations = [4, 5, 6, 3, 2]
    dates = [start_date + timedelta(weeks=4*sum(durations[:i])) for i in range(len(phases)+1)]

    fig = go.Figure()
    for i, phase in enumerate(phases):
        fig.add_trace(go.Bar(
            x = [(dates[i+1] - dates[i]).days],
            y = [phase],
            orientation = 'h',
            base = [dates[i]],
            name = phase
        ))
    fig.update_layout(
        title = 'Study Roadmap Timeline',
        xaxis_title = 'Date',
        yaxis_title = 'Phase',
        barmode = 'stack',
        showlegend = False
    )
    st.plotly_chart(fig, use_container_width = True)

def display_default_roadmap():
    st.info("No detailed roadmap available. Here's a plan:")
    st.markdown("""
    - **Foundation (Months 1-4):** Focus on NCERT basics, clear concepts in Physics, Chemistry, and Math.
    - **Intermediate (Months 5-9):** Start solving JEE-level problems, join test series, cover advanced topics.
    - **Advanced (Months 10-15):** Take mock tests, analyze mistakes, focus on weak areas.
    - **Revision (Months 16-18):** Revise all subjects, practice previous year papers.
    - **Mock Tests (Months 19-20):** Take full-length mock tests, simulate exam conditions.
    """)

def display_resources(result):
    st.subheader("📚 Recommended Resources")
    if hasattr(result, 'tasks_output') and len(result.tasks_output) > 2:
        resources_output = result.tasks_output[2].raw
        st.markdown("**AI-Recommended Resources:**")
        st.write(resources_output)
    else:
        st.write("- NCERT Textbooks\n- H.C. Verma for Physics\n- O.P. Tandon for Chemistry\n- R.D. Sharma for Math\n- Previous Year JEE Papers\n- Online platforms: Unacademy, Vedantu, Khan Academy")

def display_progress_tracker():
    st.subheader("📈 Progress Tracker")
    st.write("Track your study progress here! (Feature coming soon)")
    progress = st.slider("Your Preparation Progress (%)", 0, 100, 40)
    st.progress(progress)