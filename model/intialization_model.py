from elasticsearch import Elasticsearch
from sentence_transformers import SentenceTransformer
from indexMapping import indexMapping

import pandas as pd

## Set up elasticSearch
es = Elasticsearch(
    "https://localhost:9200",
    basic_auth=("elastic", "chatb0t**"),
    ca_certs="~/Desktop/project/Bible_Chatbot_SBERT/cert/ca.crt"
)

if not es.ping():
    raise ValueError("Not connected to ElasticSearch")

print("passed")

# Prepare the data
df = pd.read_json("data/nave/topics.json")
# add error catch

# Intialize SBERT model 
model = SentenceTransformer('all-mpnet-base-v2')
print("sucessful: sbert model created!")

# Save the model locally
model.save('sbert/saved_model')
print("Model successfully saved!")

# Convert the topic_name to a vector using BERT model
df["vector"] = df["topic_name"].apply(lambda x: model.encode(x))

## Create new index in ElasticSearch
es.indices.create(index="topics", mappings =indexMapping)

## Ingest the data into index
record_list = df.to_dict("records")
for record in record_list:
    try: 
        es.index(index="topics", document=record,id=record["topic_name"])
    except Exception as e:
        print(e)
