# Connect to Elasticsearch
from elasticsearch import Elasticsearch
es = Elasticsearch("http://localhost:9200")

# Function to search linked films in Elasticsearch
def similarity_funct(id):
    search_body = {
        "query": {
            "more_like_this": {
                "fields": [

                    "genre"
                ],
                "like": [{
                    "_index": "movies",
                    "_id": id}
                ],
                "max_query_terms": 3,
                "min_term_freq": 1
            }
        }
    }

    results = es.search(index="movies", body=search_body)
    results_hits = [hit for hit in results['hits']['hits']]

    return results_hits[:3]




# Function to search films in Elasticsearch

def search_films_in_elasticsearch(keyword=None, director=None, genre=None, ethnicity=None):
    # Build the Elasticsearch query based on the provided criteria
    query = {
        "query": {
            "bool": {
                "should": [],
                "must": [],
            }
        },
        "sort": {
            "year": {"order": "desc"}
        }
    }

    # Add filters based on provided arguments
    if keyword:
        query["query"]["bool"]["should"].extend([
            {"match": {"title": {"query": keyword, "boost": 3}}},
            {"match": {"director": {"query": keyword, "boost": 2}}},
            {"match": {"year": {"query": keyword, "boost": 1}}},
            {"match": {"plot": {"query": keyword, "boost": 1}}}]
        )

    if director:
        query["query"]["bool"]["must"].append({"match": {"director": director}})
    if genre:
        query["query"]["bool"]["must"].append({"match": {"genre": genre}})
    if ethnicity:
        query["query"]["bool"]["must"].append({"match": {"ethnicity": ethnicity}})

    # Execute the Elasticsearch search
    #print(query)
    # Replace 'your_index' with the actual index where your movies are stored
    result = es.search(index='movies', body=query)
    # print(result)
    # Extract and return the search results

    search_results = [hit for hit in result['hits']['hits']]
    #print(search_results)
    return search_results


def search_jobs_in_elasticsearch(keyword=None, new_Experience=None, Work_Type=None, Job_Posting_Date=None):
    # Build the Elasticsearch query based on the provided criteria
    query = {
        "query": {
            "bool": {
                "filter": [],

            }
        },
        "sort": {
            "Job Posting Date": {"order": "desc"}
        }
    }

    # Add filters based on provided arguments
    if keyword:
        query["query"]["bool"]["filter"].extend([
            {"match": {"Job Title": {"query": keyword, "boost": 3}}},
            {"match": {"Job Description": {"query": keyword, "boost": 1}}},
            {"match": {"Role": {"query": keyword, "boost": 2}}},
            ]
        )

    if Work_Type:
        query["query"]["bool"]["filter"].append({"match": {"Work Type": Work_Type}})
    if new_Experience:
        query["query"]["bool"]["filter"].append({"match": {"Experience": new_Experience}})

    # Execute the Elasticsearch search
    print(query)
    # Replace 'your_index' with the actual index where your movies are stored
    result = es.search(index='job_intern', body=query)
    # print(result)
    # Extract and return the search results

    search_results = [hit['_source'] for hit in result['hits']['hits']]
    print(search_results)
    return search_results



def get_id(id_intern):
    query = {
        "query": {
            "match": {
                "Job Id": id_intern
            }
        }
    }

    result = es.search(index="job_intern", body=query)

    if result['hits']['total']['value'] > 0:
        document_id = result['hits']['hits'][0]['_id']
        return(document_id)


def similarity_func(id):
    search_body = {
        "query": {
            "more_like_this": {
                "fields": [
                    "Job Title",
                    "Country"
                ],
                "like": [{
                    "_index": "job_intern",
                    "_id": id}
                ],
                "max_query_terms": 3,
                "min_term_freq": 1
            }
        }
    }

    results = es.search(index="job_intern", body=search_body)

    results_hits = [hit['_source'] for hit in results['hits']['hits']]

    return results_hits
