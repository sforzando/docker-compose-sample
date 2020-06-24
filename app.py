#!/usr/bin/env python3

import os

from flask import Flask
from redis import Redis


app = Flask(__name__)
redis = Redis(host="redis", port=6379)


@app.route("/")
def index():
    count = redis.incr("hits")
    return f"{os.getenv('TITLE', 'NO ENV')}: {count:04} hits."


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
