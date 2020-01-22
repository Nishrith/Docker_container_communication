#!/usr/bin/env python
from flask import Flask, request, redirect, url_for, jsonify
import pandas as pd

# create app
app = Flask(__name__)

@app.route('/')
def dataframe():
    data = {
        'A': [1,2,3],
        'B': [4,5,6],
    }
    a = pd.DataFrame(data=data)
    print(a)
    json_data = a.to_json(orient='table')
    return json_data

# run app
if __name__ == '__main__':
    app.run(port=8000, host='0.0.0.0', debug=True)
