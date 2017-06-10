# Start with Anaconda, so we don't need to install numpy, etc
FROM continuumio/anaconda3

# Install things we need from apt
RUN apt-get update \
	&& apt-get -y install gcc \
	&& apt-get -y install redis-server \
	&& apt-get -y install libsndfile1 \
	&& apt-get -y install libav-tools \
	&& rm -rf /var/lib/apt/lists/*

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install amen and redis queue
RUN pip install -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Run redis, the queue worker, and the tornado app when the container launches!
CMD ["./run.sh"]
