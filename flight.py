from selenium import webdriver
from bs4 import BeautifulSoup
import os,xlwt

chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
browser = webdriver.Chrome(chromedriver)

## 获取航班信息
def getinfo(rowId,flightNo):
    url = "https://flightaware.com/live/flight/" + flightNo
    browser.get(url)
    html = browser.page_source
    soup = BeautifulSoup(html, 'lxml')
    #name = soup.find("span", class_="flightPageAirlineCallsign").text
    name = ""
    departCity = soup.find("span", class_="flightPageSummaryCity").text
    arriveCity = soup.find("span", class_="destinationCity").text
    #departTime = soup.find("span", class_="flightPageSummaryDeparture").text
    departTime = soup.find("div", class_="flightPageDataAncillaryText").text
    #arriveTime = soup.find("span", class_="flightPageSummaryArrival").text
    arriveTime = soup.find("div", class_="flightPageDataAncillaryText").text
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
'UA1002',
'UA1003',
'UA1005',
'UA1009',
'UA1015',
'UA1018',
'UA1047',
'UA1052',
'UA1054',
'UA1055',
'UA1057',
'UA1059',
'UA1065',
'UA1087',
'UA1094',
'UA1095',
'UA1098',
'UA1109',
'UA1116',
'UA1133',
'UA1137',
'UA1140',
'UA1143',
'UA1146',
'UA1148',
'UA1149',
'UA1150',
'UA1154',
'UA116',
'UA1165',
'UA1166',
'UA1169',
'UA1173',
'UA1176',
'UA1200',
'UA1223',
'UA1226',
'UA1241',
'UA1244',
'UA1248',
'UA1249',
'UA1251',
'UA1254',
'UA1260',
'UA1264',
'UA1265',
'UA1266',
'UA1268',
'UA1276',
'UA1278',
'UA1406',
'UA1413',
'UA1415',
'UA1419',
'UA1434',
'UA1447',
'UA1469',
'UA1478',
'UA1483',
'UA1499',
'UA1502',
'UA1503',
'UA1523',
'UA1526',
'UA1527',
'UA1530',
'UA1537',
'UA1544',
'UA1546',
'UA1555',
'UA1563',
'UA1565',
'UA1567',
'UA1568',
'UA1583',
'UA1584',
'UA1585',
'UA159',
'UA1596',
'UA1597',
'UA1600',
'UA1613',
'UA1614',
'UA1615',
'UA1631',
'UA1633',
'UA1639',
'UA1647',
'UA1651',
'UA1655',
'UA1657',
'UA1659',
'UA1666',
'UA1691',
'UA1710',
'UA1711',
'UA1730',
'UA1735',
'UA1739'
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

