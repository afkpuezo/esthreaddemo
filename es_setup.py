"""
Adds the index and starter data to the es server.
Will drop/delete any existing data in the index.

Used these docs: https://elasticsearch-py.readthedocs.io/en/v7.11.0/

@author: Andrew Curry
"""
from elasticsearch import Elasticsearch


es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
print("ping", es.ping())
es.indices.delete(index='actions-index', ignore=[400, 404])
action_list_1 = "Print1to1000,Print1001to2000"
action_list_2 = "Print1to1000,Print1001to2000,Print2001to3000"
action_list_3 = "Print1to1000,Print1001to2000,Print2001to3000,Print3001to4000"
res = es.index(index='actions-index', id=1, body={'name' : 1, 'actions' : action_list_1})
res = es.index(index='actions-index', id=2, body={'name' : 2, 'actions' : action_list_2})
res = es.index(index='actions-index', id=3, body={'name' : 3, 'actions' : action_list_3})
# verify that it worked
es.indices.refresh(index="actions-index")
res = es.search(index='actions-index', body={"query": {"match_all": {}}})
#res = es.search(
#        index='actions-index', 
#        params= {'size': 1}, 
#        body={"query": {"match": {'name' : 1}}})
for hit in res['hits']['hits']:
    print(hit['_source']['actions'])