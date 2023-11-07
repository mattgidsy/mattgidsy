
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

#### lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

#### read the data
tweets_data = []
with open("project_twitter_data.csv") as data_f:
    for lin in data_f:
        st_ln = lin.strip()
        sp_ln = st_ln.split(",")
        tweets_data.append(sp_ln)
        
#strip punctuation             
def strip_punctuation(string):
    for s in string:
        if s in punctuation_chars:
            string =  string.replace(s,"")       
    return string

#check for negative words
def get_neg(string):
    neg_ct = 0
    ls = strip_punctuation(string.lower())
    str_lst = ls.split()
    for ele in str_lst:
        if ele in negative_words:
            neg_ct +=1
    return neg_ct

#check for positive words
def get_pos(string):
    pos_ct = 0
    ls = strip_punctuation(string.lower())
    str_lst = ls.split()
    for ele in str_lst:
        if ele in positive_words:
            pos_ct +=1
    return pos_ct

#evaluate the tweets and organize to list
judged_tweet_lst = [["Number of Retweets"," Number of Replies"," Positive Score"," Negative Score", " Net Score"]]
def judge_tweets(lst):
    for tweet in lst[1:]:
        rtw_val = tweet[1]
        rpl_val = tweet[2]
        pos_val = get_pos(tweet[0])
        neg_val = get_neg(tweet[0])
        net_val = pos_val - neg_val
        judged_tweet_lst.append([rtw_val,rpl_val,pos_val,neg_val,net_val])
        # print(f"Tweet positive words {pos_val}, negative words {neg_val}, avg {avg_val}")

def write_csv(lst):
    with open("resulting_data.csv", "w") as out_csv:
        for tweet in judged_tweet_lst:
            tweet_ln = ','.join([str(tweet[0]), str(tweet[1]), str(tweet[2]),str(tweet[3]),str(tweet[4])])
            out_csv.write(tweet_ln)
            out_csv.write('\n')
        
            
judge_tweets(tweets_data)
write_csv(judged_tweet_lst)

