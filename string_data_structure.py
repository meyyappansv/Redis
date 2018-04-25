import redis
import os

r = redis.Redis(host='ec2-54-235-235-122.compute-1.amazonaws.com',port='6379')
r.set('first:key', '10')

print r.get('first:key')