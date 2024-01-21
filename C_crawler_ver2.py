import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import numpy as np
import os
import time
from dotenv import load_dotenv
from typing import Final
import discord

#爬取每個判決的對應ID
def get_text(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    text = soup.find_all('li')
    return text

def get_new_judgment():
    url_mainpage = "https://cons.judicial.gov.tw/judcurrentNew1.aspx?fid=38"
    text = get_text(url_mainpage)
    text = str(text)
    text = re.findall(r'/docdata\.aspx\?fid=38&amp;id=\d\d\d\d\d\d', text)

    #store the text in a list
    url_J = []
    for i in range(len(text)):
        url_J.append(text[i])
    #remove amp; in the text
    url_J = [i.replace('amp;','') for i in url_J]
    #remove the duplicate text
    url_J = list(set(url_J))
    #add address and replace the original url
    url_J = ['https://cons.judicial.gov.tw'+i for i in url_J]
    
    return url_J

def J_URL_compare():
    url_J = get_new_judgment()

    J_URL = pd.read_csv('J_URL.csv', header=None)
    #to list
    J_URL = J_URL[0].tolist()
    #sort by number
    J_URL = sorted(J_URL)
    url_J = sorted(url_J)
    #check if every url in url_J is in J_URL
    url_J = [i for i in url_J if i not in J_URL]

    #if all the url in url_J is in J_URL, return string
    if len(url_J) != 0:
        J_URL = J_URL + url_J
        J_URL = pd.DataFrame(J_URL)
                            
        #replace the original J_URL.csv
        J_URL.to_csv('J_URL.csv',index=False,header=False)
        # print(url_J)
        return url_J
    else:               
        # print("大法官還在加班！請稍後再來！")
        return "大法官還在加班！請稍後再來！"

