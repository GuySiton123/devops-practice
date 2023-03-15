from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Guy The King of DevOps'

app.run(host='0.0.0.0', port=5000)
