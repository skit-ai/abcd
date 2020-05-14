"""
Module for working with experiments
"""
import json
import os
from glob import glob
from typing import Dict, List

from abcd.types import ExperimentDef


def load_def(json_path: str) -> ExperimentDef:
    """
    Load a planout experiment definition from given json file.
    """

    exp_name = os.path.basename(json_path).rsplit(".", 1)[0]

    with open(json_path) as fp:
        return ExperimentDef(exp_name, json.load(fp))


def load_defs_from_dir(directory: str) -> Dict[str, List[ExperimentDef]]:
    """
    Load experiment definitions organized in sub directories specifying
    namespaces.
    """

    defs = {}

    json_files = glob(os.path.join(directory, "*", "*.json"))

    for json_file in json_files:
        namespace = os.path.basename(os.path.dirname(json_file))
        if namespace not in defs:
            defs[namespace] = []

        defs[namespace].append(load_def(json_file))

    return defs
