"""
percolation.py — weryfikacja progu perkolacji z tabeli w 02_boundary_constant.md.

Ta tabela w dokumentach jest kontrprzykładem na "0.5 jest uniwersalne":

    | Siec / typ perkolacji            | p_c |
    | kwadratowa, wiazaniowa           | 0.5 (dokladnie, Kesten 1980) |
    | trojkatna, wezlowa               | 0.5 (dokladnie, dualnosc)    |
    | trojkatna, wiazaniowa            | ~0.347                        |
    | szesciokatna, wiazaniowa         | ~0.653                        |
    | kwadratowa, wezlowa              | ~0.593 (brak wzoru zamknietego)|
    | szescienna 3D, wiazaniowa        | ~0.249 (brak wzoru zamknietego)|

Co robi ten moduł:

1. **Symuluje** (Monte Carlo, unia-znajdź) perkolację wiązaniową na sieci
   kwadratowej — jedyny przypadek w tabeli, który jest jednocześnie (a)
   podstawowy do zaimplementowania w rozsądnej ilości kodu i (b) ma
   ścisły dowód (Kesten 1980, przez samodualność sieci kwadratowej) do
   porównania z wynikiem symulacji. Przy skończonym L próg wyostrza się
   dopiero przy L→∞ — symulacja odtwarza charakterystyczne przejście
   sigmoidalne wyśrodkowane blisko 0.5, nie idealny skok w 0.5 (to
   oczekiwany efekt skończonego rozmiaru, udokumentowany niżej).

2. **Cytuje** (nie symuluje) pozostałe pięć wartości z tabeli — są to
   ustalone wyniki literaturowe (Kesten 1980 dla progu dokładnego;
   Sykes-Essam 1964 dla relacji dualności trójkąt/sześciokąt; wartości
   numeryczne dla sieci bez wzoru zamkniętego pochodzą z rozległych
   symulacji w literaturze, nie są tu wyprowadzane od nowa). Oznaczenie
   "CITED" w słowniku `PERCOLATION_THRESHOLDS` jest tego jawnym zapisem —
   nie udawajmy, że ten moduł zweryfikował wszystkie sześć.
"""

from math import sin, pi
from typing import NamedTuple

import numpy as np


class ThresholdEntry(NamedTuple):
    lattice: str
    kind: str  # "bond" albo "site"
    p_c: float
    source: str  # "SIMULATED_HERE" albo "CITED"
    exact: bool  # czy wartość ma znany wzór zamknięty


PERCOLATION_THRESHOLDS = {
    "square_bond": ThresholdEntry("kwadratowa", "bond", 0.5, "SIMULATED_HERE", True),
    "triangular_site": ThresholdEntry("trojkatna", "site", 0.5, "CITED", True),
    "triangular_bond": ThresholdEntry("trojkatna", "bond", 2 * sin(pi / 18), "CITED", True),
    "hexagonal_bond": ThresholdEntry("szesciokatna", "bond", 1 - 2 * sin(pi / 18), "CITED", True),
    "square_site": ThresholdEntry("kwadratowa", "site", 0.5927460, "CITED", False),
    "cubic3d_bond": ThresholdEntry("szescienna_3D", "bond", 0.2488, "CITED", False),
}


def _spans_square_lattice(L: int, p: float, rng: np.random.Generator) -> bool:
    """Jedna próba: czy losowa konfiguracja wiązań (każde niezależnie
    obecne z prawdopodobieństwem p) na siatce L x L łączy górny i dolny
    wiersz (perkolacja pionowa). Union-find z kompresją ścieżek."""
    n = L * L
    parent = list(range(n))

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a: int, b: int) -> None:
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb

    def idx(r: int, c: int) -> int:
        return r * L + c

    h = rng.random((L, L - 1)) < p
    for r in range(L):
        for c in range(L - 1):
            if h[r, c]:
                union(idx(r, c), idx(r, c + 1))

    v = rng.random((L - 1, L)) < p
    for r in range(L - 1):
        for c in range(L):
            if v[r, c]:
                union(idx(r, c), idx(r + 1, c))

    top_roots = {find(idx(0, c)) for c in range(L)}
    bottom_roots = {find(idx(L - 1, c)) for c in range(L)}
    return len(top_roots & bottom_roots) > 0


def spanning_probability(p: float, L: int = 40, trials: int = 150, seed: int = 0) -> float:
    """Odsetek prób (z `trials`), w których losowa konfiguracja wiązań
    o gęstości `p` na siatce L x L perkoluje (łączy górę z dołem).

    Przy L→∞ powinno to dążyć do funkcji schodkowej w p=0.5 (Kesten
    1980). Przy skończonym L (domyślnie 40) oczekiwane jest gładkie
    przejście wyśrodkowane blisko 0.5 — patrz test_percolation.py dla
    konkretnych progów tolerancji użytych do weryfikacji tego.
    """
    if not (0.0 <= p <= 1.0):
        raise ValueError("p musi byc w [0,1]")
    rng = np.random.default_rng(seed)
    hits = sum(_spans_square_lattice(L, p, rng) for _ in range(trials))
    return hits / trials
