from flask import Flask, render_template, request, redirect
import smtplib

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		email = request.json["email"]
		message = request.json["message"]
		print email
		print message
		return render_template('index.html')
	else:
		print "GET"
		return render_template('index.html')

if __name__ == '__main__':
	app.run("akenn.org", 9000)
