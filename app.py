# app.py – Student Success AI Predictor
# Author: Fatemeh Ramezanpour

import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Page settings
st.set_page_config(
    page_title="Student Success AI Predictor",
    page_icon="🎓",
    layout="centered"
)

# Header and introduction
st.title("🎓 Student Success AI Predictor")
st.markdown("**v1.0 – by Fatemeh Ramezanpour**")
st.write("Predict student final grade based on study habits and attendance")

# Load model - with fallback for demo mode
@st.cache_resource
def load_model():
    try:
        # Try to load the real model
        model = joblib.load("student_success_model.pkl")
        st.sidebar.success("✅ Model loaded successfully!")
        return model
    except Exception as e:
        # If model doesn't exist, create a demo model
        st.sidebar.warning("⚠️ Using demo model (trained on sample data)")
        from sklearn.linear_model import LinearRegression
        model = LinearRegression()
        
        # Create sample data for training demo model
        np.random.seed(42)  # For reproducible results
        X_demo = np.random.rand(100, 4) * 100
        # Simulate relationship between features and final grade
        y_demo = (X_demo[:,0] * 0.6 +  # study hours
                  X_demo[:,1] * 0.3 +  # sleep hours  
                  X_demo[:,2] * 0.8 +  # attendance
                  X_demo[:,3] * 0.7 +  # assignments
                  50)  # base score
        
        model.fit(X_demo, y_demo)
        return model

# Load model
model = load_model()

# Sidebar for information
st.sidebar.header("ℹ️ About")
st.sidebar.write("This AI predictor estimates student final grades based on:")
st.sidebar.write("- 📚 Study hours per week")
st.sidebar.write("- 😴 Sleep hours per day") 
st.sidebar.write("- 📊 Attendance percentage")
st.sidebar.write("- 📝 Assignments completion")

# User input section
st.header("📊 Enter Student Data")

col1, col2 = st.columns(2)

with col1:
    study = st.slider("**Study hours per week**", 0, 100, 40, 5,
                     help="Weekly study hours")
    sleep = st.slider("**Sleep hours per day**", 0, 12, 7, 1,
                     help="Average daily sleep hours")

with col2:
    attend = st.slider("**Attendance percentage**", 0.0, 1.0, 0.85, 0.05,
                      help="Class attendance ratio (0.0 to 1.0)")
    assign = st.slider("**Assignments completed**", 0.0, 1.0, 0.75, 0.05,
                      help="Assignments completion ratio (0.0 to 1.0)")

# Display input summary
st.subheader("📋 Input Summary")
st.write(f"- Study hours: {study} hours/week")
st.write(f"- Sleep hours: {sleep} hours/day") 
st.write(f"- Attendance: {attend:.0%}")
st.write(f"- Assignments: {assign:.0%}")

# Prediction
if st.button("🎯 Predict Final Grade", type="primary"):
    with st.spinner("Predicting..."):
        # Prepare data for prediction
        X_pred = pd.DataFrame([[study, sleep, attend, assign]],
                            columns=["study_hours_per_week", "sleep_hours_per_day",
                                   "attendance_percentage", "assignments_completed"])
        
        # Prediction
        grade = model.predict(X_pred)[0]
        
        # Limit grade between 0 and 100
        grade = max(0, min(100, grade))
        
        # Determine status
        if grade >= 85:
            status = "🎉 Excellent!"
            color = "green"
        elif grade >= 70:
            status = "✅ Good"
            color = "blue"
        elif grade >= 60:
            status = "⚠️ Needs Improvement"
            color = "orange"
        else:
            status = "❌ At Risk"
            color = "red"
        
        # Display results
        st.subheader("📈 Prediction Results")
        
        # Progress bar for visual representation
        st.progress(grade/100)
        
        # Final grade display
        st.metric(
            label="**Predicted Final Grade**",
            value=f"{grade:.1f}/100",
            delta=status,
            delta_color=color
        )
        
        # Recommendations based on grade
        st.subheader("💡 Recommendations")
        if grade >= 85:
            st.success("Keep up the great work! Maintain your current study habits.")
        elif grade >= 70:
            st.info("Good performance! Consider increasing study hours slightly.")
        elif grade >= 60:
            st.warning("Focus on improving attendance and assignment completion.")
        else:
            st.error("Consider seeking academic support and improving study habits.")

# Footer
st.markdown("---")
st.markdown("*Built with Streamlit and Scikit-learn*")
