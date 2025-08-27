FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN apt-get update && apt-get install -y build-essential libglib2.0-0 libsm6 libxext6 libxrender1             && pip install --upgrade pip             && pip install -r /app/requirements.txt             && apt-get remove -y build-essential             && apt-get autoremove -y             && rm -rf /var/lib/apt/lists/*
COPY . /app
EXPOSE 5000
CMD ["python", "app.py"]
