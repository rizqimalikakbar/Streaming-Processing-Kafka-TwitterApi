#Import Libraries
from confluent_kafka import Producer
import json
import time
import logging
import tweepy

#Setup Logger
logging.basicConfig(format='%(asctime)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='producer.log',
                    filemode='w')

logger = logging.getLogger()
logger.setLevel(logging.INFO)

p=Producer({'bootstrap.servers':'localhost:9092'})
print('Kafka Producer has been initiated...')

#Authentication Tokens
bearer_token = '**********AAJOPeQEAAAAAABVCsRyM0Bek1WUA6Z************3DLMr8k5WEIswfmIwTPxDCGdkGCvQ5zb1**********'

#Search Term
search_term = 'afcfutsal'

#Function for Twitter API v2 Authentication
def TwitterAPIv2(bearer_token, search_term):
    client = tweepy.Client(bearer_token)
    tweets = client.search_recent_tweets(query=search_term,
                                         max_results=25,
                                         tweet_fields = ['author_id','created_at','geo'])
    return tweets                

def receipt(err,msg):
    if err is not None:
        print('Error: {}'.format(err))
    else:
        message = 'Produced message on topic {} with value of {}\n'.format(msg.topic(), msg.value().decode('utf-8'))
        logger.info(message)
        print(message)
        
def main():
    for tweet in tweets.data:
        response = {
           'author_id': tweet.data['author_id'],
           'created_at': tweet.data['created_at'],
           'geo': tweet.data['geo']    
           }

        m=json.dumps(response)
        p.poll(1)

        p.produce('twitterapi', m.encode('utf-8'),callback=receipt)
        p.flush()
        time.sleep(3)
        
if __name__ == '__main__':
    tweets = TwitterAPIv2(bearer_token, search_term)
    main()