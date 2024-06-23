# Use an official Python runtime as a parent image
FROM python:3.12.4-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the root
COPY requirements.txt .

# Copy the current directory contents into the container at /app as well
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run main.py when the container launches, as it is contained under the app folder, we define app.main
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
