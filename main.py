from elasticsearch import Elasticsearch

client = Elasticsearch("http://pg-bigdata-rbmp01.apac.bosch.com:9200/")

resp = client.info()

print(resp)

query = {
    "from":0,
    "size":1,
    "query": {
        "match_all": {
        }
    }
}

res = client.search(index="fts-v5",  body=query)

print(res["hits"]["total"])
