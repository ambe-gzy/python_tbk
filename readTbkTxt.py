#! /usr/bin/python3
# -*- coding:utf-8 -*-

import json


def getJson():
    f = open("./database/tbk_goods.txt","r",encoding = "utf-8")

    jsonStr = f.read().replace("'",'"')
    
    return jsonStr
    

if __name__ == '__main__':
    getJson()
