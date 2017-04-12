# -*- coding: UTF-8 -*-
import json
import urllib2
import xlrd
import xlwt
import request
import time
def GetCoordinate(address):
    ak ="aYgl4fDBNiU4GUsScGOhaupjqSQwOTuN"
    ur = "http://api.map.baidu.com/geocoder/v2/?address="
    addr = address
    output ="json"
    url= ur+addr+"&output="+output+"&ak="+ak
    temp = urllib2.urlopen(url)
    temp = json.loads(temp.read())
    result = temp['result']
    location = result['location']
    lat = location['lat']
    lng = location['lng']
    locationTuple = (lat, lng)
    return locationTuple

def WriteCoordinate():
    data = xlrd.open_workbook("BG.xls")
    aSheet =data.sheet_by_name(u"Sheet1")
    workBook = xlwt.Workbook()
    sheet = workBook.add_sheet(u"Sheet1",cell_overwrite_ok=True)
    n = 0
    while(n< 51):
        companyCode = aSheet.cell(n, 0).value
        companyName = aSheet.cell(n, 1).value
        companyAddress = aSheet.cell(n, 2).value
        if(companyAddress == "none"):
            locationTupleX = "none"
            locationTupleY = "none"
        else:
            locationTupleX = GetCoordinate(companyAddress.encode("utf-8"))[0]
            locationTupleY = GetCoordinate(companyAddress.encode("utf-8"))[1]
        sheet.write(n, 0, companyCode)
        sheet.write(n, 1, companyName)
        sheet.write(n, 2, companyAddress)
        sheet.write(n, 3, locationTupleX)
        sheet.write(n, 4, locationTupleY)
        print locationTupleX, locationTupleY, companyName
        n += 1
    workBook.save("BGU.xls")
s = GetCoordinate("北京市142信箱41分箱北京市海淀区永定路甲51号数控大楼北楼518室(快递地址)(100854)")
print s
a = WriteCoordinate()
print "yes all down"
