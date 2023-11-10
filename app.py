from flask import Flask
from collections import Counter
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    user_string = '안녕 안녕 반가워 반가워 반가워 반가워 반가워 신명진 신명진 신명진 취미는 코딩 코딩 특기는 코딩 코딩 코딩'
    counter = dict(Counter(user_string))
    result = json.dumps(counter)
    return result

