from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello Nagaraj DevOps World!"

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)