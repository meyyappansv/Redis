import redis
import os

r = redis.Redis(host='ec2-54-235-235-122.compute-1.amazonaws.com',port='6379')

user = {"name":"meyyappan","age":"38", "race":"asian"}
r.hmset('user:info',user)
print "The user info: " + r.hgetall('user:info')

