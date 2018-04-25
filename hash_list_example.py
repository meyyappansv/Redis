import redis
import os

r = redis.Redis(host='ec2-54-235-235-122.compute-1.amazonaws.com',port='6379')

r.hset('user:info','name','meyyappan','age','38','race','asian')
print "The user info: " + r.mhget('user:info')

