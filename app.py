from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Rebel Wood"

app.run(host="0.0.0.0", port=80)

