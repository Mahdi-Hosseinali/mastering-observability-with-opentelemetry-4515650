# Use the official Python 3.12 image as the base image
FROM python:3.12

# Set the working directory
WORKDIR /app

# Copy requirements.txt
COPY requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port the app runs on
EXPOSE 3010

# Command to run the application
CMD ["flask", "run", "-h", "0.0.0.0", "-p", "3010"]
