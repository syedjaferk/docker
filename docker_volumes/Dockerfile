# Use the official Python image.
FROM python:3.9-slim
 
# Set the working directory in the container
WORKDIR /app
 
# Copy the current directory contents into the container at /app
COPY . /app
 
# Install any needed packages specified in requirements.txt
RUN pip install flask
 
# Make port 5002 available to the world outside this container
EXPOSE 5002
 
# Define environment variable
ENV NAME dev-service
 
# Run dev_service.py when the container launches
CMD ["python", "dev_service.py"]
