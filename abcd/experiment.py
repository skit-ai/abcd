"""
Module for working with experiments
"""
import json
import os
from glob import glob
from typing import Dict, List

from planout.experiment import SimpleInterpretedExperiment


class Experiment(SimpleInterpretedExperiment):
    """
    Experiment loaded from compiled planout file.
    """

    def __init__(self, name: str, script_path: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.script_path = script_path

    def loadScript(self):
        with open(self.script_path) as fp:
            self.script = json.load(fp)


def load_experiment(json_path: str) -> Experiment:
    """
    Load a planout experiment from given json file.
    """

    exp_name = os.path.basename(json_path).rsplit(".", 1)[0]
    return Experiment(exp_name, json_path)


def load_experiments_from_dir(directory: str) -> Dict[str, List[Experiment]]:
    """
    Load experiments organized in sub directories specifying namespaces.
    """

    experiments = {}

    json_files = glob(os.path.join(directory, "*", "*.json"))

    for json_file in json_files:
        namespace = os.path.basename(os.path.dirname(json_file))
        if namespace not in experiments:
            experiments[namespace] = []

        experiments[namespace].append(load_experiment(json_file))

    return experiments
