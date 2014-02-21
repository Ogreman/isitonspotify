# check.py

import sys
import json
import argparse

from flask import (
    Flask, render_template,
)
from unipath import Path

TEMPLATE_DIR = Path(__file__).ancestor(1).child("templates")

app = Flask(__name__, template_folder=TEMPLATE_DIR)


@app.route('/')
def index():
    """
    Return the main view.
    """
    return render_template('index.html')


def main():
    """
    Main entry point for script.
    """
    app.run(debug=True)


if __name__ == '__main__':
    sys.exit(main())