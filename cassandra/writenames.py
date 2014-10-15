#!/usr/bin/python
# here is how you set up Cassandra on your local machine. 
# http://datafireball.com/2014/10/15/cassandra-tutorial/
recordNumber = 100000

from cassandra.cluster import  Cluster
cluster = Cluster()
session = cluster.connect('mykeyspace')

cqlTemplate = """
INSERT INTO mykeyspace.mytable ('firstname', 'lastname', 'ssn') VALUES ('fn{0}', 'ln{0}', {0})
"""

for i in range recordNumber:
	session.execute(cqlTemplate.format(str(i)))

print 'finished'
