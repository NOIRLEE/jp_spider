'''
@Author :LI_JIA_HAO
@Email ：291630817@qq.com
'''
import json

from flask import Flask,request,jsonify,render_template
from selenium_test import *
from flask_cors import CORS
app = Flask(__name__)
CORS(app,supports_credentials=True)
@app.route('/cjjc')
def cjjc():
    try:
        key = request.args.get('key')
        result = cjjc_spider(key)
        str1 = ''
        for i in result:
            if type(i) == str:
                str1 += i
            else:
                str1 += str(i)
        data = {
            'msg':'ok',
            'result':str1
        }
        return jsonify(data)
    except Exception as e:
        print(e)
        return jsonify({
            'msg': '访问失败',
            'status': 'error'
        })

@app.route('/dic')
def dictionary():
    try:
        key = request.args.get('key')
        result = dictionary_spider(key)
        str1 = ''
        for i in result:
            if type(i) == str:
                str1 += i
            else:
                str1 += str(i)
        data = {
            'msg': 'ok',
            'result': str1
        }
        return jsonify(data)
    except Exception as e:
        print(e)
        return

@app.route('/koto')
def koto():
    try:
        key = request.args.get('key')
        result = dictionary_spider(key)
        str1 = ''
        for i in result:
            if type(i) == str:
                str1 += i
            else:
                str1 += str(i)
        data = {
            'msg': 'ok',
            'result': str1
        }
        return jsonify(data)
    except Exception as e:
        print(e)
        return

@app.route('/')
def hello_world():

    return render_template('index.html')


if __name__ == '__main__':
    app.run()
