import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import pytest
from probabilistic_timdr import percolation


def test_thresholds_table_matches_documented_values():
    """02_boundary_constant.md tabela: sprawdzamy, ze stale w kodzie
    zgadzaja sie z tym, co jest udokumentowane w markdown (co do 3
    miejsc po przecinku dla wartosci numerycznych bez wzoru zamknietego)."""
    t = percolation.PERCOLATION_THRESHOLDS
    assert t["square_bond"].p_c == 0.5
    assert t["triangular_site"].p_c == 0.5
    assert t["triangular_bond"].p_c == pytest.approx(0.347, abs=0.001)
    assert t["hexagonal_bond"].p_c == pytest.approx(0.653, abs=0.001)
    assert t["square_site"].p_c == pytest.approx(0.593, abs=0.001)
    assert t["cubic3d_bond"].p_c == pytest.approx(0.249, abs=0.001)


def test_only_square_bond_marked_as_simulated():
    """Uczciwosc: tylko jeden wpis powinien twierdzic, ze zostal
    zweryfikowany symulacja w TYM repo - reszta to cytaty z literatury."""
    t = percolation.PERCOLATION_THRESHOLDS
    simulated = [k for k, v in t.items() if v.source == "SIMULATED_HERE"]
    assert simulated == ["square_bond"]


def test_spanning_probability_rejects_out_of_range_p():
    with pytest.raises(ValueError):
        percolation.spanning_probability(-0.1)
    with pytest.raises(ValueError):
        percolation.spanning_probability(1.1)


def test_spanning_probability_monotonic_and_centered_near_half():
    """Rdzen weryfikacji: prawdopodobienstwo perkolacji powinno rosnac
    z p, byc bliskie 0 daleko ponizej 0.5, bliskie 1 daleko powyzej, i
    'w okolicy' 0.5 w posrodku (dokladny prog 0.5 to wynik Kestena dla
    L->nieskonczonosc; przy skonczonym L oczekujemy gladkiego przejscia,
    nie ostrego skoku - tolerancje ponizej sa dobrane pod to)."""
    L, trials, seed = 30, 80, 1
    low = percolation.spanning_probability(0.30, L=L, trials=trials, seed=seed)
    mid_low = percolation.spanning_probability(0.45, L=L, trials=trials, seed=seed)
    mid_high = percolation.spanning_probability(0.55, L=L, trials=trials, seed=seed)
    high = percolation.spanning_probability(0.70, L=L, trials=trials, seed=seed)

    assert low < 0.15, f"p=0.30 dalo zbyt wysokie P(span)={low} - oczekiwano bliskie 0"
    assert high > 0.85, f"p=0.70 dalo zbyt niskie P(span)={high} - oczekiwano bliskie 1"
    assert low < mid_low < mid_high < high, (
        "prawdopodobienstwo perkolacji nie rosnie monotonicznie z p: "
        f"{low}, {mid_low}, {mid_high}, {high}"
    )


def test_spanning_probability_deterministic_with_seed():
    a = percolation.spanning_probability(0.5, L=20, trials=40, seed=42)
    b = percolation.spanning_probability(0.5, L=20, trials=40, seed=42)
    assert a == b
