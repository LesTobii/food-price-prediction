# Food Price Forecasting 

Food Price Forecasting is a machine learning project designed to predict future food prices based on historical data (2017–2021).  
The model was trained using PyCaret’s regression module with LightGBM, and the predictions are served through a clean, interactive Streamlit dashboard.

The current version focuses on offline-trained models — predictions are precomputed and read from CSV files to ensure fast and reproducible deployment.  
The app is fully containerized with Docker for easy deployment across environments.

---

## Overview

Food prices have a direct impact on both household economics and national policy.  
FFP provides a practical, visual way to explore and understand historical price trends and forecasts using machine learning.  

This repository demonstrates:
- Data cleaning and feature exploration  
- Model training using PyCaret  
- LightGBM regression for price prediction  
- Streamlit web app interface  
- Dockerized deployment  



---

## How to Run the App


OPTION 1  (Recommended)
Run the app using Docker — no Python installation required.

Steps:
1. Install [Docker Desktop](https://www.docker.com/products/docker-desktop/).
2. Open your terminal or PowerShell in the project folder.
3. Copy and paste these commands(in the quotes): 

- "docker build -t ffp-app ."
- "docker run -p 8501:8501 ffp-app"

4. When it finishes, open your browser and go to:
 http://localhost:8501

OPTION 2 

Steps:

1. Make sure Python 3.10+ is installed.

2. Open your terminal or PowerShell in the project folder.

3. Install everything using:
pip install -r requirements.txt

4.Then run the app with:
streamlit run app.py

5. It will open automatically in your browser at:
http://localhost:8501

----------------------------------------------------------------------------
Roadmap / Future Work

The next stage of FFP will make it smarter, live-connected, and production-ready.

Core Upgrades

Integrate live price feeds via API for real-time tracking.

Add a FastAPI or Flask backend to serve predictions through REST endpoints.

Store and retrieve data from a cloud database.

Deployment & Scaling

Deploy to cloud for public access

Add CI/CD pipelines for seamless updates.

Schedule automated retraining as new data arrives.
