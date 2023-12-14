# This is a sample Python script.
from elasticsearch import Elasticsearch
from flask import Flask, request, jsonify
from service import search_films_in_elasticsearch, similarity_funct, search_jobs_in_elasticsearch, similarity_func, get_id
app = Flask(__name__)


# Route for handling search requests
@app.route('/linked_posts', methods=['GET'])
def linked_posts():
    query = request.args.get('id')
    new_id = get_id(query)
    result = similarity_func(new_id)

    return jsonify(result)


# Route for handling search requests
@app.route('/search', methods=['GET'])
def search_films():
    query = request.args.get('query')

    keyword = "Web Developer"
    Work_Type = "Temporary"
    new_Experience = "5"

    results = search_jobs_in_elasticsearch(
        keyword=keyword,
        new_Experience=new_Experience,
        Work_Type=Work_Type
    )

    return jsonify(results)


#test route
@app.route('/search_jobs', methods = ['Get'])
def test_api():
    keyword = request.args.get("keyword")
    new_Experience = request.args.get("new_Experience")
    Work_Type = request.args.get("Work_Type")

    results = search_jobs_in_elasticsearch(
        keyword=keyword,
        new_Experience=new_Experience,
        Work_Type=Work_Type
    )


    return jsonify(results)


if __name__ == '__main__':
    app.run(debug=True)















"""
es = Elasticsearch("http://localhost:9200")
es_body = es.info().body# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
mappings = {
        "properties": {
            "title": {"type": "text", "analyzer": "english"},
            "ethnicity": {"type": "text", "analyzer": "standard"},
            "director": {"type": "text", "analyzer": "standard"},
            "cast": {"type": "text", "analyzer": "standard"},
            "genre": {"type": "text", "analyzer": "standard"},
            "plot": {"type": "text", "analyzer": "english"},
            "year": {"type": "integer"},
            "wiki_page": {"type": "keyword"}
    }
}

es.indices.create(index="movies1", mappings=mappings)

print(es_body)

"""
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
