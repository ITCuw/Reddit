#----------------------------------------------------------#
import requests #access internet
import json #parse data
#----------------------------------------------------------#
#enter a subreddit and get the latest comment tree for that post

sub = 'udub'
url = 'https://api.pushshift.io/reddit/search/submission/?size=1&subreddit=' + str(sub);

#----------------------------------------------------------#
# run url and parse through json to retreive id for each json item

r = requests.get(url, headers = {'User-agent': 'Chrome'})
def getids():

    def getids(): #retreive  ids from r's json
        for post in r.json()['data']:
            y = post['id']
            yield(y)
    ids = getids()
    id_raw = list(ids) #list out results
    return(id_raw)
id_raw = getids() #run getposts to create id list

#----------------------------------------------------------#
# retrieve all comments from the reddit post

formatted_id = ''
for i in id_raw: #turn python list into formatted_id
    formatted_id = i

comments_url = 'https://api.pushshift.io/reddit/comment/search/?link_id=' + formatted_id  + '&limit=1000';

comments_r = requests.get(comments_url, headers = {'User-agent': 'Chrome'})

def getcomments():
    def getcomments(): #retreive  ids from r's json
        for i in comments_r.json()['data']:
            y = i['body']
            yield(y)
    comments = getcomments()
    comment_list = list(comments) #list out results
    return(comment_list)
comment_list = getcomments() #run getposts to create id list

#----------------------------------------------------------#

# create json file

with open(sub + "_comments.json", "w") as text_file:
    text_file.write(str(comment_list))

print('comments for latest post in r/' + sub + ' retrieved')
