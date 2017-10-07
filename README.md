[![Build Status](https://travis-ci.org/algorithmic-music-exploration/amen-server.svg?branch=master)](https://travis-ci.org/algorithmic-music-exploration/amen-server.svg?branch=master) [![Coverage Status](https://coveralls.io/repos/github/algorithmic-music-exploration/amen-server/badge.svg?branch=add-coveralls)](https://coveralls.io/github/algorithmic-music-exploration/amen-server?branch=add-coveralls)

# amen-server
Server to run Amen analysis and return JSON results.

# Running Locally
- Install amen
- Add keys and secrets to `uploaders/s3.py`
- Create your buckets and set them to public (link to aws doc)
- Build the dockerfile:  `docker build -t amen-server-test .`
- Run the dockerfile:  `docker run -p 4000:80 amen-server-test`
- Test with CURL: `curl -X POST -F "file=@amen.mp3;type=audio/mpeg" http://localhost:4000`
- Stop docker:  `docker stop $(docker ps -q)`

# Running on AWS
- Create a new machine on AWS!  (We recommend Ubuntu Server 16.04)
- Make sure port 80 is open to everyone.
- Get the server code on your machine - we recommend checking it out from Github.
- Create your buckets, set them to public, and update them in `uploaders/s3.py`
- Add your AWS keys and secrets to `uploaders/s3.py`
- Update the path for the Tornado webserver in server.py:  we recommend `/amen-server`, as that's what the below nginx config uses.
- Set up NGINX with proper ports and routes, and get it running:
  - `sudo apt-get update`
  - `sudo apt-get install nginx`
  - Add the following lines to `/etc/nginx/sites-enabled/default`, under `listen [::]:80 default_server;`:

  ```
    location /amen-server {
        proxy_pass http://localhost:4000/amen-server;
    }
  ```

  - start nginx `sudo service nginx start`
- Install Docker:  `sudo apt-get install docker.io`
- Add the current user (`ubuntu`) to the docker group, so we can run without sudo: `sudo gpasswd -a $USER docker`
- Build the dockerfile:  `docker build -t amen-server-test .`
- Run the dockerfile:  `docker run -p 4000:80 amen-server-test`
- Send a test CURL:  `curl -X POST -F "file=@amen.mp3;type=audio/mpeg" http://<your-aws-url>/amen-server`

## Some Notes On Performance
Amen is computationally heavy, and is a Python library.  It could be faster. The mean processing time for a 3:30 audio track on a AWS free-tier t2.micro is 20.5 seconds - that drops to 16.4 seconds on an AWS c4 machine.  Plan accordingly.
