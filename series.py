from imdb import IMDb
import matplotlib.pyplot as plt

ia = IMDb()
seriesList = ['Breaking Bad', 'Game of Thrones']

for s in seriesList:
    allFoundSeries = ia.search_movie(s)
    tvSeries = allFoundSeries[0]

    for series in allFoundSeries:
        if series.data['kind'] == 'tv series':
            tvSeries = series 
            break        

    seriesID = tvSeries.movieID

    wholeSeries = ia.get_movie_episodes(seriesID)

    seasons=wholeSeries['data']['episodes']

    ratings = []
    timeline = []
    i =1
    for key in sorted(seasons):
        episodes=seasons[key]
        for epNo in sorted(episodes):
            episode = episodes[epNo]
            print('Season:'+str(key)+' Episode:'+str(epNo)+" Rating:"+str(episode.data['rating']))
            ratings.append(episode.data['rating'])
            timeline.append(i)
            i+=1

    plt.plot(timeline, ratings, label=s ) 
    plt.legend()
  
# naming the x axis 
plt.xlabel('Episodes') 
# naming the y axis 
plt.ylabel('Rating') 
  
# giving a title to my graph 
plt.title('Series Rating Graph') 
plt.show()
print(ratings)