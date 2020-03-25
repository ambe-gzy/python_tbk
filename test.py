#! /usr/bin/python3
# -*- coding:utf-8 -*-

from readTbkTxt import(
    getJson
    )

def read():
    data = getJson();
    print("dushuju")
    dataList = str.split('{}')
    print(type(data))
    print(type(dataList))
    print(dataList)

if __name__ == "__main__":
    read()
    
