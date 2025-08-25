from flask import Flask, render_template
import redis

app = Flask(__name__)

# Connect to Redis container
r = redis.Redis(host='redis', port=6379, decode_responses=True)

# Reset counter at startup
r.set('visits', 0)

@app.route('/')
def hello_welcome():
    # Show current count without incrementing
    count = r.get('visits')
    if count is None:
        count = 0
    else:
        count = int(count)
    return render_template('index.html', count=count)

@app.route('/count')
def count_page():
    # Increment the counter in Redis
    count = r.incr('visits')
    return render_template('index.html', count=count)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
