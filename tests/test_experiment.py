from abcd.experiment import load_defs_from_database


def test_dir_loading():
    defs = load_defs_from_database("./tests/assets/db.sqlite")

    assert list(defs.keys()) == ["test"]
    assert len(defs["test"]) == 1
