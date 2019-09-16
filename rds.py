#!/usr/bin/env python
#coding=utf-8
import datetime
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkrds.request.v20140815 import DescribeResourceUsageRequest
from aliyunsdkrds.request.v20140815 import DescribeResourceUsageRequest
UTC_End = datetime.datetime.today() - datetime.timedelta(hours=8)
UTC_Start = UTC_End - datetime.timedelta(minutes=25)

StartTime = datetime.datetime.strftime(UTC_Start, '%Y-%m-%dT%H:%MZ')
EndTime = datetime.datetime.strftime(UTC_End, '%Y-%m-%dT%H:%MZ')
client = AcsClient('***', '***', 'cn-hangzhou')

request = DescribeResourceUsageRequest.DescribeResourceUsageRequest()
#request.set_accept_format('json')
request.set_DBInstanceId('rm-bp1qtk3z3g646in7e')
response = client.do_action_with_exception(request)
#request.set_action_name('DescribeDBInstancePerformance')

#request.set_query_params(dict(DBInstanceId="rm-bp1qtk3z3g646in7e",key="性能指标",StartTime="2018-05-22T15:00Z",EndTime="2018-05-22T16:00Z"))

#print(client.do_action_with_exception(request))
# python2:  print(response)
print(str(response, encoding='utf-8'))
