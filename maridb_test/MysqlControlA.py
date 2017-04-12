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
            # cursor.execute("create table company(id INT PRIMARY KEY ,name varchar(20),code int ,locationX float(20),locationY float(20))")
            data = xlrd.open_workbook(u"AGU.xls")
            sheet = data.sheet_by_name("Sheet1")
            n = 0
            while(n <1239):
                companyCode = sheet.cell(n, 0).value.encode("utf-8")
                companyName = sheet.cell(n, 1).value.encode("utf-8")
                companyAddress = sheet.cell(n, 2).value.encode("utf-8")
                if(companyAddress == "none"):
                    locationX= 0
                    locationY= 0
                else:
                    locationX = sheet.cell(n, 3).value
                    locationY = sheet.cell(n, 4).value
                sqli = "insert into companyInfo values(%s,%s,%s,%s,%s,%s)"
                ns = str(n+51)
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
