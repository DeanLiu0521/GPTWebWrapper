# Use an official Python runtime as a base image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable to specify where the Flask application is
ENV FLASK_APP=app/main.py
ENV FLASK_ENV=development

# Run app.py when the container launches
CMD ["flask", "run", "--host=0.0.0.0"]
