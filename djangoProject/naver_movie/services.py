import csv
import os.path

import pandas as pd
from selenium import webdriver

from webcrawler.models import ScrapVO
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup


class ScrapService(ScrapVO):

    def __init__(self):
        global driverpath, naver_url, savepath, encoding
        driverpath = r"C:\Users\AIA\PycharmProjects\django-react-AIA\djangoProject\webcrawler\chromedriver.exe"
        savepath = r"C:\Users\AIA\PycharmProjects\django-react-AIA\djangoProject\naver_movie\naver_movie.csv"
        # 파일명 없으면 Permission Error 발생
        naver_url = "https://movie.naver.com/movie/sdb/rank/rmovie.naver"
        encoding = "UTF-8"



    def naver_movie_review(self):
        if os.path.isfile(savepath) == False:
            driver = webdriver.Chrome(driverpath)
            driver.get(naver_url)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            all_divs = soup.find_all('div', attrs={'class', 'tit3'})
            products = [[div.a.string for div in all_divs]]
            with open(savepath, 'w', newline='', encoding=encoding) as f:
                wr = csv.writer(f)
                wr.writerows(products)
            driver.close()
        else:
            df = pd.read_csv(savepath)
            # 프론트요구사항: 순위 rank, 제목 title 로 변경해서 리턴할 것
            result = [{'rank': f"{i+1}", 'title': f"{j}"} for i, j in enumerate(df)]
            return result






    #
    # def bugs_music(self, arg): # BeautifulSoup 기본크롤링
    #     soup = BeautifulSoup(urlopen(arg.domain + arg.query_string), 'lxml')
    #     title = {"class": arg.class_names[0]}
    #     artist = {"class": arg.class_names[1]}
    #     titles = soup.find_all(name=arg.tag_name, attrs=title)
    #     titles = [i.find('a').text for i in titles]
    #     artists = soup.find_all(name=arg.tag_name, attrs=artist)
    #     artists = [i.find('a').text for i in artists]
    #     [print(f"{i}위 {j} : {k}")  # 디버깅
    #      for i, j, k in zip(range(1, len(titles)), titles, artists)]
    #     diction = {}  # dict 로 변환
    #     for i, j in enumerate(titles):
    #         diction[j] = artists[i]
    #     arg.diction = diction
    #     arg.dict_to_dataframe()
    #     arg.dataframe_to_csv()  # csv파일로 저장
    #
    # def melon_music(self, arg): # BeautifulSoup 기본크롤링
    #     soup = BeautifulSoup(
    #         urlopen(urllib.request.Request(arg.domain + arg.query_string, headers={'User-Agent': "Mozilla/5.0"})),
    #         "lxml")
    #     title = {"class": arg.class_names[0]}
    #     artist = {"class": arg.class_names[1]}
    #     titles = soup.find_all(name=arg.tag_name, attrs=title)
    #     titles = [i.find('a').text for i in titles]
    #     artists = soup.find_all(name=arg.tag_name, attrs=artist)
    #     artists = [i.find('a').text for i in artists]
    #     [print(f"{i}위 {j} : {k}")  # 디버깅
    #      for i, j, k in zip(range(1, len(titles)), titles, artists)]
    #     diction = {}  # dict 로 변환
    #     for i, j in enumerate(titles):
    #         diction[j] = artists[i]
    #     arg.diction = diction
    #     arg.dict_to_dataframe()
    #     arg.dataframe_to_csv()  # csv파일로 저장
    #
    #
    #





music_menus = ["Exit", #0
                "BugsMusic",#1
                "MelonMusic",#2.
                ]
if __name__=="__main__":
    scrap = ScrapVO()
    while True:
        [print(f"{i}. {j}") for i, j in enumerate(music_menus)]
        menu = input('메뉴선택: ')
        if menu == "0":
            print("종료")
            break
        elif menu == "1":
            print("벅스")
            scrap.domain = "https://music.bugs.co.kr/chart/track/day/total?chartdate="
            scrap.query_string = "20221101"
            scrap.parser = "lxml"
            scrap.class_names=["title", "artist"]
            scrap.tag_name = "p"
            # BugsMusic(scrap)
        elif menu == "2":
            print("멜론")
            scrap.domain = "https://www.melon.com/chart/index.htm?dayTime="
            scrap.query_string = "2022110909"
            scrap.parser = "lxml"
            scrap.class_names = ["rank01", "rank02"]
            scrap.tag_name = "div"
            # MelonMusic(scrap)
        elif menu == "3":
            pass
            # df = pd.read_csv(f"{static}/save/cop/scp/bugs_ranking.csv")
            # print(df)
        else:
            print("해당메뉴 없음")