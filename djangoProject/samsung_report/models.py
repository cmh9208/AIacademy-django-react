from nltk.tokenize import word_tokenize
from konlpy.tag import Okt
import pandas as pd
from nltk import FreqDist
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re
from dataclasses import dataclass
import nltk


@dataclass
class Entity:
    context: str
    fname: str
    target: str

    @property
    def context(self) -> str: return self._context

    @context.setter
    def context(self, context): self._context = context

    @property
    def fname(self) -> str: return self._fname

    @fname.setter
    def fname(self, fname): self._fname = fname

    @property
    def target(self) -> str: return self._target

    @target.setter
    def target(self, target): self._target = target


class Service:
    def __init__(self):
        self.texts = []
        self.tokens = []
        self.stopwords = []
        self.freqtxt = []
        self.okt = Okt()

    def extract_tokens(self, payload):
        # print(' text 문서에서 token 추출')
        filename = payload.fname
        with open(filename, 'r', encoding='utf-8') as f:
            self.texts = f.read()
        # print(f'{self.texts[:300]}')

    def extract_hangeul(self):
        # print('한글 추출')
        texts = self.texts.replace('\n', ' ')
        tokenizer = re.compile(r'[^ ㄱ-힣]')
        self.texts = tokenizer.sub('', texts)
        # print(f'{self.texts[:300]}')

    def conversion_token(self):
        # print('토큰으로 변환')
        self.tokens = word_tokenize(self.texts)
        # print(f'{self.tokens[:300]}')

    def compound_noun(self):
        # print('복합명사는 묶어서 filtering 으로 출력')
        # print('예: 삼성전자의 스마트폰은 --> 삼성전자 스마트폰')
        noun_tokens = []
        for token in self.tokens:
            token_pos = self.okt.pos(token)
            temp = [txt_tag[0] for txt_tag in token_pos
                    if txt_tag[1] == 'Noun']
            if len("".join(temp)) > 1:
                noun_tokens.append("".join(temp))
        self.texts = " ".join(noun_tokens)
        # print(f'{self.texts[:300]}')

    def extract_stopword(self, payload):
        # print('스톱워드 추출')
        filename =  payload.fname
        with open(filename, 'r', encoding='utf-8') as f:
            self.stopwords = f.read()
        self.stopwords = self.stopwords.split(' ')

    def filtering_text_with_stopword(self):
        # print('스톱워드 필터링')
        self.texts = word_tokenize(self.texts)
        self.texts = [text for text in self.texts
                      if text not in self.stopwords]

        # print(f'{self.texts[:300]}')


    def frequent_text(self):
        # print('빈도수로 정렬')
        self.freqtxt = pd.Series(dict(FreqDist(self.texts))).sort_values(ascending=False)
        # print(f'{self.freqtxt[:100]}')
        # ls = []
        x = pd.Series(dict(FreqDist(self.texts))).sort_values(ascending=False)

        # [{'rank': '가능보고서위', 'title': '125'}] 구조로 맞추어 주어야 함.
        result = [{'rank' : f'{key}위', 'title': f'{value}'} for key, value in x.items()]
        result = [result[0]]
        # result = [{'rank' : f'{i+1}위', 'title': f'{j}'} for i, j in enumerate(dict(FreqDist(self.texts[:1])))]
        # print(result)
        print(result)
        return result





    def draw_wordcloud(self, payload):
        # print('워드 크라우드 생성')
        filename = payload.fname
        wcloud = WordCloud(filename,
                           relative_scaling=0.2,
                           background_color='white').generate(" ".join(self.texts))

        plt.figure(figsize=(12, 12))
        plt.imshow(wcloud, interpolation='bilinear')
        plt.axis('off')
        plt.show()


class Controller:
    def __init__(self):
        self.entity = Entity()
        self.service = Service()

    def download_dictionary(self):
        nltk.download('punkt')

    def data_analysis(self):
        self.download_dictionary()
        self.entity.fname = r'C:\Users\AIA\PycharmProjects\django-react-AIA\djangoProject\samsung_report\data\kr-Report_2018.txt'
        self.service.extract_tokens(self.entity)
        self.service.extract_hangeul()
        self.service.conversion_token()
        self.service.compound_noun()
        self.entity.fname = r'C:\Users\AIA\PycharmProjects\django-react-AIA\djangoProject\samsung_report\data\stopwords.txt'
        self.service.extract_stopword(self.entity)
        self.service.filtering_text_with_stopword()
        self.service.frequent_text()
        self.entity.fname = r'C:\Users\AIA\PycharmProjects\django-react-AIA\djangoProject\samsung_report\data\D2Coding.ttf'
        # self.service.draw_wordcloud(self.entity)
        return self.service.frequent_text()



if __name__ == '__main__':
    app = Controller()
    # app.download_dictionary()
    app.data_analysis()

# from konlpy.tag import Okt
# okt = Okt()
# okt.pos('삼성전자 글로벌센터 전자사업부', stem=True)
# with open('admin/crawling/data/kr-Report_2018.txt','r',
#           encoding='UTF-8') as f:
#     texts = f.read()
# print(texts)