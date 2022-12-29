import csv
import os
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup
from dataclasses import dataclass
import pandas as pd
from selenium import webdriver
from webcrawler.models import ScrapVO


class ScrapService(ScrapVO):
    def __init__(self):
        global driverpath, naver_url, savepath, encoding
        driverpath = r'C:\Users\AIA\PycharmProjects\djangoProject\webcrawler\chromedriver.exe'
        savepath = r"C:\Users\AIA\PycharmProjects\djangoProject\webcrawler\save\vs.csv"
        naver_url = "https://movie.naver.com/movie/sdb/rank/rmovie.naver"
        encoding = "UTF-8"


    def bugs_music(self, arg): # BeautifulSoup 기본크롤링
        soup = BeautifulSoup(urlopen(arg.domain + arg.query_string), 'lxml')
        title = {"class": arg.class_names[0]}
        artist = {"class": arg.class_names[1]}
        titles = soup.find_all(name=arg.tag_name, attrs=title)
        titles = [i.find('a').text for i in titles]
        artists = soup.find_all(name=arg.tag_name, attrs=artist)
        artists = [i.find('a').text for i in artists]
        [print(f"{i}위 {j} : {k}")  # 디버깅
         for i, j, k in zip(range(1, len(titles)), titles, artists)]
        diction = {}  # dict 로 변환
        for i, j in enumerate(titles):
            diction[j] = artists[i]
        arg.diction = diction
        arg.dict_to_dataframe()
        arg.dataframe_to_csv()  # csv파일로 저장

    def melon_music(self, arg): # BeautifulSoup 기본크롤링
        soup = BeautifulSoup(
            urlopen(urllib.request.Request(arg.domain + arg.query_string, headers={'User-Agent': "Mozilla/5.0"})),
            "lxml")

        title = {"class": arg.class_names[0]}
        artist = {"class": arg.class_names[1]}
        titles = soup.find_all(name=arg.tag_name, attrs=title)
        titles = [i.find('a').text for i in titles]
        artists = soup.find_all(name=arg.tag_name, attrs=artist)
        artists = [i.find('a').text for i in artists]
        [print(f"{i}위 {j} : {k}")  # 디버깅
         for i, j, k in zip(range(1, len(titles)), titles, artists)]
        diction = {}  # dict 로 변환
        for i, j in enumerate(titles):
            diction[j] = artists[i]
        arg.diction = diction
        arg.dict_to_dataframe()
        arg.dataframe_to_csv()  # csv파일로 저장



    def naver_movie_review(self):
        if os.path.isfile(savepath):
            df = pd.read_csv(savepath)
            return df.columns[0]
        else:
            driver = webdriver.Chrome(driverpath)
            driver.get(naver_url)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            all_divs = soup.find_all('div', attrs={'class', 'tit3'})
            products = [[div.a.string for div in all_divs]]
            with open(savepath, 'w', newline='', encoding=encoding) as f:
                wr = csv.writer(f)
                wr.writerows(products)
            driver.close()
            return products[0][0]

    # def naver_movie_review(self, naver_url):
    #     driver = webdriver.Chrome(driverpath)
    #     driver.get(naver_url)
    #     soup = BeautifulSoup(driver.page_source, 'html.parser')
    #     all_divs = soup.find_all('div', attrs={'class', 'tit3'})
    #     products = [[div.a.string for div in all_divs]]
    #     with open(savepath, 'w', newline='', encoding=encoding) as f:
    #         wr = csv.writer(f)
    #         wr.writerows(products)
    #     df = pd.read_csv(r'C:\Users\AIA\PycharmProjects\djangoProject\webcrawler\save\vs.csv')
    #     a = df.columns[0]
    #
    #     driver.close()
    #     return print(a)


#
#
music_menus = ["Exit", #0
                "bugs_music",#1
                ]

if __name__=="__main__":
    scrap = ScrapService()
    while True:
        [print(f"{i}. {j}") for i, j in enumerate(music_menus)]
        menu = input('메뉴선택: ')
        if menu == "0":
            print("종료")
            break

        elif menu == "1":
             scrap.naver_movie_review(naver_url)


        else:
            print("해당메뉴 없음")

#
#
#
#
#
#
#         elif menu == "1":
#             print("벅스")
#             scrap.domain = "https://music.bugs.co.kr/chart/track/day/total?chartdate="
#             scrap.query_string = "20221101"
#             scrap.parser = "lxml"
#             scrap.class_names=["title", "artist"]
#             scrap.tag_name = "p"
#             # BugsMusic(scrap)
#
#         elif menu == "2":
#             print("멜론")
#             scrap.domain = "https://www.melon.com/chart/index.htm?dayTime="
#             scrap.query_string = "2022110909"
#             scrap.parser = "lxml"
#             scrap.class_names = ["rank01", "rank02"]
#             scrap.tag_name = "div"
#             # MelonMusic(scrap)
#
#         elif menu == "3":
#             df_b = pd.read_csv(r"C:\Users\AIA\PycharmProjects\djangoProject\webcrawler\bugs_ranking.csv")
#             df_m = pd.read_csv(r"C:\Users\AIA\PycharmProjects\djangoProject\webcrawler\melon_ranking.csv")
#             print(df_b)
#             print(df_m)
#         else:
#             print("해당메뉴 없음")