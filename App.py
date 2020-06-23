import os
from flask import Flask, json, jsonify, request
import TwitterAPI


app = Flask(__name__)



@app.route('/')
def home_teste():
    return jsonify({"HELLO":"WORLD"})

@app.route('/api')
def get_tweets():
    # Chamaremos de 'q' nossa pesquisa na URL. -> /api?q=nossaquery 
    query = request.args.get('q')
    return jsonify(TwitterAPI.pesquisa(query))



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 33507))
    app.run(host='0.0.0.0', port=port)
