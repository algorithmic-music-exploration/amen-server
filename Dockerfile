# Unsure if this is correct!
# This should allow us to no need to install numpy, etc
FROM continuumio/anaconda3

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install gcc and libsndfile
RUN apt-get update && apt-get -y install gcc
RUN apt-get -y install redis-server 
RUN apt-get -y install libsndfile1 && rm -rf /var/lib/apt/lists/*

# Install amen and redis queue
RUN pip install -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Run redis, the queue worker, and the tornado app when the container launches!
## Need to make this!
CMD ["python", "server.py"]
