# Holidays-bot
A bot that scrapes holidays of Brazil built using Scrapy

## Index
+ [Overview](#overview)
+ [Requirements](#requirements)
+ [Installation](#installation)

## Overview<a name="overview"></a>
This bot scrapes all holidays in Brazil from (http://feriados.com.br/).
The Brazilian Institute of Geography and Statistics (IBGE) reports 5570 cities in Brazil. This bot scrapes 5523 as of today.

The data can be extracted in JSON and it looks like this sample:

```
      {
         "city":{
            "uf":"mg",
            "cityName":"belo_horizonte",
            "holidays":{
               "facult":[
                  [
                     "15/02/2021",
                     "Carnaval"
                  ]
               ],
               "feriado":[
                  [
                     "25/12/2021",
                     "Natal"
                  ]
               ]
            }
         }
      }
```

It can also be saved in DBs, such as MongoDB with a code like this at the end of the spider file:

```
      {
          from pymongo import MongoClient
          client = MongoClient()
          client = MongoClient ('localhost', 27017)
          db = client['myBank']
          myCollection = db.myCollection
          myCollection_data = {
              'cities': city
          }
          result = myCollection.insert_one (myCollection_data)
      }
```

## Requirements<a name="requirements"></a>
+ [Python 3.6+](https://www.python.org/)
+ Uses [Scrapy](https://github.com/scrapy/scrapy), a web crawling & scraping framework for Python.
+ Text is represented in ASCII using [Unicode](https://pypi.org/project/Unidecode/)

## Installation<a name="installation"></a>
1. [Python 3](https://www.python.org/)
2. [Scrapy](https://scrapy.org/) 
3. [Unicode](https://pypi.org/project/Unidecode/)

   `pip3 install scrapy`
   `pip3 install unicode`

## Usage:
1. `cd <holidays/holidays/spiders>`
2. `scrapy crawl holidays -o holidays.json`
