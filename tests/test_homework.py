"""Autograding script."""

import os


def test_01():
    """Test word count job."""

    assert not os.path.exists("files/output/summary.csv")
    assert not os.path.exists("files/plots/top10_drivers.png")
