import requests
import pandas as pd
from bs4 import BeautifulSoup


API_Key= "[jGRnEP%2FmMvJx1xoDf7VVRaEKZHYagcn%2BiAgUGpY4SqyT8diNLCkfHgqOfsbYNXpoRw3XnwQQQwdO23DO2ju8Og%3D%3D]"
URL= "https://api.odcloud.kr/api/3074462/v1/uddi:10bde8f1-739c-4b66-b6a6-ccf5339a658e_201910221521?page=1&perPage=10"

rq=requests.get(URL)
soup = BeautifulSoup(rq.text, "html.parser")

crimes=[]
for i in soup.find_all("data"):
    crimes.append(i)
print(crimes)

    


