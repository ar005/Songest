# Use an official Python runtime as a parent image
FROM python:3.8

# Install ffmpeg
RUN apt-get update && \
    apt-get install -y ffmpeg

# Set the working directory in the container
WORKDIR library

# Copy the current directory contents into the container at library
COPY . library

# Install any needed packages specified in requirements.txt
# (you may need to adjust this depending on your script's dependencies)
RUN pip install --no-cache-dir -r requirements.txt

# Run main.py when the container launches
CMD ["python", "main.py"]


