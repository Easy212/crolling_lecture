from flask import Flask, render_template
from flask import request

import pymysql

#flask 객체 인스턴스 생성
app = Flask(__name__)

@app.route('/') #접속하는 url
def index():
    return render_template('index.html')

@app.route('/test4') #접속하는 url
def index1():
    return render_template('index4.html')

@app.route('/test5') #접속하는 url
def index2():
    return render_template('index5.html')

if __name__ == '__main__' :
    app.run(debug=True)
# host 등을 직접 지정 하고싶다면
# app.run(host="127.0.0.1", port="5000", debug=True)
