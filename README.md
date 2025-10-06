# 🎓 Student Success AI Predictor

A simple machine learning project that predicts student success based on study habits, sleep hours, and other factors.  
This was my **first AI project**, written from scratch in Google Colab — a beginner-friendly start toward understanding data preprocessing, visualization, and modeling.  

---

## 🚀 Overview

This project analyzes how factors such as **study hours**, **sleep hours**, and **parental education** influence a student's final grade.  
The model tries to classify students as **successful** or **less successful** based on their academic behavior and habits.

---

## 🧠 Data Preprocessing

### 🔹 Handling Missing and Invalid Data
Our null values only appeared in the **parents’ education** column.  
Although we could ignore them, we decided to **replace missing values** to prevent possible future errors if new data includes blanks.

### 🔹 Feature Observations
- Students who **study more hours per week** and **complete more assignments** tend to receive **higher final grades**.  
- By setting the success boundary at **70**, the number of successful and less successful students becomes roughly balanced.  
- This balance makes the comparison between the two groups clearer.

---

## 📊 Data Insights

- The relationship between **study hours** and **final grades** shows a strong positive trend.  
- **Sleep hours** also play an important role — moderate sleep correlates with better performance.  
- On the other hand, **student participation** doesn’t show a clear pattern and might not be a strong predictor.

These findings guided the feature selection for the model.

---

## ⚙️ Model and App Files

- `student_success_model.pkl` → This file stores the **trained machine learning model** (basically the “brain” that remembers how to predict).
- `app.py` → A **Streamlit web app** that allows you to interact with the model via a simple web interface.  
  (To run it, you can later learn how to use:  
  ```bash
  streamlit run app.py
