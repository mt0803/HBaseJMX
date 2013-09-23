import logging
import os
from settings import LOGFILE

logfilePath = os.path.dirname(__file__) + '/' + LOGFILE

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s %(name)s[%(process)d] %(levelname)s - %(message)s",
    filename=logfilePath)
logger = logging.getLogger("parseHBaseJMX")

# --------------------------------------------------
# jmxInfo:dict , metricGroup:string, metricname:list
# jmxInfo: all jmx info
# metricGroup: the group of metric you want to get, like 'MasterStatistics'
# metricNameList: the metric you want to get, like 'splitTimeAvgTime'
# --------------------------------------------------


def parseJMX(jmxInfo, metricGroup, metricNameList):
    groupList = jmxInfo['beans']
    result = {}
    for item in groupList:
        groupName = item['name']
        if (-1 != groupName.find(metricGroup)):
            for metric in metricNameList:
                name = metricGroup + '.' + metric
                value = item[metric]
                try:
                    result[name] = value
                except Exception, e:
                    logger.info(
                        'imput metricname: %s can not be parse', metric)
                    raise e
    return result
