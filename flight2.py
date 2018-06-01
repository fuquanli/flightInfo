from selenium import webdriver
from bs4 import BeautifulSoup
import os,xlwt

chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
browser = webdriver.Chrome(chromedriver)

## 获取航班信息
def getinfo(rowId,flightNo):
    url = "https://flightaware.com/"
    browser.get(url)
    browser.find_element_by_id("s2id_autogen1").send_keys(flightNo)
    browser.find_element_by_class_name("orange_button").click()

    html = browser.page_source
    soup = BeautifulSoup(html, 'lxml')
    #name = soup.find("span", class_="flightPageAirlineCallsign").text
    name = ""
    departCity = soup.find("span", class_="flightPageSummaryCity").text
    arriveCity = soup.find("span", class_="destinationCity").text
    departTime = soup.find("span", class_="flightPageSummaryDeparture").text
    #departTimeDiv = soup.find("div", class_="flightPageDataAncillaryText")
    #print("list(departTimeDiv.children):")
    #print(list(departTimeDiv.children))
    #print("list(departTimeDiv.descendants):")
    #print(list(departTimeDiv.descendants))
    #time = departTimeDiv.children[1].text
    arriveTime = soup.find("span", class_="flightPageSummaryArrival").text
    #arriveTime = soup.find("span", class_="flightPageDataAncillaryText").div.span.text
    insertrow(rowId,flightNo,name,departCity,arriveCity,departTime,arriveTime)

## 插入行
def insertrow(rowId,flightNo,name,departCity,arriveCity,departTime,arriveTime):
    sheet1.write(rowId,0,flightNo)
    sheet1.write(rowId,1,name.replace("\"",""))
    sheet1.write(rowId,2,departCity.replace("\n",""))
    sheet1.write(rowId,3,arriveCity.replace("\n",""))
    sheet1.write(rowId,4,departTime.replace("\n",""))
    sheet1.write(rowId,5,arriveTime.replace("\n",""))
    
workbook = xlwt.Workbook()
sheet1 = workbook.add_sheet(u"sheet1", cell_overwrite_ok=True)
sheet1.write(0,0,u'航班号')
sheet1.write(0,1,u'航空公司')
sheet1.write(0,2,u'起飞地')
sheet1.write(0,3,u'降落地')
sheet1.write(0,4,u'起飞时间')
sheet1.write(0,5,u'降落时间')

flightNoList = (
'Z2424',
'Z2425',
'Z2427',
'Z2430',
'Z2433',
'Z2437',
'Z2438',
'Z2439',
'Z2545',
'Z2546',
'Z2551',
'Z2611',
'Z2615',
'Z2622',
'Z2710',
'Z2711',
'Z27111',
'Z2712',
'Z2753',
'Z2754',
'Z2759',
'Z2761',
'Z2762',
'Z2764',
'Z2767',
'Z2768',
'Z2771',
'Z2772',
'Z2773',
'Z2775',
'Z2776',
'Z2778',
'Z2780',
'Z27800',
'Z27801',
'Z2781',
'Z2782',
'Z27820',
'Z27821',
'Z2783',
'Z2786',
'Z2791',
'Z288',
'Z2884',
'Z289',
'Z2940',
'Z2941',
'Z2942',
'Z2943',
'UA1002'
)

rowId = 1
for flightNo in flightNoList:
    try:
        getinfo(rowId,flightNo)
    except:
        print("-------------------------" + flightNo + "出现错误-------------------------")
    rowId = rowId + 1

workbook.save('test.xls')
browser.quit()

