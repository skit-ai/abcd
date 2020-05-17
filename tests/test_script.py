from abcd.script import script_inputs
from abcd.experiment import load_def


def test_script_inputs():
    script = load_def("./tests/assets/test.json").script

    assert script_inputs(script) == ["id"]
