# Student Success AI Predictor – v1.0

**Author:** Fatemeh Ramezanpour – 12th-grade student, Iran  
**Why this repo?**  
- I started this **only weeks after learning Python**, to **test myself**, **practise clean code**, and **build something useful** – **not for show**.  
- **Full logic, structure, and Git history are mine**; AI assistant was used **only for typing speed**.  

## What You See
- **v1.0** → student-grade predictor (72 % acc, R² = 0.53)
- **v-next** → Persian **handwriting OCR** (my own letters)
- **v-after** → **marine-litter %** from beach photos (my own camera)

## Files
- `Student-Success-AI-Predictor.ipynb` – full EDA & training
- `contentdataset_challenge1_ai.csv` – raw dataset
- `student_success_model.pkl` – trained model
- `app.py` – English Streamlit web-app
- `requirements.txt` – dependencies
- `LICENSE` – MIT

## Live Demo
[Click here](https://share.streamlit.io/Fatemeh-Ramezanpour-AI/student-success-ai-predictor/main/app.py)

## How to Run Locally
```bash
git clone https://github.com/Fatemeh-Ramezanpour-AI/student-success-ai-predictor.git
cd student-success-ai-predictor
pip install -r requirements.txt
streamlit run app.py
