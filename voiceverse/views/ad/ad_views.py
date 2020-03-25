#! /usr/bin/python3
# -*- coding:utf-8 -*-

import tornado.web
import sys
from tornado.escape import json_decode
import logging
from logging.handlers import TimedRotatingFileHandler
from datetime import datetime


#从commons中导入http_response方法
from common.commons import (
    http_response,
)

from database.readTbkTxt import (
    getJson
)

#从配置文件中导入错误码
from conf.base import (
    ERROR_CODE,
)
  
 
########## Configure logging #############
logFilePath = "log/ad/tbk_goods.log"
logger = logging.getLogger("Users")  
logger.setLevel(logging.DEBUG)  
handler = TimedRotatingFileHandler(logFilePath,  
                                   when="D",  
                                   interval=1,  
                                   backupCount=30)  
formatter = logging.Formatter('%(asctime)s \
%(filename)s[line:%(lineno)d] %(levelname)s %(message)s',)  
handler.suffix = "%Y%m%d"
handler.setFormatter(formatter)
logger.addHandler(handler)
 
 
class TbkGoodsHandle(tornado.web.RequestHandler):
    def post(self):
        try:
            #getData
            jsonStr = getJson();
            #jsonStr = "jiekouchenggong"
            http_response(self,jsonStr,0)
            #获取入参
        except:
            #获取入参失败时，抛出错误码及错误信息
            logger.info("RegistHandle: request argument incorrect")
            http_response(self,getJson(), 1003)
            return 
            
