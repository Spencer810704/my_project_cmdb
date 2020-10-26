#!/usr/bin/env python
#coding=utf-8
import json
from configparser import ConfigParser
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkcdn.request.v20180510.RefreshObjectCachesRequest import RefreshObjectCachesRequest
from aliyunsdkcdn.request.v20180510.DescribeRefreshQuotaRequest import DescribeRefreshQuotaRequest
from aliyunsdkcdn.request.v20180510.PushObjectCacheRequest import PushObjectCacheRequest


class Aliyun_CDN(object):
    def __init__(self, account):

        # 讀取配置檔
        cfg = ConfigParser()
        cfg.read("/Users/spencer/PycharmProjects/cmdb/scripts/config/account.ini")
        self.__access_id = cfg[account]['access_id']
        self.__access_secret = cfg[account]['access_secret']


        self.client = AcsClient(self.__access_id , self.__access_secret, 'cn-hangzhou')



    def purge_cdn(self, operation_type, refresh_type, url):


        # PUSH為主動推送阿里節點進行預熱
        if operation_type == 'push':
            self.request = PushObjectCacheRequest()
            self.request.set_accept_format('json')
            self.request.set_ObjectPath(url)


        # REFRESH為阿里回源服務器拉取資源
        elif operation_type == 'refresh':
            self.request = RefreshObjectCachesRequest()
            self.request.set_accept_format('json')

            if refresh_type == 'url':
                self.request.set_ObjectType("File")
                self.request.set_ObjectPath(url)

            elif refresh_type == 'dir':
                self.request.set_ObjectType("Directory")
                self.request.set_ObjectPath(url)


        try:
            response = self.client.do_action_with_exception(self.request)
            result = json.loads(response)
            return result
        except ServerException as e:
            print(e.message)
            print(e.http_status)
            return {
                "http_status": e.http_status,
                "error_code" : e.error_code,
                "message"    : e.message
            }

    def get_quota(self):

        self.request = DescribeRefreshQuotaRequest()
        self.request.set_accept_format('json')

        response = json.loads(self.client.do_action_with_exception(self.request))

        return response