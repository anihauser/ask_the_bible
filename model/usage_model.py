from elasticsearch import Elasticsearch
from sentence_transformers import SentenceTransformer

import json
import pandas as pd
import random

def getVersesFromTopic(topic):
    verse_json = "data/nave/verses.json"
    with open(verse_json, 'r') as verse_file:
        verse_data = json.load(verse_file)
    
    verses = []
    for data in verse_data:
        if data["topic_key"] == topic and data["verse_txt"] != "Verse not found":
            verses.append(f'{data["verse_txt"]}" ({data["book_key"]} {data["chapter_nbr"]}:{data["verse_nbr"]}).')

    return verses

def run_model(user_input):
    ## Set up elasticSearch
    es = Elasticsearch(
        "https://localhost:9200",
        basic_auth=("elastic", "chatb0t**"),
        ca_certs="~/Desktop/project/Bible_Chatbot_SBERT/cert/ca.crt"
    )

    if not es.ping():
        raise ValueError("Not connected to ElasticSearch")

    ## Load SBERT Model
    model = SentenceTransformer('sbert/saved_model')

    ## Search the data
    user_input_vector = model.encode(user_input)

    query = {
        "field" : "vector",
        "query_vector": user_input_vector,
        "k" : 2,
        "num_candidates" : 500
    }

    ## Pick topics
    result_topics = es.knn_search(index="topics", knn=query, source= ["topic_name"])
    print("SCORE: ", result_topics["hits"]["hits"][0]['_score'])
    ## input topic, output verses: 
    topic = result_topics["hits"]["hits"][0]['_id']
    verses = getVersesFromTopic(topic)
    random_verse = random.choice(verses)

    return topic, random_verse

## test in script:
# user_input = "I want to dance"
# verses = run_model(user_input)
# print(verses)


