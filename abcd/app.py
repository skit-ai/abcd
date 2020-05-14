"""
abcd allocation server

Usage:
  abcd <experiments-dir> [--port=<port>]

Arguments:
  <experiments-dir>    Directory to keep experiment files in. This directory
                       has sub-directories specifying namepace and compiled
                       planout files.

Options:
  --port=<port>        Port for server [default: 8813]
"""

from docopt import docopt

from abcd.experiment import load_experiments_from_dir
from flask import Flask

APP = Flask(__name__)


@APP.route("/")
def hello_world():
    return "hello"


def main():
    args = docopt(__doc__)

    port = int(args["--port"])
    experiments = load_experiments_from_dir(args["<experiments-dir>"])

    APP.run(port=port)
