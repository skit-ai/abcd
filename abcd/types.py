from dataclasses import dataclass
from typing import Dict, List


@dataclass
class ExperimentDef:
    name: str
    script: Dict
    input_vars: List[str]
