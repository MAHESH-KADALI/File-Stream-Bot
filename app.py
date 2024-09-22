from flask import Flask
app = Flask(name)

@app.route('/')
def hello_world():
    return 'Mahesh'


if name == "main":
    app.run()
