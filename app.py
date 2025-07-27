from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "This is a Flask app running on port 5000!"

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)
