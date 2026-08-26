"""
probabilistic_timdr — kod obliczeniowy dla repozytorium probabilistic-timdr.

Kontekst: dokumenty markdown w tym repo (01-04, TIMDR_POROWNANIE.md) same
przyznają, że nie zawierają "żadnego wzoru obliczeniowego" (patrz
TIMDR_POROWNANIE.md, punkt 1) — R_total i R* były tam etykietami
pojęciowymi, nie policzalnymi wielkościami. Ten pakiet to naprawia dla
trzech konkretnych, zweryfikowanych twierdzeń z dokumentów:

- `birthday.py`      — dokładna kombinatoryka paradoksu urodzin (01, 02).
- `percolation.py`   — Monte Carlo weryfikacja progu perkolacji ≈0.5 dla
                        sieci kwadratowej wiązaniowej (02), plus cytowane
                        (nie symulowane tu) wartości dla pozostałych sieci
                        z tabeli w 02_boundary_constant.md.
- `spherical_collapse.py` — niezależne wyprowadzenie δ_crit≈1.686 (04) z
                        parametrycznego (cykloidalnego) rozwiązania kolapsu
                        sferycznego, a nie tylko zacytowana stała.
- `threshold_schema.py`  — uczciwa, DZIAŁAJĄCA wersja schematu
                        "R_total ≥ R* ⇒ OBIEKT" z 03_timdr_mapping.md:
                        każda domena rejestruje WŁASNY próg R* i WŁASNY
                        sposób liczenia R_total — schemat nie zakłada
                        jednej uniwersalnej stałej (to była poprawka już
                        wprowadzona w treści dokumentów; tu dostaje kod).

Żaden z tych modułów nie twierdzi, że te trzy domeny są "tym samym
mechanizmem" — to konkretna, przetestowana implementacja trzech osobnych,
poprawnie wyprowadzonych wyników, spięta wspólnym, jawnie nie-uniwersalnym
interfejsem klasyfikacyjnym.
"""

from . import birthday, percolation, spherical_collapse, threshold_schema

__all__ = ["birthday", "percolation", "spherical_collapse", "threshold_schema"]
