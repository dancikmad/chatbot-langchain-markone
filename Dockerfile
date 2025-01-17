FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 8501

# Run the Streamlit app
ENTRYPOINT ["streamlit", "run", "bot/app.py", "--server.port=8501", "--server.address=0.0.0.0"]