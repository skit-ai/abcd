"""
abcd allocation server

Usage:
  abcd [--port=<port>]

Options:
  --port=<port>      Port for server [default: 8813]
"""

from docopt import docopt

from flask import Flask

APP = Flask(__name__)


@APP.route("/")
def hello_world():
    return "hello"


def main():
    args = docopt(__doc__)

    port = int(args["--port"])
    APP.run(port=port)
