import redis
import os

r = redis.Redis(host='ec2-54-235-235-122.compute-1.amazonaws.com',port='6379')
r.set('first:key', '10')

print r.get('first:key')
print "\n"
r.set('users:meyyappan', 'My first')

print r.get('users:meyyappan')
print "\n"
r.append('users:meyyappan','car is mitsubishi')

print "After append: " + r.get('users:meyyappan')
print "\n"

r.set('range:test','ABCDEF' )

print "Substring: "  + r.getrange('range:test',1,1)

