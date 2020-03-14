# WebScraper for IMDB

### Setup
##### 1. Create a virtual environment.
```
pip install virtualenv
virtualenv scrapyenv
```
##### 2. Activate new virtual environment
```
cd scrapyenv
.\Scripts\activate.bat
```
##### 3. Install scrapy library
```
pip install scrapy
```
Note: There might be problems around Twisted library. You will need to download it manually and install it locally.

### Create project
##### 1. Create a Scrapy project
```
scrapy startproject webscrapy
```
##### 2. Create a Spider
```
cd webscrapy
scrapy genspider imdb www.imdb.com
``` 
##### 3. Run Spider
```
scrapy crawl imdb -o imdbdata.json -t json
```