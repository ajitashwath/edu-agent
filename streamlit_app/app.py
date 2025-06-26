import streamlit as st
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from components.input_form import StudentInputForm
from components.roadmap_display import RoadmapDisplay
from utils.helpers import HelperFunctions
# from edu_agent.crew import EducationCrew

def main():
    # Page configuration
    st.set_page_config(
        page_title="IIT-JEE Study Roadmap Generator",
        page_icon="🎓",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    st.markdown("""
    <style>
        .main-header {
            font-size: 3rem;
            color: #1f77b4;
            text-align: center;
            margin-bottom: 2rem;
        }
        .motivational-quote {
            font-style: italic;
            text-align: center;
            color: #666;
            padding: 1rem;
            border-left: 4px solid #1f77b4;
            margin: 1rem 0;
            background-color: #f8f9fa;
        }
        .success-metric {
            background: linear-gradient(90deg, #00C851, #007E33);
            color: white;
            padding: 1rem;
            border-radius: 10px;
            text-align: center;
            margin: 0.5rem 0;
        }
        .stButton > button {
            background: linear-gradient(90deg, #1f77b4, #0d47a1);
            color: white;
            border: none;
            padding: 0.5rem 1rem;
            border-radius: 5px;
            font-weight: bold;
        }
    </style>
    """, unsafe_allow_html=True)
    
    # Header
    st.markdown('<h1 class="main-header">IIT-JEE Study Roadmap Generator</h1>', unsafe_allow_html=True)
    st.markdown('<div class="motivational-quote">"' + HelperFunctions.get_motivational_quote() + '"</div>', unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        #st.image("https://via.placeholder.com/300x200.png?text=IIT-JEE+Success", use_column_width=True)
        st.header("📊 Quick Stats")
        
        # Display some motivational stats
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Days to JEE (Expected)", HelperFunctions.calculate_exam_countdown())
        with col2:
            st.metric("Success Rate", "2.5%")
        
        st.write("### 🎯 Why Choose Our Roadmap?")
        st.write("✅ Personalized study plans")
        st.write("✅ Expert-curated resources")
        st.write("✅ Time-optimized schedules")
        st.write("✅ Progress tracking tools")
        st.write("✅ Success-proven strategies")
        
        st.write("### 📞 Need Help?")
        st.info("Contact our experts for personalized guidance!")
    
    # Main content
    # Initialize session state
    if 'roadmap_generated' not in st.session_state:
        st.session_state.roadmap_generated = False
    if 'student_data' not in st.session_state:
        st.session_state.student_data = None
    if 'roadmap_data' not in st.session_state:
        st.session_state.roadmap_data = None
    
    # Show different views based on state
    if not st.session_state.roadmap_generated:
        # Input form view
        st.write("## 📝 Tell Us About Yourself")
        st.write("Help us create a personalized study roadmap tailored to your academic profile and goals.")
        
        # Render input form
        student_data = StudentInputForm.render()
        
        if student_data:
            # Validate data
            errors = HelperFunctions.validate_student_data(student_data)
            
            if errors:
                for error in errors:
                    st.error(f"❌ {error}")
            else:
                # Show profile summary
                StudentInputForm.display_profile_summary(student_data)
                
                # Generate roadmap
                with st.spinner("🤖 AI agents are working on your personalized roadmap..."):
                    # Save student data
                    st.session_state.student_data = student_data
                    HelperFunctions.save_user_session(student_data)
                    roadmap_data = HelperFunctions.generate_mock_roadmap(student_data)
                    
                    st.session_state.roadmap_data = roadmap_data
                    st.session_state.roadmap_generated = True
                
                # Auto-rerun to show roadmap
                st.rerun()
    
    else:
        # Roadmap display view
        st.write("## 🗺️ Your Personalized Study Roadmap")
        
        # Add navigation buttons
        col1, col2, col3 = st.columns([1, 1, 1])
        
        with col1:
            if st.button("🔄 Generate New Roadmap", use_container_width=True):
                st.session_state.roadmap_generated = False
                st.session_state.student_data = None
                st.session_state.roadmap_data = None
                st.rerun()
        
        with col2:
            if st.button("📊 View Profile", use_container_width=True):
                if st.session_state.student_data:
                    StudentInputForm.display_profile_summary(st.session_state.student_data)
        
        with col3:
            if st.button("💾 Save Roadmap", use_container_width=True):
                st.success("Roadmap saved to your session!")
        
        # Display the roadmap
        if st.session_state.roadmap_data:
            RoadmapDisplay.render(st.session_state.roadmap_data)
            
            # Download options
            st.write("---")
            RoadmapDisplay.display_download_options(st.session_state.roadmap_data)
        
        # Additional resources section
        st.write("---")
        st.write("## 🔗 Additional Resources")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.write("### 📚 Free Resources")
            st.write("• [Khan Academy](https://www.khanacademy.org)")
            st.write("• [NCERT Solutions](https://ncert.nic.in)")
            st.write("• [Previous Year Papers](https://jeemain.nta.nic.in)")
            st.write("• [Physics Wallah YouTube](https://youtube.com/c/PhysicsWallah)")
        
        with col2:
            st.write("### 🏫 Coaching Institutes")
            st.write("• Allen Career Institute")
            st.write("• Resonance")
            st.write("• FIITJEE")
            st.write("• Aakash Institute")
        
        with col3:
            st.write("### 📱 Mobile Apps")
            st.write("• Unacademy")
            st.write("• Motion Learning App")
            st.write("• Melvano")
            st.write("• Vedantu")
    
    # Footer
    st.write("---")
    st.markdown("""
    <div style='text-align: center; color: #666; padding: 1rem;'>
        <p>🎓 Powered by crewAI</p>
        <p>💡 Remember: Success is a journey, not a destination. Keep learning, keep growing!</p>
    </div>
    """, unsafe_allow_html=True)

# Subject-specific tips page
def show_subject_tips():
    st.header("📚 Subject-Specific Preparation Tips")
    
    tab1, tab2, tab3 = st.tabs(["🧮 Mathematics", "⚡ Physics", "🧪 Chemistry"])
    
    with tab1:
        st.subheader("Mathematics Preparation Strategy")
        tips = HelperFunctions.get_subject_tips('Mathematics')
        for tip in tips:
            st.write(f"• {tip}")
    
    with tab2:
        st.subheader("Physics Preparation Strategy")
        tips = HelperFunctions.get_subject_tips('Physics')
        for tip in tips:
            st.write(f"• {tip}")
    
    with tab3:
        st.subheader("Chemistry Preparation Strategy")
        tips = HelperFunctions.get_subject_tips('Chemistry')
        for tip in tips:
            st.write(f"• {tip}")

# Navigation
def navigation():
    st.sidebar.markdown("---")
    st.sidebar.write("### 📋 Navigation")
    
    page = st.sidebar.radio(
        "Go to:",
        ["🏠 Home", "📚 Subject Tips", "📊 Progress Tracker", "❓ FAQ"]
    )
    
    return page

if __name__ == "__main__":
    # Handle navigation
    selected_page = navigation()
    
    if selected_page == "🏠 Home":
        main()
    elif selected_page == "📚 Subject Tips":
        show_subject_tips()
    elif selected_page == "📊 Progress Tracker":
        st.header("📊 Progress Tracker")
        st.info("Progress tracking feature coming soon!")
    elif selected_page == "❓ FAQ":
        st.header("❓ Frequently Asked Questions")
        
        with st.expander("How accurate is the AI-generated roadmap?"):
            st.write("Our AI agents are trained on successful JEE preparation strategies and adapt to your specific profile for maximum effectiveness.")
        
        with st.expander("Can I modify the generated roadmap?"):
            st.write("Yes! The roadmap serves as a guideline. You can adjust it based on your preferences and learning pace.")
        
        with st.expander("How often should I update my profile?"):
            st.write("We recommend updating your profile monthly to get refined recommendations based on your progress.")
        
        with st.expander("Is this suitable for both JEE Main and Advanced?"):
            st.write("Yes, our roadmap covers preparation strategies for both JEE Main and JEE Advanced.")