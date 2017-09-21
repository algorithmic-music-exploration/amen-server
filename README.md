[![Build Status](https://travis-ci.org/algorithmic-music-exploration/amen-server.svg?branch=master)](https://travis-ci.org/algorithmic-music-exploration/amen-server.svg?branch=master) [![Coverage Status](https://coveralls.io/repos/github/algorithmic-music-exploration/amen-server/badge.svg?branch=add-coveralls)](https://coveralls.io/github/algorithmic-music-exploration/amen-server?branch=add-coveralls)

# amen-server
Server to run Amen analysis and return JSON results.


## Don't forget to talk about bucket policies!
(https://stackoverflow.com/questions/2547046/make-a-bucket-public-in-amazon-s3)


When running manually on AWS, you need to remap NGINX proxy-pass, and prefix MainHandler accordingly.
You'll also need to make secrets.py!

