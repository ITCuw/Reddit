#----------------------------------------------------------#
import requests #access internet
import json #parse data

#----------------------------------------------------------#
#enter a subreddit and get the latest comment tree for that post

sub = 'philosophy'
comment_amount_cap = 10000
#----------------------------------------------------------#
# run url and parse through json to retreive body for each json item

def getallcomments():

    def getcomments(): #retreive  comments from r's json
        url = 'https://api.pushshift.io/reddit/search/comment/?subreddit=' + str(sub) + '&size=1000';
        r = requests.get(url, headers = {'User-agent': 'Chrome'})
        for post in r.json()['data']:
            y = post
            yield(y)
    comments = getcomments()
    print('INITIAL COMMENTS RETRIEVED')
    comments_raw = list(comments) #list out results
    length = len(comments_raw)
    while length > 0 and len(comments_raw) < comment_amount_cap: #continue retrieving data until there are no more comments or until you have reached the comment amount cap
        print('GETTING MORE COMMENTS BECAUSE INITIAL FILE HAD ' + str(length) + '...')
        comment_json = json.dumps(comments_raw) #convert json object into python list with set of dictionaries
        comment_obj = json.loads(comment_json)#^^^^^
        data_length = len(comment_obj)#get length of list
        date_constraint = comment_obj[data_length - 1]['created_utc']#get date that the 1000th comment was created to continue getting more comments
        def getmorecomments(): #retreive  comments from r's json
            newurl = 'https://api.pushshift.io/reddit/search/comment/?subreddit=' + str(sub) + '&size=1000' + '&before=' + str(date_constraint);
            r = requests.get(newurl, headers = {'User-agent': 'Chrome'})
            for post in r.json()['data']:
                y = post
                yield(y)
        additional_comments = getmorecomments()
        additional_comments_raw = list(additional_comments)
        print('MORE COMMENTS RETRIEVED...')
        length = len(additional_comments_raw)
        comments_raw += additional_comments_raw
        print( '------TOTAL COMMENT COUNT IS AT ' + str(len(comments_raw)) + '------')
    return(comments_raw)

comment_list = getallcomments() #run getcomments to create comment list

print('ALL COMMENTS RETRIEVED, CREATING JSON FILE...')
#----------------------------------------------------------#

# create json file

with open(sub + "_comments.json", "w") as text_file:
    text_file.write(str(comment_list))

print( str(len(comment_list)) + ' comments for latest post in r/' + sub + ' retrieved')

#----------------------------------------------------------#
