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
from abcd.exceptions import UnderspecifiedInput, MissingExperiment
from flask import Flask, request, jsonify
from planout.experiment import SimpleInterpretedExperiment

APP = Flask(__name__)


@APP.route("/")
def abcd():
    return "abcd"


@APP.route("/allocate/<namespace>", methods=["POST"])
def allocate(namespace):
    params = request.json.get("params")

    try:
        # TODO: Run all experiments
        exp_def = APP.defs[namespace][0]
    except (IndexError, KeyError):
        raise MissingExperiment()

    missing_vars = set(exp_def.input_vars) - set(params.keys())
    if missing_vars:
        raise UnderspecifiedInput("Input is underspecified", sorted(missing_vars))

    exp = SimpleInterpretedExperiment(**params)
    exp.name = exp_def.name
    exp.script = exp_def.script

    return exp.get_params()


@APP.errorhandler(UnderspecifiedInput)
def handle_underspecified_input(error):
    response = jsonify(error.to_dict())
    response.status_code = 422
    return response


@APP.errorhandler(MissingExperiment)
def handle_missing_experiment(error):
    response = jsonify({"message": "Missing experiment"})
    response.status_code = 404
    return response


def main():
    args = docopt(__doc__)

    port = int(args["--port"])
    APP.defs = load_defs_from_dir(args["<experiments-dir>"])

    APP.run(port=port)
