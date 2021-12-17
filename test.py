import logging
from cassandra.cluster import Cluster


logging.basicConfig(level=logging.INFO)


def cassandra_connection():
    """
    Connection object for Cassandra
    :return: session, cluster
    """
    cluster = Cluster(['127.0.0.1'], port=9042)
    session = cluster.connect()

    return session, cluster


if __name__ == "__main__":
    cassandra_connection()
    logging.info('Not callable')
