# Unsure if this is correct!
# This should allow us to no need to install numpy, etc
FROM continuumio/anaconda3

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install gcc for Resampy
RUN apt-get update && apt-get -y install gcc && rm -rf /var/lib/apt/lists/*

# Conda magic
# /opt/conda/lib/python3.6/site-packages
RUN pip install -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Run redis, the queue worker, and the tornado app when the container launches!
## Need to make this!
CMD ["python", "server.py"]
