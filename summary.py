from bs4 import BeautifulSoup
import telegram
import requests
import datetime
import sys
import json

token="5228090269:AAGaMC51TzJN3a0ZCJcSGLkmib4ekgizhyk"
receiver_id=2090364215
url_1='https://www.ddaily.co.kr/news/section/?sec_no=94'

def url_extract_digitaldaily():
    req=requests.get(url_1)
    html=req.text
    soup=BeautifulSoup(html,'html.parser')
    news_list=soup.find("div",class_="mo1_arl9").find_all("dl")

    url_list=[]

    for i in news_list[:5]:
        a=i.find("dt").find("a").attrs['href']
        url_list.append("https://www.ddaily.co.kr"+a)
    
    return url_list

def content_extract(url_list):
    contents_list=[]
    for i in url_list:
        req=requests.get(i)
        html=req.text
        soup=BeautifulSoup(html, 'html.parser')
        a=soup.find("div",class_="smartOutput").get_text()
        contents_list.append(a)
    return contents_list

def title_extract_digitaldaily():
    req=requests.get(url_1)
    html=req.text
    soup=BeautifulSoup(html,'html.parser')
    news_list=soup.find("div",class_="mo1_arl9").find_all("dl")[:5]

    title_list=[]

    for i in news_list:
        a=i.find("dt").find("a").get_text()
        title_list.append(a)
    
    return title_list


u=url_extract_digitaldaily()
t=title_extract_digitaldaily()
news_content=content_extract(u)[0]



client_id="avbd9bb1q5"
client_secret="dFjpf9NCQnFkVXzPoYaLuYtIxC4JvfNNZ0hS83z5"

headers={
    "avbd9bb1q5": client_id,
    "dFjpf9NCQnFkVXzPoYaLuYtIxC4JvfNNZ0hS83z5": client_secret,
    "Content-Type": "application/json"
}

language="ko"
model="news"
tone="2"
summaryCount="3"
url="https://naveropenapi.apigw.ntruss.com/text-summary/v1/summarize"
content=news_content

data={
    "document": {
        "content": content
    },
    "option": {
        "language": language,
        "model": model,
        "tone": tone,
        "summaryCount": summaryCount
    }
}
response=requests.post(url,data=json.dumps(data),headers=headers)

rescode=response.status_code
'''if(rescode==200):
    print(response.text)
else:
    print("Error : "+ response.text)'''

print(response.json())
