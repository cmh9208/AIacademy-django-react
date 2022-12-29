FROM python:3.9

WORKDIR /usr/src/app

COPY . .
COPY requirements.txt requirements.txt

RUN apt-get update

RUN pip install mysqlclient
RUN pip install imblearn
RUN pip install tweepy==3.10.0
RUN pip install -U pip wheel cmake
RUN pip install -r requirements.txt
RUN pip install opencv-python

RUN pip install torchvision
RUN pip install -r requirements.txt
RUN apt-get update


RUN apt-get update
RUN apt-get -y install libgl1-mesa-glx

RUN pip install --upgrade pip
RUN pip install wordcloud
RUN pip install -U imbalanced-learn
RUN pip install -r requirements.txt


CMD ["bin/sh", "-c", "python", "manage.py", "runserver", "0.0.0.0:8000"]
EXPOSE 8000
