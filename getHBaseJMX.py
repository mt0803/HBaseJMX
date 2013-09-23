import httplib
import json
import os
import logging
from parseHBaseJMX import parseJMX
from settings import Master_Metric, LOGFILE
from settings import MySQL_Metric, MasterMetricTable
from mySql_Client import MySql_Client
from threading import Thread

logfilePath = os.path.dirname(__file__) + '/' + LOGFILE

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s %(name)s[%(process)d] %(levelname)s - %(message)s",
    filename=logfilePath)
logger = logging.getLogger("getHBaseJmx")


def getHBaseJmx(ip, port):
    conn = httplib.HTTPConnection(ip, port, timeout=30)
    conn.request('GET', '/jmx')
    response = conn.getresponse()
    status = response.status
    if (200 == status):
        jmxData = response.read()
        return jmxData
    else:
        return ''


def Jmx_test(master_Metric):
    fileHandle = open('10.jmx')
    jmxJsData = fileHandle.read()
    fileHandle.close()

    jmxPyData = json.loads(jmxJsData)
    result = {}

    for group in master_Metric:
        metricList = master_Metric[group]
        result.update(parseJMX(jmxPyData, group, metricList))

    for key in result:
        print 'key=%s, value=%d' % (key, result[key])


def Jmx_report_test(master_Metric):
    fileHandle = open('10.jmx')
    jmxJsData = fileHandle.read()
    fileHandle.close()

    jmxPyData = json.loads(jmxJsData)
    result = {}

    for group in master_Metric:
        metricList = master_Metric[group]
        result.update(parseJMX(jmxPyData, group, metricList))

    return result


class HBaseJMXtoMysqlThread(Thread):

    def run(self):
        try:
            i = 0
            while i < 10:
                self.jmxObtain()
                self.jmxParse(Master_Metric)
                self.Jmx_Mysql(MySQL_Metric, self.result)
                i += 1
        except Exception, e:
            logger.error('get HBase Jmx info  thread error...')
        finally:
            mysql_client.close_mysql()

    # get the jmxInfo
    def jmxObtain(self):
        fileHandle = open('10.jmx')
        self.jmxJsData = fileHandle.read()
        fileHandle.close()

    # parse the jmxInfo, get a dict, like {metric:value,...}
    def jmxParse(self, master_Metric):
        jmxPyData = json.loads(self.jmxJsData)
        self.result = {}
        for group in master_Metric:
            metricList = master_Metric[group]
            self.result.update(parseJMX(jmxPyData, group, metricList))

    # in order to the config,choose metrics save into mysql
    def Jmx_Mysql(self, mysql_list, metric_dict):
        self.value = []
        for metric in mysql_list:
            self.value.append(metric_dict[metric])
        print self.value
        mysql_client.insert_mysql(MasterMetricTable, self.value)


def initMySql():
    global mysql_client
    mysql_client = MySql_Client()
    mysql_client.connect_mysql()


def main():
    initMySql()
    getHbaseJMXThread = HBaseJMXtoMysqlThread()
    getHbaseJMXThread.start()

if __name__ == '__main__':
    # Jmx_test(Master_Metric)
    # Jmx_Mysql(MySQL_Metric, Jmx_report_test(Master_Metric))
    main()
