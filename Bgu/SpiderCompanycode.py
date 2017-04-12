# coding : utf-8
from selenium import webdriver
from bs4 import BeautifulSoup
import time
class SpiderCompanycode:
    def __init__(self, Companycode):
        self.Companycode = Companycode
    def GetString(self):
        driver = webdriver.PhantomJS()
        Url="http://www.sse.com.cn/assortment/stock/list/info/company/index.shtml?COMPANY_CODE="+self.Companycode
        driver.get(Url)
        time.sleep(8)
        soup = BeautifulSoup(driver.page_source, 'lxml')
        con = soup.find("div", id="tableData_stockListCompany")
        co = con.find("div")
        cs = co.find_next_sibling("div")
        tbody = cs.table.tbody
        tr = tbody.find("tr")
        n = 0
        while n < 7:
            tr = tr.find_next_sibling("tr")
            n += 1
        td = tr.td
        tdString = td.string
        driver.quit()
        # print tdString.encode("utf-8")
        return tdString.encode("UTF-8")
# SpiderCompanycode = SpiderCompanycode("600012")
# SpiderCompanycode.GetString()

