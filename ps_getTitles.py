#----------------------------------------------------------#
import requests #access internet
import json #parse data
#----------------------------------------------------------#

sub = 'udub'
num = 1000
url = 'https://api.pushshift.io/reddit/search/submission/?size=' + str(num) + '&subreddit=' + str(sub);

#----------------------------------------------------------#
# run url and parse through json to retreive titles for each json item

r = requests.get(url, headers = {'User-agent': 'Chrome'})
def getposts():

    def gettitles(): #retreive  titles from r's json
        for post in r.json()['data']:
            y = post['title']
            yield(y)
    titles = gettitles()
    title_list = list(titles) #list out results
    return(title_list)
title_list = getposts() #run getposts to create title list

#----------------------------------------------------------#

#create json file

with open(str(num) + "posts.json", "w") as text_file:
    text_file.write(str(title_list))

print('json file with ' + str(num) + ' posts created')
