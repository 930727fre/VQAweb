FROM python:3.12-slim

# Set working directory inside container
WORKDIR /app

# Copy only requirements.txt to install dependencies
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# The CMD will run the main.py script, which is mounted via -v
# CMD ["python3", "demo.py"]
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3000"]
