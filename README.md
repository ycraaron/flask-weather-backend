# 3 Branches
 - This repo has 3 braches.
 - master: weather API
 - merge_interval: a tail recursion algorithm of merging a list of interval.
 - stack_tower: algorithm for stacking a bunch of books in to a stable tower.


## Weather API
1. A worker that fetches the current weather data for HK and SG every minute.
2. Store the temperature and humidity, etc data with timestamps in MongoDB
3. Provide a RESTFUL API endpoint to query the weather data from the database. 

## Links

- Backend: [Website](http://13.59.162.183:8000/weather?city=HK)
- Linkedin Profile: [https://www.linkedin.com/in/craaronyang/]

## Tech stack
     - Flask + MongoDB + Python

## Functionality
   1. Collect weather data from pyowm.
   2. Prepare and process data, store the data into MongoDB.

## Installation
  - make sure mongodb > 3.4 is installed and running
  - git clone this repo
  - pip3 install -r dev-requirement.txt OR pip3 install flask pymongo -y
  - pip3 install pyowm

## Run
  ### Run worker to get weather data:
  `
  $/path/to/python3 worker.py
  `
  
  ### Run server:
  ` 
  $/path/to/python3 app.py
  `
  

## Test use case:
  - http://13.59.162.183:8000/weather?city=HK
  - http://13.59.162.183:8000/weather?city=HK&start=2017-11-23T04:08:05&end=2017-12-24T04:08:05
  - http://13.59.162.183:8000/weather?city=HK&start=2017-13-23T04:08:05&end=2017-15-24T04:08:05
  - http://13.59.162.183:8000/weather?city=HK&start=2017-11-13T04:08:05&end=2017-12-24T04:08:05
  - http://13.59.162.183:8000/weather?city=HK&start=2017-11-13T04:08:05&end=2017-10-24T04:08:05
  - http://13.59.162.183:8000/weather?city=SG&start=2017-11-13T04:08:05&end=2017-10-24T04:08:05
  - http://13.59.162.183:8000/weather?city=H
  



