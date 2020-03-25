#! /usr/bin/python3
# -*- coding:utf-8 -*-

import xlrd

goods_id = 0
goods_name = 1
goods_pic = 2
goods_price = 5
goods_taokouling = 12
goods_youhuiquan = 19
goods_discount = 15
json = {};
datas = [];

def readexcel():
    workbook = xlrd.open_workbook('./tbk.xls')
    sheetNames = workbook.sheet_names()
    sheet = workbook.sheet_by_name(sheetNames[0]) #get the page
    nrows = sheet.nrows #get row
    ncols = sheet.ncols #get col
    position = 1
    while position < nrows:
        name = sheet.cell(position,goods_name).value;
        save_name = name.replace("'",' ')
        item = { \
        "goods_id":sheet.cell(position,goods_id).value,
        "goods_name":save_name, \
        "goods_pic":sheet.cell(position,goods_pic).value, \
        "goods_price":sheet.cell(position,goods_price).value, \
        "goods_taokouling":sheet.cell(position,goods_taokouling).value, \
        "goods_youhuiquan":sheet.cell(position,goods_youhuiquan).value, \
        "goods_discount":sheet.cell(position,goods_discount).value}
        datas.append(item)
        position = position+1;
    json = {'datas':datas}
    jsonStr = str(json)
    
    with open('./tbk_goods.txt','a') as file_handle:
        file_handle.write(jsonStr)

if __name__ == '__main__':
    readexcel()
    
