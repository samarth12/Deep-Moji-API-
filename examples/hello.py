from flask import Flask
from score_texts_emojis import model_deep
from flask import request
from flask import json


app = Flask(__name__)

@app.route("/")
def index():
    language1 = request.args.get('language1')
    language2 = request.args.get('language2')
    list_up = [language1, language2]
    return model_deep(list_up)

@app.route('/hello/<name>')
def hello(name):
    #return "Hello World!"
    return 'Hello' + name

@app.route("/members",methods=['POST'])
def members():
     req_data = request.get_json()
     print('PRINTED!!!!:', req_data)

     return model_deep(req_data['language'])

@app.route("/members/<string:name>/")
def getMember(name):
    return name

if __name__ == "__main__":
    app.run()
