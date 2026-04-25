# 🛫 Travel Customer Churn Prediction

![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue.svg) ![Streamlit](https://img.shields.io/badge/Streamlit-1.20%2B-FF4B4B.svg) ![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Random%20Forest-brightgreen.svg)

> An end-to-end Machine Learning web application that predicts travel customer churn. Built with Python, Scikit-Learn (Random Forest), and Streamlit, it analyzes customer demographics and behavior to provide real-time churn risk assessments.

## 🌟 Live Demo
[Click here to view the live app on Streamlit Community Cloud](https://customer-churn-prediction-eomfxmy87vka4erdsx6d6y.streamlit.app/)

---

## 🎯 Project Overview
Customer churn is a critical metric for businesses, as acquiring new customers is significantly more expensive than retaining existing ones. This project provides a proactive solution for travel companies by predicting which customers are at high risk of churning (leaving) based on their travel history and demographic data. 

### ✨ Key Features
* **Interactive UI:** Built with Streamlit for a seamless, user-friendly experience.
* **Real-Time Predictions:** Instant churn prediction based on custom user inputs.
* **Probability Scoring:** Displays the exact probability of a customer staying or leaving.
* **Automated Preprocessing:** Handles label encoding for categorical variables seamlessly on the backend.

---

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Frontend/Framework:** Streamlit
* **Machine Learning:** Scikit-Learn (Random Forest Classifier)
* **Data Manipulation:** Pandas, NumPy
* **Visualization:** Matplotlib, Seaborn

---

## 📊 Dataset Information
The model is trained on the `Customertravel.csv` dataset. Key features include:
* **Age:** Age of the customer.
* **Frequent Flyer:** Whether the customer frequently books flights.
* **Annual Income Class:** Categorized as Low, Middle, or High Income.
* **Services Opted:** Number of additional services opted for by the customer.
* **Account Synced to Social Media:** Whether the customer's account is linked to their social profiles.
* **Booked Hotel Or Not:** Whether the customer booked a hotel through the service.
* **Target (Churn):** `1` (Likely to Churn) or `0` (Likely to Stay).

---

## 🚀 Local Installation & Setup

Follow these steps to run the application locally on your machine.

1. Clone the repository:
git clone https://github.com/your-username/your-repo-name.git

2. Navigate to the project directory:
cd your-repo-name

3. Install dependencies:
pip install -r requirements.txt

4. Run the Streamlit app:
streamlit run app.py

5. View the app:
Open your web browser and navigate to http://localhost:8501

---

## 📁 Repository Structure

* app.py (Main Streamlit application file)
* requirements.txt (List of Python dependencies)
* Customertravel.csv (Dataset used for training)
* Customer_Churn_Prediction.ipynb (Jupyter notebook with EDA and model training)
* README.md (Project documentation)

---

## 🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

## 📝 License
This project is MIT licensed.

---
*Developed as part of the B.Tech Gen AI 2nd Semester Final Project.*
