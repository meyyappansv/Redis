import redis
import os

r = redis.Redis(host='ec2-54-235-235-122.compute-1.amazonaws.com',port='6379')

user = {"name":"meyyappan","age":"38", "race":"asian"}
user1 = {"name":"hari", "age":"38", "race":"asian"}
r.hmset('user:info',user)
r.hmset('user:info',user1)
print "The user info: " + str(r.hgetall('user:info'))

print r.hmget('user:info','name','age')