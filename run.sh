#!/bin/bash
redis-server &
rq worker &
python server.py
