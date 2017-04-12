#  coding :utf-8
import xlrd
import xlwt
import SpiderCompanycode
class xlsCompanyInfo:
    def __init__(self):
        print "begin..."
    def GetData(self):
        data = xlrd.open_workbook("B.xlsx")
        table = data.sheet_by_name(u"Sheet1")
        workBook = xlwt.Workbook()
        sheet = workBook.add_sheet("Sheet1", cell_overwrite_ok=True)
        nrows = table.nrows
        n = 1
        while(n < 52):
            companyCode = table.cell(n, 0).value
            companyName = table.cell(n, 1).value
            companyCode = int(companyCode)
            companyCode = str(companyCode)
            SpiCompanycode = SpiderCompanycode.SpiderCompanycode(companyCode)
            address = SpiCompanycode.GetString()
            print companyCode, companyName, address
            n += 1
            sheet.write(n, 0, companyCode.decode("ascii"))
            sheet.write(n, 1, companyName)
            sheet.write(n, 2, address.decode("utf-8"))
        workBook.save("B.xls")
xlsCompanyInfo = xlsCompanyInfo()
xlsCompanyInfo.GetData()