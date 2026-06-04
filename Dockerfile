FROM python:3.10
WORKDIR /app
COPY . . 
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000
CMD ["streamlit", "run", "app_streamlit.py", "--server.port=10000", "--server.address=0.0.0.0"]