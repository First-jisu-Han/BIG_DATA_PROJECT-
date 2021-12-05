import requests
import pandas as pd
from bs4 import BeautifulSoup
import csv
import json

# 공공데이터 인증키+오픈API 가져오기 
# 범죄 발생 장소의 데이터 추출 

urlList=[]
urlList.append("https://api.odcloud.kr/api/15063818/v1/uddi:04d5cc76-463a-4559-87c7-df3a690d59e9?page=1&perPage=1000&serviceKey=jGRnEP%2FmMvJx1xoDf7VVRaEKZHYagcn%2BiAgUGpY4SqyT8diNLCkfHgqOfsbYNXpoRw3XnwQQQwdO23DO2ju8Og%3D%3D")

rq=[]
for i in range(len(urlList)):
    rq.append(requests.get(urlList[i]))

soup=[]
for i in range(len(rq)):
    soup.append(BeautifulSoup(rq[i].text, "html.parser"))        # html로 이루어진 데이터들 파싱

print(soup) 


response=[]
for i in range(len(soup)):
    response.append(soup[i].text)

json_ob=[] 

for i in range(len(response)):
    json_ob.append(json.loads(response[i]))

print(len(json_ob))

data=[]
for i in range(len(json_ob)):
    data.append(json_ob[i]["data"])


crimePlace=[]
crimeCnt=[]


for i in range(len(data)):
    for j in range(len(data[i])):
        for key, val in (data[i][j]).items():   # value 값만 따서 crimeInformation에 저장했다. 
            crimePlace.append(key)
            crimeCnt.append(val)


dict={'crime_place':crimePlace,'crime_cnt':crimeCnt }     # panda 라이브러리 이용해서 csv로 저장한다. 
df=pd.DataFrame(dict)
df.to_csv("crimeSeoul.csv")


        