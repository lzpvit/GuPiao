# -*- coding: utf-8 -*-
import MySQLdb
# import types
import xlrd
class MysqlControl:
    def __init__(self, host, user, passwd, db, port):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.db = db
        self.port = port
    def GetConnect(self):
        try:
            conn = MySQLdb.connect(host=self.host, user=self.user, passwd=self.passwd, db=self.db, port=self.port, charset="utf8")
            cursor = conn.cursor()
            cursor.execute("create table companyInfo(id INT PRIMARY KEY ,name VARCHAR (20),code INT , address VARCHAR(100) ,locationX FLOAT (20),locationY FLOAT (20))")
            data = xlrd.open_workbook(u"BGU.xls")
            sheet = data.sheet_by_name("Sheet1")
            n = 0
            while(n <51):
                companyCode = sheet.cell(n, 0).value.encode("utf-8")
                companyName = sheet.cell(n, 1).value.encode("utf-8")
                companyAddress = sheet.cell(n, 2).value.encode("utf-8")
                #companyAddress = "ggmyfriend"
                locationX = sheet.cell(n, 3).value
                locationY = sheet.cell(n, 4).value
                # nn = str(n)
                sqli = "insert into companyInfo values(%s,%s,%s,%s,%s,%s)"
                ns = str(n)
                code = str(companyCode)
                x = str(locationX)
                y = str(locationY)
                cursor.execute(sqli, (ns, companyName, code, companyAddress, x, y))
                n += 1
            cursor.execute("select name from companyInfo")
            data = cursor.fetchall()
            print data
            for x in data:
                print x[0]
            cursor.close()
            conn.commit()
            conn.close()
        except MySQLdb.Error, e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])
lzp2 = MysqlControl("localhost", "root", 'root', "lzp1", 3307)
lzp2.GetConnect()
