# Copyright (c) Facebook, Inc. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

from pathlib import Path
import json
import tempfile
import pytest
from . import experiment as exp
from .fetchers import load_demo, load_csv, load_json, README_DEMOS


def test_fetcher_demo() -> None:
    xp = load_demo("demo")
    xp.validate()
    assert xp.datapoints
    with pytest.raises(exp.ExperimentFetcherDoesntApply):
        load_demo("something_else")


def test_fetcher_csv() -> None:
    xp = load_csv(str(Path(Path(__file__).parent.parent, ".circleci", "nutrients.csv")))
    xp.validate()
    assert xp.datapoints
    assert len(xp.datapoints) == 7637
    with pytest.raises(exp.ExperimentFetcherDoesntApply):
        load_csv("something_else")
    with pytest.raises(exp.ExperimentFetcherDoesntApply):
        load_csv("file_does_not_exist.csv")


def test_fetcher_json() -> None:
    with tempfile.NamedTemporaryFile("w+", suffix=".json") as tmpf:
        json.dump([{"id": 1, "metric": 1.0, "param": "abc"}, {"id": 2, "metric": 1.0, "param": "abc", "option": "def"}], tmpf)
        tmpf.flush()
        xp = load_json(tmpf.name)
        xp.validate()
        assert xp.datapoints
        assert len(xp.datapoints) == 2
    with pytest.raises(exp.ExperimentFetcherDoesntApply):
        load_json("something_else")


def test_demo_from_readme() -> None:
    for k, v in README_DEMOS.items():
        print(k)
        v().validate()._asdict()
