import requests
import pandas as pd
from bs4 import BeautifulSoup
import csv
import json





# 공공데이터 인증키+오픈API 가져오기 
URL="https://api.odcloud.kr/api/3074462/v1/uddi:efafd73f-3310-48f8-9f56-bddc1c51f3ba_201910221541?page=1&perPage=10&serviceKey=jGRnEP%2FmMvJx1xoDf7VVRaEKZHYagcn%2BiAgUGpY4SqyT8diNLCkfHgqOfsbYNXpoRw3XnwQQQwdO23DO2ju8Og%3D%3D"

rq=requests.get(URL)
soup=BeautifulSoup(rq.text, "html.parser")         # html로 이루어진 데이터들 파싱 

print(soup)

response=soup.text
json_ob=json.loads(response)
data = json_ob["data"]
print(len(data[0]))  

region=[]
cnt=[]

# data는 10개의 딕셔너리로 이루어져있기 때문에 각 딕셔너리를 순회하며 범죄-빈도를 각 리스트에 저장한다.
for i in range(len(data)):
    for key, val in data[i].items():
        region.append(key)
        cnt.append(val)

# 범죄와 빈도 데이터들을 칼럼으로 대응시켜 저장 
dict={'city_name':region,'city_cnt':cnt}     # panda 라이브러리 이용해서 csv로 저장한다. 
df=pd.DataFrame(dict)
df.to_csv("crimes2.csv")
        



