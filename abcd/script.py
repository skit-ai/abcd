"""
Planout script related utilities
"""

from typing import List, Dict, Union
from pydash import py_


def collect_script_operator(script: Union[Dict, List], operator: str) -> List[Dict]:
    """
    Walk down the script and collect usage of operator.
    """

    nodes = []

    if isinstance(script, dict):
        if script.get("op") == operator:
            nodes.append(script)

        skip_keys = ["op", "var"]
        for key, value in script.items():
            if key not in skip_keys:
                nodes.extend(collect_script_operator(value, operator))

    elif isinstance(script, list):
        nodes.extend(py_.flatten([collect_script_operator(node, operator) for node in script]))

    return nodes


def script_input_vars(script: Dict) -> List[str]:
    """
    Return a list of vars which should be supplied as input to the given
    script.

    Planout seems to return something even when the input to script is
    underspecified. But we don't like this.

    This is a very rudimentary function assuming that the script doesn't
    overwrite any input parameter.
    """

    set_vars = {node["var"] for node in collect_script_operator(script, "set")}
    get_vars = {node["var"] for node in collect_script_operator(script, "get")}

    return sorted(get_vars - set_vars)
