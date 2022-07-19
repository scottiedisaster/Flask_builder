import os

project = input("Flask Project/site name. Eg Flask_app: ")

pwd = os.getcwd()
print(pwd)
os.mkdir(project)
os.chdir(project)
app = open('app.py', 'w')
app.write('''from flask import Flask

app = Flask(__name__)
app.config.from_object('config')''')

config = open('config.py', 'w')
config.write('''DEBUG = True''')
os.mkdir('static')
os.mkdir('templates')
folder = os.listdir()
print(folder)