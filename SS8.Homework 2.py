from bs4 import *
from flask import *
import urllib.request

# class Hot_News:
#     def __init__(self, title, link):
#         title = self.title
#         link = self.link

with urllib.request.urlopen('http://dantri.com.vn/giao-duc-khuyen-hoc.htm') as response:
    html = response.read()

    soup = BeautifulSoup(html, "html.parser")

    # div_1 = soup.find("div", "mt3 clearfix")
    # print(div_1.a.img["src"])
    # print(div_1.a["title"])
    # print(div_1.div.div.string)
    #
    div_2 = soup.find("div", "clearfix")
    div_list = soup.find_all("div", "mt3 clearfix")
    for div_key in div_list:
        print("Link ảnh: ",div_key.a.img["src"])
        print("Title: ",div_key.a["title"])
        dong = div_key.div.div
        dong2 = str(dong)
        list1 = dong2.split(">")
        list2 = list1[1].split("</b")
        print ("Short Description:"+ list2[0])
        print()



