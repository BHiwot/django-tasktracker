# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project
COPY . .


# Collect static files and migrate the database
RUN python manage.py collectstatic --noinput
RUN python manage.py migrate

# Run the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
