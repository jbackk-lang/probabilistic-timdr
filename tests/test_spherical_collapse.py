import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import pytest
from probabilistic_timdr import spherical_collapse


def test_closed_form_matches_documented_value():
    """04_cosmic_application.md cytuje delta_crit ~ 1.686."""
    assert spherical_collapse.delta_crit_closed_form() == pytest.approx(1.686, abs=0.001)


def test_symbolic_derivation_matches_closed_form():
    """To jest istota tego modulu: wyprowadzenie z rozwiazania
    cykloidalnego (niezalezna sciezka) powinno zgadzac sie z zamknietym
    wzorem az do wielu cyfr, nie tylko w przyblizeniu do 3 miejsc."""
    derived = spherical_collapse.derive_delta_crit_symbolic()
    closed = spherical_collapse.delta_crit_closed_form()
    assert derived == pytest.approx(closed, rel=1e-9)


def test_symbolic_derivation_matches_literature_value():
    derived = spherical_collapse.derive_delta_crit_symbolic()
    assert derived == pytest.approx(1.6865, abs=0.001)
