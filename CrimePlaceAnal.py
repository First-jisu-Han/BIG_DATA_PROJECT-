import requests
import pandas as pd
from bs4 import BeautifulSoup
import csv
import json





# 공공데이터 인증키+오픈API 가져오기 
# 범죄 발생 장소의 데이터 추출 
urlList=[]
urlList.append("https://api.odcloud.kr/api/15054737/v1/uddi:6d076c9e-fbfe-47d1-8c3e-b2f84a2a56c4?page=1&perPage=10&serviceKey=jGRnEP%2FmMvJx1xoDf7VVRaEKZHYagcn%2BiAgUGpY4SqyT8diNLCkfHgqOfsbYNXpoRw3XnwQQQwdO23DO2ju8Og%3D%3D")
urlList.append("https://api.odcloud.kr/api/15054737/v1/uddi:5810d736-6b35-472e-972b-864cd4770312?page=1&perPage=10&serviceKey=jGRnEP%2FmMvJx1xoDf7VVRaEKZHYagcn%2BiAgUGpY4SqyT8diNLCkfHgqOfsbYNXpoRw3XnwQQQwdO23DO2ju8Og%3D%3D")
urlList.append("https://api.odcloud.kr/api/15054737/v1/uddi:a2948aec-3b5a-4b08-8333-e805a7d88c52?page=1&perPage=10&serviceKey=jGRnEP%2FmMvJx1xoDf7VVRaEKZHYagcn%2BiAgUGpY4SqyT8diNLCkfHgqOfsbYNXpoRw3XnwQQQwdO23DO2ju8Og%3D%3D")
urlList.append("https://api.odcloud.kr/api/15054737/v1/uddi:35155cd5-2f9d-422d-b34d-a8089e9d1eb7?page=1&perPage=10&serviceKey=jGRnEP%2FmMvJx1xoDf7VVRaEKZHYagcn%2BiAgUGpY4SqyT8diNLCkfHgqOfsbYNXpoRw3XnwQQQwdO23DO2ju8Og%3D%3D")
urlList.append("https://api.odcloud.kr/api/15054737/v1/uddi:ec2882d0-3705-47f5-9e19-93a79ca36e7f?page=1&perPage=10&serviceKey=jGRnEP%2FmMvJx1xoDf7VVRaEKZHYagcn%2BiAgUGpY4SqyT8diNLCkfHgqOfsbYNXpoRw3XnwQQQwdO23DO2ju8Og%3D%3D")
urlList.append("https://api.odcloud.kr/api/15054737/v1/uddi:22c0720d-460f-4f72-bed5-c300b994df29?page=1&perPage=10&serviceKey=jGRnEP%2FmMvJx1xoDf7VVRaEKZHYagcn%2BiAgUGpY4SqyT8diNLCkfHgqOfsbYNXpoRw3XnwQQQwdO23DO2ju8Og%3D%3D")
urlList.append("https://api.odcloud.kr/api/15054737/v1/uddi:db96f650-e7f0-47b8-acb4-95ec82856dc7?page=1&perPage=10&serviceKey=jGRnEP%2FmMvJx1xoDf7VVRaEKZHYagcn%2BiAgUGpY4SqyT8diNLCkfHgqOfsbYNXpoRw3XnwQQQwdO23DO2ju8Og%3D%3D")
urlList.append("https://api.odcloud.kr/api/15054737/v1/uddi:d7bd369c-6160-48b9-aa0c-aa4845a8bb67?page=1&perPage=10&serviceKey=jGRnEP%2FmMvJx1xoDf7VVRaEKZHYagcn%2BiAgUGpY4SqyT8diNLCkfHgqOfsbYNXpoRw3XnwQQQwdO23DO2ju8Og%3D%3D")
# 일일이 직접 입력하지 않기 위해서 반복문으로 구성해보았음. 
rq=[]
for i in range(len(urlList)):
    rq.append(requests.get(urlList[i]))
soup=[]
for i in range(len(rq)):
    soup.append(BeautifulSoup(rq[i].text, "html.parser"))        # html로 이루어진 데이터들 파싱 
# for i in range(len(soup)):
#     print(soup[i])

response=[]
for i in range(len(soup)):
    response.append(soup[i].text)

# response=soup.text
# response2=soup2.text
# response3=soup3.text 

json_ob=[] 
print(len(response))

for i in range(len(response)):
    json_ob.append(json.loads(response[i]))

data=[]
for i in range(len(json_ob)):
    data.append(json_ob[i]["data"])

print(data[0])

crime=[]
crimeInformation=[]

# data는 10개의 딕셔너리로 이루어져있기 
# 때문에 각 딕셔너리를 순회하며 범죄-빈도를 각 리스트에 저장한다.
for i in range(len(data)):
    for j in range(len(data[i])):
        for key, val in (data[i][j]).items():
            crime.append(key)
            crimeInformation.append(val)

# 범죄와 빈도 데이터들을 칼럼으로 대응시켜 저장 
dict={'crime': crime ,'crime_information':crimeInformation}     # panda 라이브러리 이용해서 csv로 저장한다. 
df=pd.DataFrame(dict)
df.to_csv("crimes3.csv")
        