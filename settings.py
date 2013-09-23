# *************Master  Addr  info******************#
Master_Ip = '10.1.6.10'
Master_Port = 60010

# **********Regionserver  Addr  info***************#
RegionServer_Ip = '10.1.6.12'
RegionServer_Port = 60030

# *************pid and log file********************#
PID = 'getHBaseJMX.pid'
LOGFILE = 'getHBaseJMX.log'

# ************Master Metric Config******************#
# DEFAULT_CONTENT_TYPE =>
# Master_Metric={group1:[Metric1,Metric2,Metric3.....],group2:[Metric1,.....]
Master_Metric = {'MasterStatistics': ['splitTimeAvgTime', 'cluster_requests'],
                 'RPCStatistics': ['getAvgTime', 'multiAvgTime', 'putAvgTime']}

# ************Master Metric Config******************#
# DEFAULT_CONTENT_TYPE =>
# Metric={group1:[Metric1,Metric2,Metric3.....],group2:[Metric1,.....]


# ************Metric Save into MySQL****************#
MySQL_Metric = [
    'MasterStatistics.splitTimeAvgTime', 'MasterStatistics.cluster_requests',
    'RPCStatistics.getAvgTime', 'RPCStatistics.multiAvgTime', 'RPCStatistics.putAvgTime']

# ****************MySql config**********************#
MySql_HOST = 'localhost'
MySql_USER = 'root'
MySql_PASS = 'root'
MySql_PORT = 3306

DATABASE = 'hbase'
MasterMetricTable = 'masterMetric'
AUTOINCID = 'id'
