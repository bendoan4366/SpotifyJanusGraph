from cassandra.cluster import Cluster
import sys

host = str(sys.argv[1])

if len(host) == 1:
    cluster=Cluster()
elif len(host) > 2:
    print("please specify only one argumemt - the host ip for your cassandra cluster")
    sys.exit()
else:
    cluster = Cluster(host)

session = cluster.connect()
keyspaces = session.execute(""" SELECT * FROM system_schema.keyspaces;""")

for k in keyspaces:
    print(k)