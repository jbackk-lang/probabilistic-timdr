import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import pytest
from probabilistic_timdr import threshold_schema as ts


def test_birthday_system_classifies_23_as_obiekt_22_as_szum():
    assert ts.BIRTHDAY_SYSTEM.classify(23) == "OBIEKT"
    assert ts.BIRTHDAY_SYSTEM.classify(22) == "SZUM"


def test_percolation_system_classifies_far_extremes_correctly():
    assert ts.PERCOLATION_SQUARE_SYSTEM.classify(0.9, L=20, trials=40, seed=3) == "OBIEKT"
    assert ts.PERCOLATION_SQUARE_SYSTEM.classify(0.1, L=20, trials=40, seed=3) == "SZUM"


def test_spherical_collapse_system_classifies_around_threshold():
    assert ts.SPHERICAL_COLLAPSE_SYSTEM.classify(2.0) == "OBIEKT"
    assert ts.SPHERICAL_COLLAPSE_SYSTEM.classify(1.0) == "SZUM"


def test_thresholds_are_not_all_the_same_value():
    """Sedno tego modulu: te trzy systemy MAJA WSPOLNY interfejs, ale
    NIE MAJA wspolnego progu R* - to byloby dokladnie tym bledem, ktory
    02_boundary_constant.md i 04_cosmic_application.md juz odrzucily w
    tresci (falszywa uniwersalnosc 0.5)."""
    thresholds = ts.compare_thresholds()
    assert thresholds["birthday"] == 0.5
    assert thresholds["percolation_square"] == 0.5
    assert thresholds["spherical_collapse"] == pytest.approx(1.686, abs=0.001)
    # birthday i percolation dzielą wartosc 0.5, ale z NIEZALEZNYCH wyprowadzen
    # (kombinatoryka vs dowod Kestena) - nie jest to ta sama stala "skopiowana",
    # sprawdzane przez roznicujace threshold_source ponizej.
    assert ts.BIRTHDAY_SYSTEM.threshold_source != ts.PERCOLATION_SQUARE_SYSTEM.threshold_source


def test_all_three_systems_have_distinct_threshold_sources():
    sources = {s.threshold_source for s in ts.ALL_SYSTEMS.values()}
    assert len(sources) == 3
