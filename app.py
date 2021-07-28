import sys
from flask import Flask, request, logging
from flask_restful import Resource, Api, reqparse
import ast
import trans
import logging

app = Flask(__name__)


app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)


@app.route('/')
def index():
    return "Welcome"

@app.route('/courses/<string:word>',methods=['GET'])
def get_word(word):
    mot = trans.transliterate(word)

    return {'mot':mot}




if __name__ == '__main__':
    app.run()