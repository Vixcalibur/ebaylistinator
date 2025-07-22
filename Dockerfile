# Use official Python base
FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Copy files
COPY . .

# Install dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Expose port
EXPOSE 8000

# Run FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
