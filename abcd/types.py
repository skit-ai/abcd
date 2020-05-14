from dataclasses import dataclass
from typing import Dict


@dataclass
class ExperimentDef:
    name: str
    script: Dict
