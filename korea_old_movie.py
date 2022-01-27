import pandas as pd
import csv
import json
import requests
import numpy as np
movie_list = []
a= 1
for i in range(1990,2007):
  
  url =f'https://kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json?key=f5eef3421c602c6cb7ea224104795888&openStartDt={i}&openEndDt={i}&itemPerPage=100'
  res = requests.get(url)
  text = res.text

  d = json.loads(text)
  
  
  for i in d['movieListResult']['movieList']:
    title = i['movieNm'].replace(' ','')
    genre =i['repGenreNm']
    openDt = i['openDt'][:4]
    movie_list.append([a,openDt,title,genre])
    a+=1
    
movie_data = pd.DataFrame(movie_list, columns= ['movieid','openDt','title','genre'])


# save csv
# from google.colab import drive
# drive.mount('drive')
# movie_data.to_csv('movie_data.csv')
# !cp movie_data.csv 'drive/My Drive/'
