"""
Module for working with experiments
"""
import json
import sqlite3
from typing import Dict, List

from abcd.script import script_input_vars
from abcd.types import ExperimentDef


def load_defs_from_database(db_path: str) -> Dict[str, List[ExperimentDef]]:
    """
    Load definitions from an sqlite database. Check schema.sql for db schema.
    """

    db = sqlite3.connect(db_path)
    cur = db.cursor()

    cur.execute("SELECT namespace, name, enabled, planout, compiled FROM scripts")

    defs = {}
    for row in cur.fetchall():
        namespace, name, enabled, planout, compiled_s = row
        if not enabled:
            continue

        if namespace not in defs:
            defs[namespace] = []

        script = json.loads(compiled_s)
        defs[namespace].append(ExperimentDef(name, script, script_input_vars(script)))

    return defs
