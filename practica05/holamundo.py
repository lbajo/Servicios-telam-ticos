#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
from flask import Flask
app=Flask(__name__)
@app.route('/')
def index():
	return "hola mundo"
@app.route('/user/<name>')
def user(name):
	return "hola, "+name
if __name__ == '__main__':
	app.run(debug=True)