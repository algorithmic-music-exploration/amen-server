[![Build Status](https://travis-ci.org/algorithmic-music-exploration/amen-server.svg?branch=master)](https://travis-ci.org/algorithmic-music-exploration/amen-server.svg?branch=master) [![Coverage Status](https://coveralls.io/repos/github/algorithmic-music-exploration/amen-server/badge.svg?branch=add-coveralls)](https://coveralls.io/github/algorithmic-music-exploration/amen-server?branch=add-coveralls)

# amen-server
Server to run Amen analysis and return JSON results.

# Running Locally
I think this is as simple as installing amen and then running the Dockerfile?
- Install amen
- Add keys and secrets to `s3.py` -- DON'T COMMIT THIS FILE !!
- Create your buckets and set them to public (link to aws doc)
- build the dockerfile:  `docker build -t amen-server-test .`
- run the dockerfile:  `docker run -p 4000:80 amen-server-test`
- Test CURL: `curl -X POST -F "file=@amen.mp3;type=audio/mpeg" http://localhost:4000`
- Stop docker:  `docker stop $(docker ps -q)`

# Running on AWS
Lots of steps here
- Install Amen on the machine
- Get the server code on your machine (check out from us!)
- Add keys and secrets to `s3_secrets.py`
- Create your buckets and set them to public
- Update the ports and routes in server.py
- Update MainHandler with proper route
- Set up NGINX with proper ports and rou, and get it running
- build and run the Dockerfile
- send a test CURL



## Don't forget to talk about bucket policies!
(https://stackoverflow.com/questions/2547046/make-a-bucket-public-in-amazon-s3)

When running manually on AWS, you need to remap NGINX proxy-pass, and prefix MainHandler accordingly.
You'll also need to make secrets.py!

