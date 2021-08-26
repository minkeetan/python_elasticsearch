from elasticsearch import Elasticsearch

client = Elasticsearch("http://pg-bigdata-rbmp01.apac.bosch.com:9200/")

resp = client.info()

print(resp)

res = client.search(index="fts-v5")
print("Got %d Hits:" % res['hits']['total']['value'])
