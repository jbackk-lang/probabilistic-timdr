"""
threshold_schema.py — działająca wersja schematu z 03_timdr_mapping.md:

    R_total >= R* => OBIEKT
    R_total <  R* => SZUM

W dokumencie markdown R_total i R* są etykietami pojęciowymi — nie ma tam
żadnego wzoru na policzenie którejkolwiek z nich (przyznane wprost w
TIMDR_POROWNANIE.md, punkt 1). Ten moduł nadaje temu schematowi
implementację, ale CELOWO NIE jako jedną uniwersalną funkcję z jednym
uniwersalnym progiem — to byłby dokładnie ten błąd, który 02 i 04 już
poprawiły w tekście (0.5 nie jest uniwersalne; δ_crit≈1.686 to inna
liczba z innego wyprowadzenia).

Zamiast tego: `ThresholdSystem` to kontener wiążący RAZEM metrykę R_total,
jej próg R* i jawne źródło tego progu. Trzy zarejestrowane instancje
(`BIRTHDAY_SYSTEM`, `PERCOLATION_SQUARE_SYSTEM`, `SPHERICAL_COLLAPSE_SYSTEM`)
pokazują trzy NIEZALEŻNE progi (0.5 z kombinatoryki, 0.5 z symulacji
perkolacji, 1.686 z kolapsu sferycznego) pod wspólnym interfejsem
klasyfikacji — nie pod wspólną wartością liczbową.
"""

from dataclasses import dataclass
from typing import Callable

from . import birthday, percolation, spherical_collapse


@dataclass(frozen=True)
class ThresholdSystem:
    name: str
    describe_r_total: str
    describe_r_star: str
    r_star: float
    threshold_source: str  # skąd pochodzi R* - żeby nie zgadywać
    compute_r_total: Callable[..., float]

    def classify(self, *args, **kwargs) -> str:
        """Zwraca 'OBIEKT' jesli R_total >= R*, w przeciwnym razie 'SZUM'."""
        r_total = self.compute_r_total(*args, **kwargs)
        return "OBIEKT" if r_total >= self.r_star else "SZUM"


BIRTHDAY_SYSTEM = ThresholdSystem(
    name="paradoks_urodzin",
    describe_r_total="P(>=1 wspolnych urodzin) dla N osob, wzor dokladny",
    describe_r_star="0.5 - rownowaga miedzy istnieniem a nieistnieniem kolizji",
    r_star=0.5,
    threshold_source="kombinatoryka (01_probability_basics.md)",
    compute_r_total=lambda n, days=365: birthday.exact_collision_probability(n, days),
)

PERCOLATION_SQUARE_SYSTEM = ThresholdSystem(
    name="perkolacja_kwadratowa_wiazaniowa",
    describe_r_total="prawdopodobienstwo perkolacji (spanning) na siatce L x L, symulacja MC",
    describe_r_star="0.5 - dokladny prog z dowodu samodualnosci sieci (Kesten 1980)",
    r_star=0.5,
    threshold_source="Kesten 1980, dualnosc sieci kwadratowej (02_boundary_constant.md)",
    compute_r_total=lambda p, L=40, trials=150, seed=0: percolation.spanning_probability(p, L, trials, seed),
)

SPHERICAL_COLLAPSE_SYSTEM = ThresholdSystem(
    name="kolaps_sferyczny",
    describe_r_total="liniowo ekstrapolowany kontrast gestosci delta dla danej fluktuacji",
    describe_r_star="~1.686 - z rozwiazania cykloidalnego kolapsu top-hat (formalizm Pressa-Schechtera)",
    r_star=spherical_collapse.delta_crit_closed_form(),
    threshold_source="kolaps sferyczny top-hat, tlo Einsteina-de Sittera (04_cosmic_application.md)",
    compute_r_total=lambda delta: delta,
)


ALL_SYSTEMS = {
    "birthday": BIRTHDAY_SYSTEM,
    "percolation_square": PERCOLATION_SQUARE_SYSTEM,
    "spherical_collapse": SPHERICAL_COLLAPSE_SYSTEM,
}


def compare_thresholds() -> dict:
    """Zwraca {nazwa_systemu: R*} dla wszystkich zarejestrowanych systemow —
    uzyteczne, zeby na pierwszy rzut oka zobaczyc, ze progi NIE sa takie
    same (0.5, 0.5, ~1.686), mimo wspolnego interfejsu klasyfikacji."""
    return {name: sys.r_star for name, sys in ALL_SYSTEMS.items()}
