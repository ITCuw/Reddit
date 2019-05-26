#----------------------------------------------------------#

import requests #access internet

import json #parse data

import datetime #figure out today's date

import csv #reformat data to csv file
#----------------------------------------------------------#
#In order to retreive the posts, all you need to do is input the url of the
#subreddit that you want to pull posts from, and the amount of posts you want to pull
#. Then, this program will create a json file in the same folder as this file is in.

url = 'https://www.reddit.com/r/udub/'
num_posts = 1000


#----------------------------------------------------------#

todaykey = datetime.date.today() #return datetime object of today's date
datestr = todaykey.strftime("%B %d, %Y") #convert the datetime object to format of daily thread (mmmmm, dd, yyyy)
datestr2 = todaykey.strftime("%d %B, %Y") #convert the datetime object to format for writing out csv
searchkey = 'Daily FI discussion thread - {0}'.format(datestr) #search key
printkey = 'Daily FI thread - {0}'.format(datestr)

r = requests.get(url + '.json?count=' + str(num_posts), headers = {'User-agent': 'Chrome'}) #render latest 10 posts in json

#----------------------------------------------------------#
#//////////////////////////////////////////////////////////#
#//////////////////////////////////////////////////////////#
#//////////////////////////////////////////////////////////#
#----------------------------------------------------------#

#get url of the post

def snoo():
    def getfiurls(): #retreive  url from r's json
        for post in r.json()['data']['children']:
            y = post['data']
            yield(y)
    fi_urls = getfiurls()
    url_list = list(fi_urls) #list out results
    return(url_list)
url_list = snoo() #run snoo to create url list
# fi_link = url_list[post_index] #retreive url from post with specific index
# print(fi_link)

#----------------------------------------------------------#
#//////////////////////////////////////////////////////////#
#//////////////////////////////////////////////////////////#
#//////////////////////////////////////////////////////////#
#----------------------------------------------------------#

#create csv files and put url in csv file

# with open("snoopost.json", "w") as text_file:
#     text_file.write(str(fi_link))

with open("100posts.json", "w") as text_file:
    text_file.write(str(url_list))

# with open("snootext.json", "w") as text_file:
#     text_file.write(str(printkey))

print('json file with ' + str(num_posts) + ' posts created')

#----------------------------------------------------------#
#//////////////////////////////////////////////////////////#
#//////////////////////////////////////////////////////////#
#//////////////////////////////////////////////////////////#
#----------------------------------------------------------#
