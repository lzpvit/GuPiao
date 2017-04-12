# -*- coding: utf-8 -*-
import xlrd
import xlwt
def AdressNone():
    aData = xlrd.open_workbook("B.xls")
    aTable = aData.sheet_by_name(u"Sheet1")
    workBook = xlwt.Workbook()
    sheet = workBook.add_sheet("Sheet1",cell_overwrite_ok=True)
    n = 0
    while(n< 51):
        companyCode = aTable.cell(n+2, 0).value
        companyName = aTable.cell(n+2, 1).value
        companyAddress = aTable.cell(n+2, 2).value
        if(len(companyAddress)< 10):
            companyAddress = "none".decode("utf-8")
        sheet.write(n, 0, companyCode)
        sheet.write(n, 1, companyName)
        sheet.write(n, 2, companyAddress)
        n += 1
    workBook.save("BG.xls")
AdressNone()

