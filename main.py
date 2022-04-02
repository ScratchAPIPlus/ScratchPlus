from flask import Flask, render_template
import requests
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/settings')
def settings():
  return render_template('settings.html')

@app.route('/users/<username>')
def user(username):
    user = requests.get('https://scratchapiplus.mel0n7.repl.co/api/v1/users/' + username).json()
    return render_template('user.html', user=user)

app.run(host='0.0.0.0', port=8080)