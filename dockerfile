FROM python:3.9

# Define the working directory
WORKDIR /app
COPY . /app

# Running commands
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx

# Define the port to expose
EXPOSE 8501

# Execute the streamlit
CMD ["streamlit", "run", "main.py"]