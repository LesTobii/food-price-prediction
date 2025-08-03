# Use a lightweight Python image
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app2

# Copy only requirements first (for caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy only files needed for the app
COPY app2.py .
COPY ffp_model.pkl .
COPY df_engineered.csv .
COPY forecasts.csv .


# Expose Streamlit's default port
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "app2.py", "--server.port=8501", "--server.address=0.0.0.0"]
