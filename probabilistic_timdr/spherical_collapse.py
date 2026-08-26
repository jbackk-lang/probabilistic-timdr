"""
spherical_collapse.py — niezależne wyprowadzenie δ_crit ≈ 1.686
(04_cosmic_application.md), zamiast samego zacytowania stałej.

Kontekst fizyczny (formalizm Pressa-Schechtera, kolaps sferyczny top-hat
w tle Einsteina-de Sittera, Ω_m=1): przecomtona nadgęstość sferyczna
ewoluuje jak zamknięty pod-wszechświat, którego rozwiązanie parametryczne
("cykloida") to:

    t(θ)          ∝ (θ - sin θ)
    1 + δ_nonlin(θ) = 9 (θ - sin θ)² / (2 (1 - cos θ)³)

gdzie θ=0 to początek, θ=π to moment zawrócenia (turnaround), θ=2π to
formalny kolaps (δ_nonlin → ∞).

Ten moduł WYPROWADZA δ_crit z tego rozwiązania (rozwinięcie szeregiem
Taylora przy małym θ, dopasowanie do wzrostu liniowego t^(2/3) typowego
dla EdS), zamiast po prostu przypisać stałą 1.686 z literatury — patrz
`derive_delta_crit_symbolic()`. Wynik zgadza się z powszechnie cytowaną
wartością z formalizmu Pressa-Schechtera (patrz test_spherical_collapse.py
i README), co jest testem poprawności wyprowadzenia, nie założeniem.

Wyprowadzenie (skrót; pełne kroki w kodzie poniżej):
1. Rozwinięcie w szereg Taylora przy małym θ:
     t(θ)           ≈ θ³/6
     δ_nonlin(θ)    ≈ (3/20) θ²
2. Przy wczesnych czasach δ_nonlin ≈ δ_lin (liniowa teoria = nieliniowa
   teoria, dopóki δ << 1) — to definiuje stałą normalizacji łączącą
   δ_lin z parametrem rozwoju θ dla WSZYSTKICH θ (nie tylko małych),
   korzystając z tego, że w EdS δ_lin(t) ∝ t^(2/3) dokładnie:
     δ_lin(θ) = (3/20) · 6^(2/3) · (θ - sin θ)^(2/3)
3. Podstawiając θ=2π (kolaps):
     δ_crit = δ_lin(2π) = (3/20) · (12π)^(2/3) ≈ 1.6865
"""

from math import pi

try:
    import sympy as sp
    _HAS_SYMPY = True
except ImportError:  # pragma: no cover
    _HAS_SYMPY = False


def delta_crit_closed_form() -> float:
    """Zamknięty wzór δ_crit = (3/20)(12π)^(2/3), bez wyprowadzenia —
    to jest wartość powszechnie cytowana w literaturze (Press-Schechter).
    Użyj `derive_delta_crit_symbolic()`, żeby zobaczyć, skąd się bierze."""
    return (3.0 / 20.0) * (12.0 * pi) ** (2.0 / 3.0)


def derive_delta_crit_symbolic(series_order: int = 8) -> float:
    """Wyprowadza δ_crit z rozwiązania cykloidalnego (patrz docstring
    modułu), zamiast zwracać zacytowaną stałą. Zwraca wartość numeryczną,
    która powinna zgadzać się z `delta_crit_closed_form()` do wielu
    cyfr — to jest niezależna weryfikacja, nie ta sama linijka kodu.

    Wymaga sympy. Rzuca ImportError, jeśli sympy niedostępne (brak
    cichego fallbacku do stałej — to zaprzeczałoby sensowi funkcji)."""
    if not _HAS_SYMPY:
        raise ImportError(
            "derive_delta_crit_symbolic() wymaga sympy do wyprowadzenia "
            "symbolicznego; delta_crit_closed_form() nie wymaga sympy, "
            "ale nie jest wyprowadzeniem, tylko zacytowaną stałą."
        )

    theta = sp.symbols("theta", positive=True)

    t_expr = theta - sp.sin(theta)
    one_plus_delta_nl = 9 * (theta - sp.sin(theta)) ** 2 / (2 * (1 - sp.cos(theta)) ** 3)

    # Rozwinięcie w szereg Taylora przy małym theta (wczesne czasy)
    delta_nl_series = sp.series(one_plus_delta_nl - 1, theta, 0, series_order).removeO()

    # Wiodący człon powinien być (3/20)*theta^2 — sprawdzamy to wprost
    # (asercja, nie zaokrąglenie w locie), zamiast zakładać z góry.
    leading_coeff = sp.Poly(sp.expand(delta_nl_series), theta).coeff_monomial(theta**2)
    if leading_coeff != sp.Rational(3, 20):
        raise AssertionError(
            f"wiodacy wspolczynnik szeregu wyszedl {leading_coeff}, "
            "oczekiwano 3/20 - wyprowadzenie nie jest juz zgodne z "
            "przyjetym rozwiazaniem cykloidalnym, sprawdz wzor."
        )

    # delta_lin(theta) = (3/20) * 6^(2/3) * (theta - sin(theta))^(2/3),
    # dopasowane tak, by przy malym theta odtworzyc delta_nl ~ (3/20)*theta^2
    # (bo t(theta)~theta^3/6, wiec t^(2/3) ~ theta^2 / 6^(2/3)).
    delta_lin_of_theta = leading_coeff * (6 ** sp.Rational(2, 3)) * t_expr ** sp.Rational(2, 3)

    delta_crit_symbolic = delta_lin_of_theta.subs(theta, 2 * sp.pi)
    return float(delta_crit_symbolic)
