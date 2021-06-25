from cassandra.cluster import Cluster
import sys


def create_keyspace(cass_args):
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

def print_keyspaces(cass_args):

    host = str(sys.argv[1])

    if len(host) == 1:
        cluster = Cluster()
    elif len(host) > 2:
        print("please specify only one argumemt - the host ip for your cassandra cluster")
        sys.exit()
    else:
        cluster = Cluster(host)

    session = cluster.connect()
    keyspaces = session.execute(""" SELECT * FROM system_schema.keyspaces;""")

    for k in keyspaces:
        print(k)