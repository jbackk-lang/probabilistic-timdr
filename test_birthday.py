import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import pytest
from probabilistic_timdr import birthday


# Tabela z 01_probability_basics.md (juz raz poprawiona w dokumencie) -
# ten test pilnuje, zeby kod dawal dokladnie te same wartosci.
TABLE = {
    2: 0.27, 5: 2.71, 10: 11.69, 13: 19.44,
    20: 41.14, 22: 47.57, 23: 50.73,
}


@pytest.mark.parametrize("n,expected_pct", list(TABLE.items()))
def test_matches_documented_table(n, expected_pct):
    p = birthday.exact_collision_probability(n) * 100
    assert p == pytest.approx(expected_pct, abs=0.01)


def test_pair_count():
    assert birthday.pair_count(2) == 1
    assert birthday.pair_count(3) == 3
    assert birthday.pair_count(4) == 6
    assert birthday.pair_count(13) == 78
    assert birthday.pair_count(23) == 253


def test_pair_count_negative_rejected():
    with pytest.raises(ValueError):
        birthday.pair_count(-1)


def test_probability_monotonic_increasing():
    ps = [birthday.exact_collision_probability(n) for n in range(1, 60)]
    assert all(b >= a for a, b in zip(ps, ps[1:]))


def test_probability_is_one_past_pigeonhole():
    assert birthday.exact_collision_probability(366) == 1.0
    assert birthday.exact_collision_probability(400) == 1.0


def test_probability_zero_at_n_le_1():
    assert birthday.exact_collision_probability(0) == 0.0
    assert birthday.exact_collision_probability(1) == 0.0


def test_first_n_crossing_threshold_reproduces_23():
    """Ten test odtwarza samo serce '02_boundary_constant.md': prog 0.5
    jest pierwszy raz przekroczony przy N=23, nie przy innej wartosci."""
    assert birthday.first_n_crossing_threshold(0.5) == 23


def test_first_n_crossing_threshold_invalid_range():
    with pytest.raises(ValueError):
        birthday.first_n_crossing_threshold(1.5)
    with pytest.raises(ValueError):
        birthday.first_n_crossing_threshold(0.0)
