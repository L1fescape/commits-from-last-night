from flask import Flask, render_template, request, redirect
import smtplib
import urllib2

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
    email = request.json["email"]
    message = request.json["message"]

    url = "https://api.github.com/legacy/user/email/"+email
    f = urllib2.urlopen(url)
    response = f.read()
    f.close()

    print url
    print response
    print email
    print message


    return render_template('index.html')
  else:
    print "GET"
    return render_template('index.html')

if __name__ == '__main__':
  app.run("akenn.org", 9000)

