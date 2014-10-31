FROM ubuntu
MAINTAINER Bin Wang <binwang.cu@gmail.com>

RUN echo deb http://archive.ubuntu.com/ubuntu precise universe >> /etc/apt/sources.list
RUN apt-get update

## Development Family
RUN apt-get install -qy git

## Java Family
RUN apt-get install -qy openjdk-7-jre-headless 

## Python Family
RUN apt-get install -qy python python-dev python-distribute python-pip ipython

## Selenium 
RUN apt-get install -qy firefox xvfb 
RUN pip install selenium pyvirtualdisplay

## Scraping Family
RUN pip install beautifulsoup4 requests
RUN apt-get install -qy libffi-dev libxml2-dev libxslt-dev lib32z1-dev libssl-dev
RUN pip install lxml scrapy

