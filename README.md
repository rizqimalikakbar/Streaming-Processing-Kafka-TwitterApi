# Streaming-Processing-Kafka-TwitterApi
Buatlah streaming processing menggunakan Kafka basic components yang consume/subscribe data dari API twitter. Data twitter yang digunakan is up to students, feel free to explore.

## Prerequisite
1. Python 3
2. Install Confluent Kafka Package
   `pip install confluent-kafka`
3. Install Tweepy
   `pip install tweepy`

## How to Run
1. Get the Bearer Token on Website Twitter Developer
2. Insert the Bearer Token to kafka_producer.py
3. Insert your topic to kafka_producer.py in `search term`
4. Activate Docker and start running `docker-compose.yml` with command
   `docker-compose build`
   `docker-compose up`
5. Running Kafka Producer with command `python3 kafka_producer.py`
