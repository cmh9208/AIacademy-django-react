import os
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup
from dataclasses import dataclass
import pandas as pd

import os
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup
from dataclasses import dataclass
import pandas as pd



@dataclass
class ScrapVO:
    html = ''
    parser = ''
    domain = ''
    query_string = ''
    headers = {}
    tag_name = ''
    fname = ''
    class_names = []
    artists = []
    titles = []
    diction = {}
    df = None

    def dict_to_dataframe(self):
        print(len(self.diction))
        self.df = pd.DataFrame.from_dict(self.diction, orient='index')

    def dataframe_to_csv(self):
        path = r'C:\Users\AIA\PycharmProjects\djangoProject\webcrawler\melon_ranking.csv'
        self.df.to_csv(path, sep=',', na_rep="NaN", header=None)

