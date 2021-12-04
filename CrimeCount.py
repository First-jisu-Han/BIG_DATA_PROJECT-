import requests
import pandas as pd
from bs4 import BeautifulSoup
import csv

# 지역별 범죄 발생 빈도와 종류 분석을 통한 치안 관리 효율화 

#섬범죄 데이터 - 그냥 공개 웹URL을 따와서 크롤링하여 CSV파일화 한 것 


URL="http://116.67.77.182/openapi/SOCitysStats/"     # 성범죄 데이터 URL 
rq=requests.get(URL)
soup = BeautifulSoup(rq.text, "html.parser")         # html로 이루어진 데이터들 파싱 

city_name=[]
city_count=[]
for i in soup.find_all("city-name"):                 # city_name 태그 단 것들 모두 city_name 리스트에 저장 
    city_name.append(i.text)   

for i in soup.find_all("city-count"):                # city_count 태그 단 것들 모두 city_count 리스트에 저장 
    city_count.append(i.text)

dict={'city_name':city_name,'city_cnt':city_count}     # panda 라이브러리 이용해서 csv로 저장한다. 
df=pd.DataFrame(dict)
df.to_csv("crimes.csv")


