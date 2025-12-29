from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from DevOps Pipeline! this is successful uday reddy Thanks for the deployment i love creating pipelines"

app.run(host="0.0.0.0", port=80)

