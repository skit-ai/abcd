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

from abcd.experiment import load_defs_from_dir
from flask import Flask, request
from planout.experiment import SimpleInterpretedExperiment

APP = Flask(__name__)


@APP.route("/")
def abcd():
    return "abcd"


@APP.route("/allocate/<namespace>", methods=["POST"])
def allocate(namespace):
    params = request.json.get("params")
    exp = SimpleInterpretedExperiment(**params)

    # TODO: Run all experiments
    exp_def = APP.defs[namespace][0]

    exp.name = exp_def.name
    exp.script = exp_def.script

    return exp.get_params()


def main():
    args = docopt(__doc__)

    port = int(args["--port"])
    APP.defs = load_defs_from_dir(args["<experiments-dir>"])

    APP.run(port=port)
