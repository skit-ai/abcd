from abcd.experiment import load_def


def test_script_input_vars():
    assert load_def("./tests/assets/test.json").input_vars == ["id"]
