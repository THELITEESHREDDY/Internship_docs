# Use a slim, stable Python image
FROM python:3.12-slim
# Prevent Python from writing .pyc files and enable unbuffered logging
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies needed for compiling certain packages (like psycopg)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy only requirements first to leverage Docker layer caching
COPY requirements.txt .

# Install dependencies directly into the container environment
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code into the container
COPY . .

# Expose the port your API runs on (change 8000 if your framework uses a different port)
EXPOSE 8000

# Start the application using Uvicorn (adjust if your entrypoint file is named differently)
CMD ["uvicorn", "assignment.main:app", "--host", "0.0.0.0", "--port", "8000"]