import mysql.connector
import argparse
import vespucci.graph_config as grph

__author__ = 'axel_hadfeg as axelerate'

# __CONSTANTS__
CONST_USER_FLAG = 'user'
CONST_PASSWORD_FLAG = 'password'
CONST_HOST_FLAG = 'host'
CONST_RAISE_WARNINGS_FLAG = 'raise_on_warnings'
CONST_DATABASE = 'database'


def main():

    # __PARSER__
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('input_database', type=str, help='mysql database')
    parser.add_argument('input_user', type=str, help='mysql username')
    parser.add_argument('input_password', type=str, help='mysql password')
    args = parser.parse_args()

    # __MYSQL_CONFIG__
    mysql_config = {
      CONST_USER_FLAG: args.input_user,
      CONST_PASSWORD_FLAG: args.input_password,
      CONST_HOST_FLAG: '127.0.0.1',
      CONST_DATABASE: args.input_database,
      CONST_RAISE_WARNINGS_FLAG: True
    }

    cnx = mysql.connector.connect(**mysql_config)

    curA = cnx.cursor(buffered=True)
    list_table_query = ('SHOW TABLES FROM ' + args.input_database)
    curA.execute(list_table_query)
    table_list = [row[0] for row in curA.fetchall()]
    curA.close()

    graph = []
    curB = cnx.cursor(buffered=True)
    for table in table_list:
        node_query = ('select TABLE_NAME,COLUMN_NAME,CONSTRAINT_NAME, '
                      'REFERENCED_TABLE_NAME,REFERENCED_COLUMN_NAME from '
                      'INFORMATION_SCHEMA.KEY_COLUMN_USAGE where '
                      'REFERENCED_TABLE_NAME = \'' + table + '\';')
        curB.execute(node_query)
        reference_list = [row[0] for row in curB.fetchall()]
        for reference in reference_list:
            graph.append((reference, table))
    curB.close()

    # GRAPH_DRAWER
    grph.draw_graph(graph)
    cnx.close()

if __name__ == 'vespucci':
    main()
