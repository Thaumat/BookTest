from flask import Flask
from flask.ext.pymongo import PyMongo
import json

app = Flask(__name__)
app.config['MONGO_HOST'] = 'localhost'
app.config['MONGO_PORT'] = 27017
app.config['MONGO_DBNAME'] = 'CatWorks'

mongo = PyMongo(app, config_prefix='MONGO')


@app.route('/')
def home_page():
    catworks = mongo.db.cat_data.find()
    cat_data = []
    for catwork in catworks:
        cat_data.append(catwork)

    return json.dumps(cat_data)

@app.route('/search')
def search():
    return '''
        <form action="/search" method="post">
            Please enter the work name: <input name="workname" type="text" />
            <input value="Search" type="submit" />
        </form>
    '''


# @app.route('/search', methods=['POST'])
# def do_search():
#     author = request.forms.get('workname')
#     return "<p>Your meme is worthy. Doge is the only acceptable answer.</p>"
#     #return cat_data.find_one({"title": "Cathod"})


'''
@app.route('/works/<work_id>')
def works_page(work_id):
    work = mongo.db.cat_data.find_one({'_id': work_id})
    author_data = []
    for author in work['authors']:
        url_author = 'https://openlibrary.org' + author['author']['key'] + '.json'

        author_result = requests.get(url_author).text
        author_result_data = json.loads(author_result)
        author_result_data['key'] = author['author']['key']
        author_data.append(author_result_data)

    work['authors'] = author_data

    return json.dumps(work)
    '''


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)