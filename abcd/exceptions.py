from typing import List


class UnderspecifiedInput(Exception):
    """
    Exception for situation when input to an experiment is underspecified.
    """

    def __init__(self, message: str, missing_vars: List[str]):
        super().__init__()
        self.message = message
        self.missing_vars = missing_vars

    def to_dict(self):
        return {
            "message": self.message,
            "missing_vars": self.missing_vars
        }
