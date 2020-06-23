import tweepy, json, os
    
def autentica():
    consumer_key = ""
    consumer_secret = ""
    access_token = ""
    access_token_secret = ""
    
    #verificar se existe arquivo credenciais, se não tiver, pegar variaveis do heroku
    try:
        with open('credenciais.json', 'r') as keys:
            k = json.load(keys)
            consumer_key = k["consumer_key"]
            consumer_secret = k["consumer_secret"]
            access_token = k["access_token"]
            access_token_secret = k["access_token_secret"]
    except Exception as e:
        #get heroku vars
        consumer_key = os.environ.get('consumer_key')
        consumer_secret = os.environ.get('consumer_secret')
        access_token = os.environ.get('access_token')
        access_token_secret = os.environ.get('access_token_secret')
    finally:
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
    
    return tweepy.API(auth)

def pesquisa(query):
    api = autentica()
    pesquisa = api.search(q=query, lang='pt')

    tweets = [] #lista vazia que colocaremos os tweets
    for t in pesquisa:
        tweets.append(t._json)
    print(f'pego {len(tweets)} tweets')

    dic = []
    for tweet in tweets: 
        dic.append({"nome":tweet["user"]["name"], "texto":tweet["text"]})

    return dic

    