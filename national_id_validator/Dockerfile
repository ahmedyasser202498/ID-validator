# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the rest of the application into the container
COPY . /app/

# Install dependencies from the requirements.txt file
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000 for the Django app
EXPOSE 8000

# Run the management command to generate the API key and start the server
CMD ["sh", "-c", "python manage.py generate_api_key && python manage.py runserver 0.0.0.0:8000"]

