Academic Abstract
Currently, religion and technology have significant influences on Americans politically and socially. Despite increases in digital biblical studies, there is a gap in research in digital engagement with the Bible. Hence, this project developed a chatbot that allows users to interact with the Bible digitally. Nave’s Topical Bible supplies the chatbot’s thematic interpretation of the Bible while the English Standard Version supplies the actual biblical verses. Using the digital tools, Sentence-Bidirectional Encoder Representations from Transformers (SBERT) and Elastic Search, the chatbot’s performance depends greatly on the user input: shorter or clearer user inputs performed best, while longer or abstract user inputs posed challenges for the chatbot. Despite its limitations, the chatbot proves that machine learning can be used to enhance engagement with the Bible through its interactive and simple platform.

Introduction
This chatbot has been developed using SBERT and Elastic Search. 

To develop this project on your own, follow the instructions below. Changes must be made in order to go into production (found at https://www.elastic.co/guide/en/elasticsearch/reference/8.16/docker.html#docker-prod-prerequisite).

Steps For ElasticSearch Using Docker
1. Install Docker
2. Start Docker instance, entering the following lines of code:
    docker network create elastic
    docker pull docker.elastic.co/elasticsearch/elasticsearch:8.16.0
    docker run --name es01 --net elastic -p 9200:9200 -it -m 1GB docker.elastic.co/elasticsearch/elasticsearch:8.16.0
        - Output should start with:
         ✅ Elasticsearch security features have been automatically configured!
    
    docker cp es01:/usr/share/elasticsearch/config/certs/http_ca.crt .
    curl --cacert http_ca.crt -u elastic:$PASSWORD for elastic search https://localhost:9200
3. Store API key and password for elastic user in .env file

Steps for Elastic Search Using Docker Compose
1. Follow https://www.elastic.co/blog/getting-started-with-the-elastic-stack-and-docker-compose

Steps For Data:
1. Enter folder for data:
    cd data
2. Nave's Topical Bible -
    wget http://www.justverses.com/downloads/zips/nave.zip
    mkdir nave
    unzip nave.zip -d nave
    rm nave.zip

3. English Standard Version (of the Bible) - clone https://github.com/honza/bibles

Steps to Run Chatbot:
    venv/bin/activate
    cd model
    python run_flask.py

If python run_flask.py, make sure Docker instance is running! 
