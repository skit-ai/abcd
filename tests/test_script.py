from abcd.experiment import load_defs_from_database


def test_script_input_vars():
    defs = load_defs_from_database("./tests/assets/db.sqlite")
    assert defs["test"][0].input_vars == ["id"]
