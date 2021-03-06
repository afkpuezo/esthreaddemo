"""
A function to get the action list corresponding to an indicated program.

@author: Andrew Curry
"""
from elasticsearch import Elasticsearch


def get_action_list(program_name: str) -> str:
    """
    A function to get the action list corresponding to an indicated program.
    Returns "" if there is no matching program.
    Input should be in the format 'Program:n'
    """
    short_name = int(program_name[8:])
    es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    res = es.search(
        index='actions-index', 
        params= {'size': 1}, 
        body={"query": {"match": {'name' : short_name}}})
    for hit in res['hits']['hits']:
        return hit['_source']['actions']
    return ""