from cassandra.cluster import Cluster
import sys

cass_args = sys.argv

if len(cass_args) == 2:
    cluster=Cluster()
elif len(cass_args) > 3:
    print("please specify only two arguments - the name of your keyspace FIRST and then the host ip for your cassandra cluster SECOND")
    sys.exit()
else:
    cluster = Cluster(cass_args[2])

session = cluster.connect()
session.execute("""CREATE KEYSPACE IF NOT EXISTS {}""".format(cass_args[1]))
