from flask import Flask, render_template, request, redirect
import smtplib
import urllib2
from time import gmtime, strftime
import pymongo
import simplejson
from pymongo import Connection
import re

import settings


connection = Connection(settings.mongo_domain, settings.mongo_port)
db = connection.commits
collection = db.commits
app = Flask(__name__, template_folder="views")

@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
    email = request.json["email"]
    message = request.json["message"]
    remote = request.json["remote"]

    message = message.split(" ")
    commitId = message[0]
    del message[0]
    message = " ".join(message)
    message = re.sub('\#cfln$', '', message)

    url = "https://api.github.com/legacy/user/email/"+email
    f = urllib2.urlopen(url)
    response = f.read()
    f.close()
    response = simplejson.loads(response)

    realname = response['user']['name']
    username = response['user']['login']
    time = strftime("%d-%m-%Y %H:%M:%S")
    picture = "http://www.gravatar.com/avatar/"+response['user']['gravatar_id']

    collection.insert({ "username":username, "realname":realname, "email":email, "picture":picture, "message":message, "commitId":commitId, "time":time, "remote":remote })

    return ""
  else:
    commits = collection.find().sort("time" , -1)
    return render_template('index.html', commits=commits)

if __name__ == '__main__':
  app.run(settings.flask_domain, settings.flask_port)

