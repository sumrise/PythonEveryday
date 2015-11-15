#!python2.7
# coding=UTF-8

# info TODO

__author__ = 'sumrise'

import practice1
import redis

r = redis.Redis(host="10.211.55.4", port=6384, db=0)

for i in range(200):
    code = practice1.generator()
    r.lpush("practice3", code)

print()
r.lrange("practice3",0,-1)

