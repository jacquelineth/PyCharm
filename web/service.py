from flask import Flask
app = Flask(__name__)

# default route
@app.route("/")
def hello():
    return "Hello World!"
# Test  with that URL to get the name
@app.route("/user/<username>")
def show_user(username):
    return "User: %s" % username
