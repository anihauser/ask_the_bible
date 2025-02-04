indexMapping = {
    "properties":{
        "topic_name":{
            "type": "text"
        },
        "vector":{
            "type": "dense_vector",
            "dims": 768,
            "index": True,
            "similarity": "l2_norm"
        }
    }
}