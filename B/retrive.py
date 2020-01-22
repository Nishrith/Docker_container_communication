from flask import Flask, request, redirect, url_for, jsonify
import requests, json
import pandas as pd

app = Flask(__name__)

with app.test_request_context():
    r = requests.get('http://data-frame:8000')
    print(r.content)

@app.route('/')
def index():
    content = r.content.decode('utf-8')
    json_content = json.loads(content)
    data_frame = pd.DataFrame(data=json_content['data'])
    return json_content

if __name__ == '__main__':
    app.run(port=5001,  host='0.0.0.0',debug=True)