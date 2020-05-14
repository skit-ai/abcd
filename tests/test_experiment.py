from abcd.experiment import load_def, load_defs_from_dir


def test_def_loading():
    assert load_def("./tests/assets/test.json")


def test_dir_loading():
    defs = load_defs_from_dir("./tests/")

    assert list(defs.keys()) == ["assets"]
    assert len(defs["assets"]) == 1
