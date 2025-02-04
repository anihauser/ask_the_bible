import imp
from flask import Flask, render_template, request, jsonify
from waitress import serve
from usage_model import run_model

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    print("what", request.json['user_input'])
    user_input = request.json['user_input']

    # if not user input
    if not bool(user_input.strip()):
        return "please type in your question before hitting enter!"

    # model input and output
    topic, verse = run_model(user_input)
    result = {"topic" : topic,
                "verse" : verse}
    return jsonify(result)

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)
