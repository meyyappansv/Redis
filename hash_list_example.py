import redis
import os

r = redis.Redis(host='ec2-54-235-235-122.compute-1.amazonaws.com',port='6379')

user = {"name":"meyyappan","age":"38", "race":"asian"}
r.hmset('user:info',user)
print "The user info: " + str(r.hgetall('user:info'))

print "The name is {} and the age is {}" + r.hmget('user:info','name','age')