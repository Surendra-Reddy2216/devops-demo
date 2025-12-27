from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from DevOps Pipeline! this is successful surendra reddy thanks
and i am so happy that i performed automation with jenkins by Ci"

app.run(host="0.0.0.0", port=80)

