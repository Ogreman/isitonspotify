# check.py

import sys
import json
import argparse
import requests 

from flask import (
    Flask, render_template, request, jsonify,
)
from unipath import Path

TEMPLATE_DIR = Path(__file__).ancestor(1).child("templates")

app = Flask(__name__, template_folder=TEMPLATE_DIR)

URL = "http://ws.spotify.com/search/1/artist.json"

@app.route('/')
def index():
    """
    Return the main view.
    """
    return render_template('index.html')


@app.route('/api/', methods=['GET'])
def api():
    artist = request.args.get('artist', '', type=str)
    response = requests.get(URL, params={ 'q': artist })
    return jsonify(
        {
            "success": True,
            "check": response.json()['info']['num_results'] > 0,
            "artist": artist,
        }
    )


def main():
    """
    Main entry point for script.
    """
    app.run(debug=True)


if __name__ == '__main__':
    sys.exit(main())