from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)


@app.route("/")
@cross_origin()
def hello_world():
    return {"text": "hello world"}


mocked_data = [{"text": "relevant"}, {"text": "irrelevant"}]


@app.route("/analyse", methods=['POST'])
@cross_origin()
def analyse_text():
    data = test()
    return data


def test():
    # do something NLP-related: only related comments are returned
    return [mocked_data[0]]
