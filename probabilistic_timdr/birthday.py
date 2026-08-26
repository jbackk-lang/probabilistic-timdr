"""
birthday.py — dokładna kombinatoryka paradoksu urodzin (01_probability_basics.md,
02_boundary_constant.md).

Implementuje dokładnie te dwie wielkości, o których mówią dokumenty:
- liczbę par w grupie N osób: C(N,2),
- prawdopodobieństwo, że co najmniej dwie z N osób mają urodziny tego
  samego dnia (przy `days` równomiernie rozłożonych, domyślnie 365,
  bez roku przestępnego — standardowe uproszczenie podręcznikowe).

Wzór dokładny (bez przybliżeń, bez pośrednich zaokrągleń):

    P(≥1 wspólnych urodzin) = 1 - days! / ((days-N)! * days**N)
                            = 1 - prod_{i=0}^{N-1} (days-i)/days

Tabela w 01_probability_basics.md została zweryfikowana względem tego
dokładnego wzoru (patrz test_birthday.py) — w tym referencyjna wartość
50.73% dla N=23, powszechnie cytowana w literaturze.
"""

from math import comb


def pair_count(n: int) -> int:
    """Liczba nieuporządkowanych par w grupie n osób: C(n,2)."""
    if n < 0:
        raise ValueError("n musi być nieujemne")
    return comb(n, 2)


def exact_collision_probability(n: int, days: int = 365) -> float:
    """P(co najmniej dwie z n osób mają urodziny tego samego dnia).

    Liczone jako dopełnienie iloczynu (bez pośrednich zaokrągleń, bez
    wzoru przybliżonego typu 1 - exp(-n^2/(2*days))) — dokładna wartość
    kombinatoryczna.
    """
    if n < 0:
        raise ValueError("n musi być nieujemne")
    if n > days:
        # gołębnik: przy n > days kolizja jest pewna
        return 1.0

    p_no_collision = 1.0
    for i in range(n):
        p_no_collision *= (days - i) / days
    return 1.0 - p_no_collision


def first_n_crossing_threshold(threshold: float = 0.5, days: int = 365, max_n: int = None) -> int:
    """Najmniejsze N, dla którego exact_collision_probability(N, days) >= threshold.

    Domyślnie threshold=0.5 odtwarza "próg brzegowy 0.5" z
    02_boundary_constant.md i powinno zwrócić 23 dla days=365.
    """
    if not (0.0 < threshold < 1.0):
        raise ValueError("threshold musi być w (0,1)")
    n = 1
    limit = max_n if max_n is not None else days + 1
    while n <= limit:
        if exact_collision_probability(n, days) >= threshold:
            return n
        n += 1
    raise ValueError(f"próg {threshold} nie osiągnięty do n={limit}")
