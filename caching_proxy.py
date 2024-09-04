#!/usr/bin/env python3

import requests
import argparse
from flask import Flask, request
from flask_caching import Cache
from requests import RequestException


# Creates a file system cache, using the 'cache' directory
def create_cache():
    cache_config = {
        "DEBUG": True,
        "CACHE_TYPE": "FileSystemCache",
        "CACHE_DIR": "cache",
    }
    cache = Cache(config=cache_config)
    return cache


# Names port and origin as optional flags for passing arguments when launching the app.
def get_args():
    parser = argparse.ArgumentParser(prog="CachingProxy", description="Caching server.")
    parser.add_argument("--port", default=3000)
    parser.add_argument("--origin")
    return parser.parse_args()


cache = create_cache()
args = get_args()

# Initializes Flask app
app = Flask(__name__)
cache.init_app(app)


# Sets the cache key to the full request path including query parameters
def cache_key():
    return request.full_path


# Registers a catch-all route, allowing app to act as a proxy for any GET requests made.
# Sets the cache key to the full path via cache_key().
@app.route("/<path:subpath>", methods=["GET"])
@cache.cached(key_prefix=cache_key)
def get_request(subpath):
    query_params = request.args
    if not subpath:
        return {"Missing request path"}, 400
    try:
        # If present, takes query params as a dict and converts them into a 
        # string of key and value pairs to append to the proxied url.
        query = query_params.to_dict(flat=False)
        if query:
            items = query.items()
            params = []
            for key, value in items:
                params.append(f"{key}={value[0]}")
            query_string = "&".join(params)
            get_url = f"{args.origin}/{subpath}?" + query_string
        else:
            get_url = f"{args.origin}/{subpath}"
        response = requests.get(get_url)
        response.raise_for_status()
        return response.text
    except RequestException as e:
        return {"Failed to retrieve data": str(e)}, 502


app.run(port=args.port)
