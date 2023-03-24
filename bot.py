from bs4 import BeautifulSoup
import telegram
import requests
import datetime

token="5228090269:AAGaMC51TzJN3a0ZCJcSGLkmib4ekgizhyk"
receiver_id=5228090269
url='https://www.ddaily.co.kr/news/section/?sec_no=94'

def sendMessage(chat_id,message):
    bot.sendMessage(chat_id=chat_id, text=message)

def title_extract_digitaldaily():
    req=requests.get(url)
    html=req.text
    soup=BeautifulSoup(html,'html.parser')
    news_list=soup.find("div",class_="mo1_arl9").find_all("dl")[:5]

    title_list=[]

    for i in news_list:
        a=i.find("dt").find("a").get_text()
        title_list.append(a)
    
    return "  ".join(title_list)

def content_extract_digitaldaily():
    req=requests.get(url)
    html=req.text
    soup=BeautifulSoup(html,'html.parser')
    news_list=soup.find("div",class_="mo1_arl9").find_all("dl")[:5]

    content_list=[]

    for i in news_list:
        a=i.find("dd").find("a").get_text()
        content_list.append(a)
    
    return " ".join(content_list)

def url_extract_digitaldaily():
    req=requests.get(url)
    html=req.text
    soup=BeautifulSoup(html,'html.parser')
    news_list=soup.find("div",class_="mo1_arl9").find_all("dl")

    url_list=[]

    for i in news_list[:5]:
        a=i.find("dt").find("a").attrs['href']
        url_list.append("https://www.ddaily.co.kr"+a)
    
    return url_list
    

def main():
    bot=telegram.Bot(token = token)
    news_titles=title_extract_digitaldaily()
    #news_sum=content_extract_digitaldaily()
    #new_url=url_extract_digitaldaily()
    bot.sendMessage(chat_id=receiver_id,text=news_titles)



if __name__=="__main__":
    main()