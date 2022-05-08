"""

--------------------------------------------------------------
Crawl website varzesh3.com and save it to csv file.

(C) 2022 Saeed Mirzamohammadi, Qazvin, Iran

Email: saeed1843mirzamohammadi@gmail.com

Id telegram : @e_l_f_5_5_5

2022/4/30
--------------------------------------------------------------

"""




import requests
from bs4 import BeautifulSoup as bs
import asyncio
from asyncio import *
import pandas as pd
from colorama import Fore,init



async def crawl(File_storage_location:str):

    init()
    print("\n"+Fore.MAGENTA+" started the crawl \n")
    print(Fore.BLUE+" wait...")


    dic_of_data={"title":[],"content":[],"visit":[],"time":[]}
    data=pd.DataFrame(dic_of_data)
    # make dataframe

    list_of_title=[]
    list_of_content=[]
    list_of_visit=[]
    list_of_time=[]

    for page_number in range(1821200,1822117):         #From the news , Until the news
        try:
            url="https://www.varzesh3.com/news/"
            response=requests.get(url+str(page_number)) 
            page=bs(response.content,"html.parser")

            title=page.find("h1",class_="headline").get_text()
            # the end title

            info_content=page.find("div",class_="news-text").get_text()
            separate_content=info_content.replace("\n","")
            separate1_content=separate_content.replace("\u200c","")
            content=separate1_content.replace("\xa0","")
            # the end content

            info_visit=page.find("div",class_="news-info").get_text()
            separate_visit=info_visit.split("\n")[3]
            separate1_visit=separate_visit.split(" ")[0]
            visit=separate1_visit.replace(",","")
            # the end visit

            info_time=page.find("div",class_="news-info").get_text()
            separate_time=info_time.split("\n")
            time=separate_time[2]
            # the end time

            list_of_title.append(title)
            list_of_content.append(content)
            list_of_visit.append(visit)
            list_of_time.append(time)
            # end of transferring lists



        except AttributeError:
            continue


    data["title"]=list_of_title
    data["content"]=list_of_content
    data["visit"]=list_of_visit
    data["time"]=list_of_time
    # End of transfer to data

    data.to_csv(f"{File_storage_location}.csv",encoding="utf-8-sig")

    


if __name__=="__main__":
    asyncio.run(crawl("F:\\saeed\\varzesh3"))     #your path file  "F:\\newfolder\\""
    