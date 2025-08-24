# app.py

from flask import Flask
import redis

# Create Flask app
app = Flask(__name__)

# Connect to Redis container
r = redis.Redis(host='redis', port=6379)


@app.route('/')
def hello_welcome():
    return "Hello, welcome to this Coderco web!"

@app.route('/count')
def count():
    # Increment the counter in Redis
    count = r.incr('visits')
    return f'This page has been visited {count} times.'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
