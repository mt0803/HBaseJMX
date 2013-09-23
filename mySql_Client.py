import MySQLdb
import logging
import os
from settings import LOGFILE
from settings import MySql_HOST, MySql_USER, MySql_PASS, MySql_PORT, DATABASE, AUTOINCID, MasterMetricTable

logfilePath = os.path.dirname(__file__) + '/' + LOGFILE

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s %(name)s[%(process)d] %(levelname)s - %(message)s",
    filename=logfilePath)
logger = logging.getLogger("MySql_Client")


class MySql_Client():

    def connect_mysql(self):
        try:
            self.conn = MySQLdb.connect(
                host=MySql_HOST, user=MySql_USER, passwd=MySql_PASS, port=MySql_PORT)
            self.cur = self.conn.cursor()
        except Exception, e:
            logger.error('Connect to MySql Error %d:%s' %
                         (e.args[0], e.args[1]))

    def insert_mysql(self, table, value):
        try:
            self.conn.select_db(DATABASE)
            sql = 'insert into %s ' % table
            sql += 'values(%s' % AUTOINCID
            for item in value:
                sql += ',%s'
            sql += ')'
            self.cur.execute(sql, value)
            self.conn.commit()
        except Exception, e:
            logger.error('Insert into table %s Error: %d: %s' %
                        (table, e.args[0], e.args[1]))

    def close_mysql(self):
        try:
            self.cur.close()
            self.conn.close()
        except Exception, e:
            logger.error('Close connect to mysql Error %d: %s' %
                        (e.args[0], e.args[1]))


def main():
    mc = MySql_Client()
    mc.connect_mysql()
    value1 = [1, 2, 3, 4, 5]
    value2 = [1, 2, 3, 4, 5]
    mc.insert_mysql(MasterMetricTable, value1)
    mc.insert_mysql(MasterMetricTable, value2)
    mc.close_mysql()

if __name__ == '__main__':
    main()
